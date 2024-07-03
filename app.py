#!/usr/bin/python3
"""This module handles the route for provisions pall"""

from flask import render_template, request, Flask

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/', strict_slashes=False, methods=["GET"])
def display():
    """To help us render the dispay page"""

    if request.method == 'GET':
        return render_template('landing_page.html')
   

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
