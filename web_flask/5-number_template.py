#!/usr/bin/python3
"""hbnb flask module setup"""
from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def home():
    """return a string at the root page"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """return a string at the /hbnb page"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """return a string with C starting"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """return a string with Python starting,
    default text is set to 'is cool'"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>/')
def is_number(n):
    """detect arg passed is number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>/')
def number_temp(n):
    """detect arg passed is number and render a html file"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
