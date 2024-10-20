#!/usr/bin/env python3
from flask import Flask, request, Response
import jsonpickle
import numpy as np
from PIL import Image
import io
import json

# Initialize the Flask application
app = Flask(__name__)

# Endpoint for handling image data and returning its dimensions
@app.route('/api/image', methods=['POST'])
def handle_image():
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

# Endpoint for adding two integers from URL path
@app.route('/api/add/<int:x>/<int:y>', methods=['GET'])
def handle_add(x, y):
    try:
        total = x + y
        resp = {'sum': total}
    except:
        resp = {'sum': 0}
    pickled = jsonpickle.encode(resp)
    return Response(response=pickled, status=200, mimetype="application/json")

# Endpoint for handling raw image data
@app.route('/api/rawimg', methods=['POST'])
def handle_raw_image():
    r = request
    try:
        img_data = np.frombuffer(r.data, dtype=np.uint8)
        response = {'image_size': len(img_data)}
    except:
        response = {'image_size': 0}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# Endpoint for handling JSON image data
@app.route('/api/jsonimg', methods=['POST'])
def handle_json_image():
    r = request
    try:
        json_data = json.loads(r.data)
        img_array = np.array(json_data['image_data'], dtype=np.uint8)
        response = {'json_image_size': img_array.size}
    except:
        response = {'json_image_size': 0}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# Endpoint for calculating the dot product of two arrays
@app.route('/api/dotproduct', methods=['POST'])
def handle_dot_product():
    r = request
    try:
        data = json.loads(r.data)
        vec1 = np.array(data['vector1'])
        vec2 = np.array(data['vector2'])
        dot_product = np.dot(vec1, vec2)
        response = {'dot_product': dot_product}
    except:
        response = {'dot_product': 0}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# Start Flask app
app.run(host="0.0.0.0", port=5000)
