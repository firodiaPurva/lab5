#!/usr/bin/env python3
from flask import Flask, request, Response
import jsonpickle
import numpy as np
from PIL import Image
import io
import json

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/image', methods=['POST'])
def test():
    r = request
    try:
        ioBuffer = io.BytesIO(r.data)
        img = Image.open(ioBuffer)
        response = {
            'width': img.size[0],
            'height': img.size[1]
        }
    except:
        response = {'width': 0, 'height': 0}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/add/<int:x>/<int:y>', methods=['GET'])
def test_add(x, y):
    try:
        total = x + y
        resp = {
            'sum': total
        }
    except:
        resp = {
            'sum': 0
        }
    pickled = jsonpickle.encode(resp)
    return Response(response=pickled, status=200, mimetype="application/json")

@app.route('/api/rawimage', methods=['POST'])
def raw_image():
    r = request
    # Process raw image data (you can add your logic here)
    response = {'status': 'Received raw image'}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/jsonimage', methods=['POST'])
def json_image():
    r = request.get_json()
    image_data = r.get('image', None)
    # Process the image data (you can add your logic here)
    response = {'status': 'Received JSON image'}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/dotproduct', methods=['POST'])
def dot_product():
    r = request.get_json()
    vector_a = np.array(r.get('vector_a', []))
    vector_b = np.array(r.get('vector_b', []))
    result = np.dot(vector_a, vector_b)
    response = {'dot_product': result}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# Start the Flask app
app.run(host="0.0.0.0", port=5000)
