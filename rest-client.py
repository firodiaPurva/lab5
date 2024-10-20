#!/usr/bin/env python3
from __future__ import print_function
import requests
import json
import sys
from time import perf_counter
import numpy as np

# We parse command line arguments to indicate the endpoint and iterations to test as follows: machine, api route, number of runs
# python3 rest-client.py localhost add 1000

# The address of the server we are sending a request to
addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])
print(addr, endpoint, num_tests)

# Prepare headers for different HTTP requests
headers = {'content-type': 'image/png'}
headers_add = {'content-type': 'text/plain'}

img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
image_url = addr + '/api/image'
add_url = addr + '/api/add/5/2'
raw_image_url = addr + '/api/rawimage'  # Hypothetical endpoint for raw image
json_image_url = addr + '/api/jsonimage'  # Hypothetical endpoint for JSON image
dot_product_url = addr + '/api/dotproduct'  # Hypothetical endpoint for dot product

if endpoint == 'add':
    # Start timer before loop and stop after, then divide by the number of test requests
    start_t1 = perf_counter()
    for i in range(num_tests):
        resp = requests.get(add_url, headers=headers_add)
        print("Response is", resp.text)
    stop_t1 = perf_counter()

    total = stop_t1 - start_t1
    avg = total / num_tests
    print("The average time taken for the /api/add endpoint was {}".format(avg))

elif endpoint == 'image':
    start_t2 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(image_url, data=img, headers=headers)
        print("Response is", resp)
    stop_t2 = perf_counter()

    total = stop_t2 - start_t2
    avg = total / num_tests
    print("The average time taken from the /api/image endpoint was {}".format(avg))

elif endpoint == 'rawimage':
    start_t3 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(raw_image_url, data=img, headers=headers)
        print("Response is", resp)
    stop_t3 = perf_counter()

    total = stop_t3 - start_t3
    avg = total / num_tests
    print("The average time taken from the /api/rawimage endpoint was {}".format(avg))

elif endpoint == 'jsonimage':
    start_t4 = perf_counter()
    for i in range(num_tests):
        json_data = json.dumps({'image': img.decode('latin-1')})  # Encode image to JSON
        resp = requests.post(json_image_url, data=json_data, headers={'Content-Type': 'application/json'})
        print("Response is", resp)
    stop_t4 = perf_counter()

    total = stop_t4 - start_t4
    avg = total / num_tests
    print("The average time taken from the /api/jsonimage endpoint was {}".format(avg))

elif endpoint == 'dotproduct':
    start_t5 = perf_counter()
    vector_a = np.random.rand(1000)
    vector_b = np.random.rand(1000)
    resp = requests.post(dot_product_url, json={'vector_a': vector_a.tolist(), 'vector_b': vector_b.tolist()})
    print("Response is", resp)
    stop_t5 = perf_counter()

    total = stop_t5 - start_t5
    avg = total / num_tests
    print("The average time taken from the /api/dotproduct endpoint was {}".format(avg))

else:
    print("Invalid endpoint specified!")
