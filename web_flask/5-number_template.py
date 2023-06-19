#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

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


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_integer(n):
    """text"""
    if type(n) is int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_is_integer_html(n):
    """text"""
    if type(n) is int:
        return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
