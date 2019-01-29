#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """c what
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text='is cool'):
    """python is cool
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
