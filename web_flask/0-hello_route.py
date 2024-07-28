#!/usr/bin/python3
"""Flask app starting """
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slahes=False)
def hello():
    """Say something on start"""
    return "Hello HBNB"

if name = '__main__':
    app.run(host='0.0.0.0', port=5000)
