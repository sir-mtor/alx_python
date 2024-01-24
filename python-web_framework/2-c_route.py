"""
2-c_route.py
----------------

A Flask web application that displays "Hello HBNB!" at the root ("/"),
"HBNB" at the route "/hbnb", and "C " followed by the value of the text
variable (underscores replaced with spaces) at the route "/c/<text>".

Usage:
    python3 2-c_route.py

Routes:
    /: Display "Hello HBNB!"
    /hbnb: Display "HBNB"
    /c/<text>: Display "C " followed by the value of the text variable

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
