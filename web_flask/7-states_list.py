#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def shutdown_session(exception=None):
    storage.close()

@app.route("/states_list")
def states_list():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


app.run(host='0.0.0.0', port=5000)
