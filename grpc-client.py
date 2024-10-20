import grpc
import json
import numpy as np

# Import the generated classes
import sum_pb2
import sum_pb2_grpc
import struct
import sys
from time import perf_counter

# Via CLI we pass in the address to the gRPC server including the port(50051)
addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])
img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

# Open a gRPC channel
channel = grpc.insecure_channel(addr)

# Add call
if endpoint == 'add':
    stub = sum_pb2_grpc.addStub(channel)

    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.addMsg(a=5, b=4)
        resp = stub.add(number)
        print(resp.a)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)

# Image call
elif endpoint == 'image':
    stub = sum_pb2_grpc.imageStub(channel)
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.imageMsg(img=img)
        resp = stub.image(number)
        print(resp.a, resp.b)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)

# Raw image call
elif endpoint == 'rawimg':
    stub = sum_pb2_grpc.rawImageStub(channel)
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.rawImageMsg(img=img)
        resp = stub.rawimg(number)
        print(resp.image_size)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)

# JSON image call
elif endpoint == 'jsonimg':
    stub = sum_pb2_grpc.jsonImageStub(channel)
    img_array = list(np.frombuffer(img, dtype=np.uint8))
    image_data = {'image_data': img_array}
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.jsonImageMsg(img=json.dumps(image_data).encode('utf-8'))
        resp = stub.jsonimg(number)
        print(resp.json_image_size)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)

# Dot product call
elif endpoint == 'dotproduct':
    stub = sum_pb2_grpc.dotProductStub(channel)
    vectors = {
        'vector1': [1, 2, 3],
        'vector2': [4, 5, 6]
    }
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.dotProductMsg(vector1=vectors['vector1'], vector2=vectors['vector2'])
        resp = stub.dotproduct(number)
        print(resp.dot_product)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)
