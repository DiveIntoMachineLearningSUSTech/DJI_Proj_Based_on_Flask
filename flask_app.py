from flask import Flask, render_template, request

from db import close_db, query_by_name
import json


app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev', 
        DB_SERVER_IP = '47.75.87.76',
        DATABASE = 'segmentfault',
        COLLECTION = 'user_info_v2_local'
    )
app.teardown_appcontext(close_db)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        user_id = request.form['search']
        ret = query_by_name(user_id)
        try:
            obj = json.loads(ret)
        except json.JSONDecodeError:
            return ret
        return render_template(
            'base.html', skills=obj.get('skills'),
            user_name=obj.get('user_name'),
            education=obj.get('education'),
            contribution = "START",
            fans_num = obj.get("followers_count"),
        )

    else:
        return render_template(
                'base.html', 
                skills = [
                        "php",
                        "javascript",
                        "python",
                        "node",
                        "asp",
                        "net",
                        "html",
                        "bash",
                        "c"],
                user_name = "reboz",
                education = "北京大学",
                contribution = "START",
                fans_num = '465',
                )

print(__name__)