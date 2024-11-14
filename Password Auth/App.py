from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# In-memory user storage (replace with a database in production)
users = {}


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"success": False, "message": "Username already exists"}), 400

    users[username] = password
    return jsonify({"success": True, "message": "User registered successfully"})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True)