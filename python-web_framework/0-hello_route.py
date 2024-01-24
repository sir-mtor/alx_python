"""
0-hello_route.py
----------------

A simple Flask web application that displays "Hello HBNB!".

Usage:
    python3 0-hello_route.py

Routes:
    /: Display "Hello HBNB!"

Note: The application listens on 0.0.0.0, port 5000.
      Use the option strict_slashes=False in the route definition.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
