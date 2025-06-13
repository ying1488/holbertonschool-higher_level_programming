#!/usr/bin/python3
from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "homie somie"
auth = HTTPBasicAuth()
jwy = JWTManager(app)

users = {
    "user1": {
        "username": "user1", 
        "password": generate_password_hash("password"), 
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"), 
        "role": "admin"
    }
}

# Basic Authentication:
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# JWT Authentication:
#Login 
@app.route("/login", methods =["POST"])
def login():
    if request.get_json()is None:
        abort(400, "Not a json file")

    data = request.get_json()

    for x in ["username", "password"]:
        if x not in data:
            abort(400, "Missing attribute {}.".format(x))
    
    if data["username"] not in users or not check_password_hash(
        users[data["username"]]["password"], data["password"]):
            return jsonify({"msg": "Wrong username or password"}), 401

    access_token = create_access_token(identity=data["username"])
    return jsonify({"access_token": access_token})

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    currUser = get_jwt_identity()
    if currUser not in users or users[currUser]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"



# Run app
if __name__ == '__main__':
    app.run()