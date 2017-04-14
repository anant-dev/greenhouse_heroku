"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

import json
CORS(app)
@app.route('/get/' , methods = ['GET','POST'])
def get():
    with open("data.json", 'r') as file:
        return jsonify(json.loads(file.read()))


@app.route('/post/' , methods = ['GET','POST'])
def post():
    content = request.get_json()
    data = dict()
    data['temp'] = content.get('Temperature')
    data['humidity'] = content.get('Humidity')
    data['moisture'] = content.get('Soil Moisture')
    data['light'] = content.get('Light Intensity')
    with open("data.json", 'w') as file:
      file.write(json.dumps(data))
    return jsonify('success')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response



if __name__ == '__main__':
    app.run(debug=True)
