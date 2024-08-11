from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        msg = "response post"
    else:
        msg = "response get"
    return msg


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)
