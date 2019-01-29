#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask
from flask import render_template
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


@app.route("/c/<text>")
def cisfun(text):
    """c what
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def pythoniscool(text):
    """python is cool
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def intnumber(n):
    """accept integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def int_template(n):
    """only display when n is integer
    """
    return render_template('5-number.html', number=n)

app.run(host='0.0.0.0', port=5000)
