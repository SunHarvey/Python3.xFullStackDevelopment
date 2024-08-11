from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)
