#!/usr/bin/env python3
from flask import Flask, request, Response
import jsonpickle
import numpy as np
from PIL import Image
import io
from time import perf_counter

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/image', methods=['POST'])
def test():
    r = request
    start_time = perf_counter()  # Start timing
    try:
        ioBuffer = io.BytesIO(r.data)
        img = Image.open(ioBuffer)
        response = {
            'width': img.size[0],
            'height': img.size[1]
        }
    except Exception as e:
        response = {'width': 0, 'height': 0}
    
    # Measure JSON encoding time
    encoding_start_time = perf_counter()
    response_pickled = jsonpickle.encode(response)
    encoding_time = perf_counter() - encoding_start_time
    print(f"JSON encoding time: {encoding_time:.6f} seconds")  # Log the time

    processing_time = perf_counter() - start_time  # Calculate processing time
    print(f"Image processing time: {processing_time:.6f} seconds")  # Log the time

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

    # Now we pickle the response and return it to the client as true JSON
    pickled = jsonpickle.encode(resp)
    return Response(response=pickled, status=200, mimetype="application/json")

# Start the Flask app
app.run(host="0.0.0.0", port=5000)
