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
image_url = addr + '/api/image'
add_url = addr + '/api/add/5/2'

if endpoint == 'add':
    # Start timer before loop and stop after, then divide by the number of test requests
    start_t1 = perf_counter()
    for i in range(num_tests):
        resp = requests.get(add_url, headers=headers_add)
        # Decode response
        print("Response is", resp.text)
    stop_t1 = perf_counter()

    total = stop_t1 - start_t1
    avg = total / num_tests
    print("The average time taken for the /api/add endpoint was {}".format(avg))

elif endpoint == 'image':
    # Start timer before loop for the image endpoint
    start_t2 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(image_url, data=img, headers=headers)
        # Decode response
        print("Response is", resp)
    stop_t2 = perf_counter()

    total = stop_t2 - start_t2
    avg = total / num_tests
    print("The average time taken for the /api/image endpoint was {}".format(avg))

else:
    print("Invalid endpoint specified. Please use 'add' or 'image'.")
