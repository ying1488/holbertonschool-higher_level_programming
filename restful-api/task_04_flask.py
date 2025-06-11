#!/usr/bin/python3
"""Flask in action"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, jsonify, request
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
def show_username(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    
    output = users[username]
    output["username"] = username
    return jsonify(output)


if __name__ == "__main__":
    app.run()
    print ("server up!")