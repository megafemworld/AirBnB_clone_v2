#!/usr/bin/python3
"""Flask app starting
flask script to start a web app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """Say something on start
    listening: 0.0.0.0
    port: 5000
    """

    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """HBNB output"""

    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ display “C ”, followed by the value
    of the text variable"""

    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python/')
@app.route('/python/<text>')
def py(text="is cool"):
    """display “Python ”, followed by the value
    of the text variable"""

    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def num(n):
    """n is a number” only if n is an integer"""

    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def display_num(n):
    """display a HTML page only if n is an integer:"""

    return render_template('5-number.html', n=n)


if __name__ == '__main__':

    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
