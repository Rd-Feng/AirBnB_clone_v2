#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """root route
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """hbnb
    """
    return "HBNB"


app.run(host='0.0.0.0', port=5000)
