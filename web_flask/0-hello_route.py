#!/usr/bin/python3
"""Flask app starting
flask script to start a web app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Say something on start
    listening: 0.0.0.0
    port: 5000
    """

    return "Hello HBNB"


if __name__ == '__main__':

    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
