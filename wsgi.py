import db
from flask import Flask, abort, url_for

application = Flask(__name__)

@application.route('/')
def index():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f"<li><a href='{url_for('user', username=username)} '>{user['name']}</a></li>"
        )
    html.append('</ul>')
    return '\n'.join(html)

def profile(username):
    user = db.users.get(username)

    if user:
        return f"""
        <h1>{user['name']}</h1>
        Lingua:{user['lang']}<br>
        <a href ='/'>Voltar</a>
    """
    else:
        return abort(404, "Usuario nao encontrado")

application.add_url_rule('/user/<username>/', view_func=profile, endpoint='user')