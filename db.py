from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from flask import current_app, g

from bson.json_util import dumps


def get_db():
    if 'db_conn' not in g:
        client = MongoClient(host=current_app.config['DB_SERVER_IP'])
        g.db_conn = client
        
        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')
        except ConnectionFailure:
            return None

        g.db = client[current_app.config['DATABASE']][current_app.config['COLLECTION']]

    return g.db

def close_db(e=None):
    db = g.pop('db_conn', None)

    if db is not None:
        db.close()

def query_by_name(username):
    db = get_db()
    if db is None:
        return 'Can not connect to DB server: {}'.format(current_app.config['DB_SERVER_IP'])

    cursor = db.find({"user_name": username})
    if cursor.count() < 1:
        return 'No user info: {} collected in database'.format(username)
    else:
        return dumps(cursor[0])


if __name__ == '__main__':
    db = get_db()
    from pprint import pprint
    pprint(db.find_one())