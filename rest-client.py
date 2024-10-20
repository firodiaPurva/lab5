#!/usr/bin/env python3
from __future__ import print_function
import requests
import sys
from time import perf_counter

# Arguments: machine, api route, number of runs
addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])
print(addr, endpoint, num_tests)

# Prepare headers
headers = {'content-type': 'image/png'}
headers_add = {'content-type': 'text/plain'}

img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

# URLs for the different endpoints
add_url = addr + '/api/add/5/2'
image_url = addr + '/api/image'
rawimg_url = addr + '/api/rawimg'
jsonimg_url = addr + '/api/jsonimg'
dotproduct_url = addr + '/api/dotproduct'

# Measure performance for different endpoints
if endpoint == 'add':
    start_t1 = perf_counter()
    for i in range(num_tests):
        resp = requests.get(add_url, headers=headers_add)
        print("Response is", resp.text)
    stop_t1 = perf_counter()
    avg = (stop_t1 - start_t1) / num_tests
    print("The average time taken for the /api/add endpoint was {}".format(avg))

elif endpoint == 'image':
    start_t2 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(image_url, data=img, headers=headers)
        print("Response is", resp)
    stop_t2 = perf_counter()
    avg = (stop_t2 - start_t2) / num_tests
    print("The average time taken for the /api/image endpoint was {}".format(avg))

elif endpoint == 'rawimg':
    start_t3 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(rawimg_url, data=img, headers=headers)
        print("Response is", resp.text)
    stop_t3 = perf_counter()
    avg = (stop_t3 - start_t3) / num_tests
    print("The average time taken for the /api/rawimg endpoint was {}".format(avg))

elif endpoint == 'jsonimg':
    start_t4 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(jsonimg_url, data=img, headers=headers)
        print("Response is", resp.text)
    stop_t4 = perf_counter()
    avg = (stop_t4 - start_t4) / num_tests
    print("The average time taken for the /api/jsonimg endpoint was {}".format(avg))

elif endpoint == 'dotproduct':
    start_t5 = perf_counter()
    for i in range(num_tests):
        resp = requests.post(dotproduct_url, headers=headers_add)
        print("Response is", resp.text)
    stop_t5 = perf_counter()
    avg = (stop_t5 - start_t5) / num_tests
    print("The average time taken for the /api/dotproduct endpoint was {}".format(avg))
