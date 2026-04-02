from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)