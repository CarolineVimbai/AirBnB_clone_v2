#!/usr/bin/python3
"""write a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main():
    """returns text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route_hbnb():
    """text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """returns"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
