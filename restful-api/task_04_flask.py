#!/usr/bin/python3
"""Flask in action"""
from flask import Flask

# Step 1 
app = Flask(__name__)

user = {}

@app.route("/")
def home():
    return "hell0"

@app.route("/data")
def data():
    return

@app.route("/")
def route():
    return