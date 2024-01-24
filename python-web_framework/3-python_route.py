"""
3-python_route.py
----------------

A Flask web application that displays "Hello HBNB!" at the root ("/"),
"HBNB" at the route "/hbnb", "C " followed by the value of the text
variable (underscores replaced with spaces) at the route "/c/<text>",
and "Python " followed by the value of the text variable (underscores
replaced with spaces) at the route "/python/<text>". The default value
for the text variable in the "/python" route is "is cool".

Usage:
    python3 3-python_route.py

Routes:
    /: Display "Hello HBNB!"
    /hbnb: Display "HBNB"
    /c/<text>: Display "C " followed by the value of the text variable
    /python/<text>: Display "Python " followed by the value of the text variable

Note: The application listens on 0.0.0.0, port 5000.
      Use the option strict_slashes=False in the route definition.
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C ' + escape(text.replace('_', ' '))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    return 'Python ' + escape(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
