from datetime import timedelta

from flask import Flask, session, request

app = Flask(__name__, static_folder='', static_url_path='')
app.secret_key = "123456"
app.config["PERMANENT_SESSION_LIFETIME"] = 20


@app.route("/get/")
def get():
    if "username" in session:
        return "hello, {0}\n".format(session["username"])
    return 'hello, stranger\n'


# save session
@app.route("/login", methods=['POST'])
def login():
    session["username"] = request.form.get("username")
    session_id = request.cookies.get("session")
    return "login successful,%s" % session_id


# remove session
@app.route("/delete/")
def delete():
    session.pop("username", )
    return "delete  session successful"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)
