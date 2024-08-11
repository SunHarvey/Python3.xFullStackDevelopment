from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='')


@app.route("/user/<username>")
def sayHello(username):
    return "name is %s" % username


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "post is %d" % post_id


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='127.0.0.1:5000', port=5000)
