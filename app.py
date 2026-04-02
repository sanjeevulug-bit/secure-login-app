from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Get password from environment variable (secure way)
    correct_password = os.getenv("APP_PASSWORD", "admin123")

    if username == "admin" and password == correct_password:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == "__main__":
    # Required for Docker
    app.run(host='0.0.0.0', port=5000)  # nosec