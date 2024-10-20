#!/usr/bin/env python3
from __future__ import print_function
import requests
import json
import sys
from time import perf_counter

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
image_url = 'http://' + addr + '/api/image'
add_url = 'http://' + addr + '/api/add/5/2'
raw_image_url = 'http://' + addr + '/api/rawimage'  # Hypothetical endpoint for raw image
json_image_url = 'http://' + addr + '/api/jsonimage'  # Hypothetical endpoint for JSON image
dot_product_url = 'http://' + addr + '/api/dotproduct'  # Hypothetical endpoint for dot product

if endpoint == 'add':
    # Start timer before loop and stop after, then divide by the number of test requests
    start_t1 = perf_counter()
    for i in range(num_tests):
        resp = requests.get(add_url, headers=headers_add)
        # decode response
        print("Response is", resp.text)
    stop_t1 = perf_counter()

    total = stop_t1 - start_t1
    avg = total / num_tests
    print("The average time taken for the /api/add endpoint was {}".format(avg))

elif endpoint == 'image':
    # Start timer before loop and stop after, then divide by the number of tests for the image endpoint
    start_t2 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(image_url, data=img, headers=headers)
        # decode response
        print("Response is", resp)
    stop_t2 = perf_counter()

    total = stop_t2 - start_t2
    avg = total / num_tests
    print("The average time taken from the /api/image endpoint was {}".format(avg))

elif endpoint == 'rawimage':
    # Start timer for raw image endpoint
    start_raw = perf_counter()
    for i in range(num_tests):
        resp = requests.get(raw_image_url)  # Assuming a GET request for raw image
        print("Response is", resp)
    stop_raw = perf_counter()

    total_raw = stop_raw - start_raw
    avg_raw = total_raw / num_tests
    print("The average time taken for the /api/rawimage endpoint was {}".format(avg_raw))

elif endpoint == 'jsonimage':
    # Start timer for json image endpoint
    start_json = perf_counter()
    for i in range(num_tests):
        resp = requests.get(json_image_url)  # Assuming a GET request for JSON image
        print("Response is", resp)
    stop_json = perf_counter()

    total_json = stop_json - start_json
    avg_json = total_json / num_tests
    print("The average time taken for the /api/jsonimage endpoint was {}".format(avg_json))

elif endpoint == 'dotproduct':
    # Start timer for dot product endpoint
    start_dot = perf_counter()
    for i in range(num_tests):
        resp = requests.get(dot_product_url)  # Assuming a GET request for dot product
        print("Response is", resp)
    stop_dot = perf_counter()

    total_dot = stop_dot - start_dot
    avg_dot = total_dot / num_tests
    print("The average time taken for the /api/dotproduct endpoint was {}".format(avg_dot))

else:
    print("Invalid endpoint specified.")
