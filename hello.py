from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
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