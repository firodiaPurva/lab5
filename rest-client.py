#!/usr/bin/env python3
from __future__ import print_function
import requests
import sys
from time import perf_counter

# Parse command line arguments to indicate the endpoint and iterations to test
addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])
print(addr, endpoint, num_tests)

# Prepare headers for different HTTP requests
headers = {'content-type': 'image/png'}
headers_add = {'content-type': 'text/plain'}

# Load the image for the rawimg and jsonimg tests
img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

# Correct the URLs to include 'http://'
add_url = 'http://' + addr + '/api/add/5/2'
image_url = 'http://' + addr + '/api/image'
rawimg_url = 'http://' + addr + '/api/rawimg'
jsonimg_url = 'http://' + addr + '/api/jsonimg'
dotproduct_url = 'http://' + addr + '/api/dotproduct'

# Perform the tests based on the selected endpoint
if endpoint == 'add':
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
    print("The average time taken for the /api/image endpoint was {}".format(avg))

elif endpoint == 'rawimg':
    # Use POST for rawimg
    start_t3 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(rawimg_url, data=img, headers=headers)
        print("Response is", resp)
    stop_t3 = perf_counter()
    total = stop_t3 - start_t3
    avg = total / num_tests
    print("The average time taken for the /api/rawimg endpoint was {}".format(avg))

elif endpoint == 'jsonimg':
    # Use POST for jsonimg
    start_t4 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(jsonimg_url, data=img, headers=headers)
        print("Response is", resp)
    stop_t4 = perf_counter()
    total = stop_t4 - start_t4
    avg = total / num_tests
    print("The average time taken for the /api/jsonimg endpoint was {}".format(avg))

elif endpoint == 'dotproduct':
    # Use POST for dotproduct
    start_t5 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(dotproduct_url, headers=headers_add)
        print("Response is", resp.text)
    stop_t5 = perf_counter()
    total = stop_t5 - start_t5
    avg = total / num_tests
    print("The average time taken for the /api/dotproduct endpoint was {}".format(avg))

else:
    print("Invalid endpoint. Use 'add', 'image', 'rawimg', 'jsonimg', or 'dotproduct'.")
