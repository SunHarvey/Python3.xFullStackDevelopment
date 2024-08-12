from flask import Flask, session, request
from flask_session import Session
from redis import Redis

app = Flask(__name__, static_folder='', static_url_path='')
app.secret_key = "123456"

app.config['SESSION_TYPE'] = 'redis'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = False
app.config["SESSION_KEY_PREFIX"] = "session:"
app.config["SESSION_REDIS"] = Redis(host='192.168.2.104', port=6379, db=0)
Session(app)


# get session
@app.route('/get/')
def get():
    if "username" in session:
        return "hello, {0}\n".format(session['username'])
    return "hello, stranger\n"


# save session
@app.route('/login', methods=["POST"])
def login():
    session["username"] = request.form.get("username")
    session_id = request.cookies.get("session")
    print(session_id)
    return "login successful,session_id={0}".format(session_id)


# delete session
@app.route('/delete/')
def delete():
    session.pop("username", None)
    return "delete successful"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)
