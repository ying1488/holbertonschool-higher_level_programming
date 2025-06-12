#!/usr/bin/python3
"""Flask in action"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return("Welcome to the Flask API!")

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def route():
    return "OK"

@app.route("/users/<username>")
def GetUsers(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    
    output = users[username]
    output["username"] = username
    return jsonify(output)

@app.route("/add_user", METHOD=["POST"])
def add_user():
    if request.get_json() is None:
        abort(400, "Not a JSON")
    req_data = request.get_json()

    if "username" not in req_data:
        return jsonify({"error": "Username is required"}), 400
    
    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }

    output = {
        "username": req_data["username"],
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    return jsonify({"message": "User added", "user": output}), 201



if __name__ == "__main__":
    app.run()
