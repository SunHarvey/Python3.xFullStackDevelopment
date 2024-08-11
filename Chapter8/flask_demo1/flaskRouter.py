from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='')


@app.route("/")
@app.route("/index")
def index():
    return "Index Page"


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='127.0.0.1:5000', port=5000)
