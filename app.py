"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

import json
CORS(app)


@app.route('/get/' , methods = ['GET'])
def get():
    with open("data.json", 'r') as file:
        return jsonify(json.loads(file.read()))


@app.route('/post/', methods=['GET','POST'])
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


@app.route('/data/', methods=['GET', 'POST'])
def min_max_data():
    if request.method == 'GET':
        with open("min_max_data.json", 'r') as file:
            return jsonify(json.loads(file.read()))
    content = request.get_json()
    data = dict(temp={}, humidity={}, moisture={}, light={})
    data['temp']['min'] = content.get('temperature_min')
    data['temp']['max'] = content.get('temperature_max')
    data['humidity']['min'] = content.get('humidity_min')
    data['humidity']['max'] = content.get('humidity_max')
    data['moisture']['min'] = content.get('soil_moisture_min')
    data['moisture']['max'] = content.get('soil_moisture_max')
    data['light']['min'] = content.get('light_intensity_min')
    data['light']['max'] = content.get('light_intensity_max')
    with open("min_max_data.json", 'w') as file:
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
