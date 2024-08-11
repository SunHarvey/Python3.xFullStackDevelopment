from flask import Flask, request

app = Flask(__name__, static_url_path='', static_folder='')


@app.route('/register_get', methods=['GET'])
def register_get():
    print("response type=", request.method)
    if request.method == "GET":
        username = request.args.get("username")
        password = request.args.get("password")
        password2 = request.args.get("password2")
        print("username={0}, password={1},password2={2}".format(username, password, password2))

        if password and len(password) >= 3 and password == password2:
            print("register successful")
        else:
            print("register failed")
            return "register failed,please confirm your password"

        if len(username) < 3:
            print("register failed, the length of username must large than three")
            return "register failed, the length of username must large than three"
        else:
            print("register successful")
        return "register successful"


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
