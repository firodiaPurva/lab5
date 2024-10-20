#!/usr/bin/env python3
import requests
import json
import sys
from time import perf_counter

addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])

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

# Add endpoint
if endpoint == 'add':
    start_time = perf_counter()
    for _ in range(num_tests):
        resp = requests.get(add_url)
        print(resp.text)
    total_time = (perf_counter() - start_time) / num_tests
    print(f"Average time for add: {total_time}")

# Image endpoint
elif endpoint == 'image':
    start_time = perf_counter()
    for _ in range(num_tests):
        resp = requests.post(image_url, data=img)
        print(resp.text)
    total_time = (perf_counter() - start_time) / num_tests
    print(f"Average time for image: {total_time}")

# Raw image endpoint
elif endpoint == 'rawimg':
    start_time = perf_counter()
    for _ in range(num_tests):
        resp = requests.post(rawimg_url, data=img)
        print(resp.text)
    total_time = (perf_counter() - start_time) / num_tests
    print(f"Average time for rawimg: {total_time}")

# JSON image endpoint
elif endpoint == 'jsonimg':
    image_data = {'image_data': list(img)}
    start_time = perf_counter()
    for _ in range(num_tests):
        resp = requests.post(jsonimg_url, data=json.dumps(image_data), headers=headers)
        print(resp.text)
    total_time = (perf_counter() - start_time) / num_tests
    print(f"Average time for jsonimg: {total_time}")

# Dot product endpoint
elif endpoint == 'dotproduct':
    vectors = {
        'vector1': [1, 2, 3],
        'vector2': [4, 5, 6]
    }
    start_time = perf_counter()
    for _ in range(num_tests):
        resp = requests.post(dotproduct_url, data=json.dumps(vectors), headers=headers)
        print(resp.text)
    total_time = (perf_counter() - start_time) / num_tests
    print(f"Average time for dotproduct: {total_time}")
