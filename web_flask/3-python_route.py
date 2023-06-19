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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """to print /c"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text):
    """Display “Python ”"""
    return "".join(["Python ", text.replace("_", " ")])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
