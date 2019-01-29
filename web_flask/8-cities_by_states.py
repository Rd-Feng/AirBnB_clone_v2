#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage after each request
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_cities_list():
    """list states and cities sorted by name
    """
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
