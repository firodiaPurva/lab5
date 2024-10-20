import grpc
# import the generated classes
import sum_pb2
import sum_pb2_grpc
from time import perf_counter
import sys

# Via CLI we pass in the address to the gRPC server including the port(50051)
addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])
img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

# open a gRPC channel
channel = grpc.insecure_channel(addr)

# add call
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

# image call
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

# raw image call
elif endpoint == 'rawimg':
    stub = sum_pb2_grpc.rawimgStub(channel)
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.rawimgMsg(img=img)
        resp = stub.rawimg(number)
        print(resp.image_size)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)

# JSON image call
elif endpoint == 'jsonimg':
    stub = sum_pb2_grpc.jsonimgStub(channel)
    # Pass the image data as bytes directly
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.jsonimgMsg(image_data=img)  # Use img directly as bytes
        resp = stub.jsonimg(number)
        print(resp.json_image_size)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)

# dot product call
elif endpoint == 'dotproduct':
    stub = sum_pb2_grpc.dotproductStub(channel)
    vectors = {
        'vector1': [1, 2, 3],
        'vector2': [4, 5, 6]
    }
    timer1_start = perf_counter()
    for i in range(num_tests):
        number = sum_pb2.dotproductMsg(vector1=vectors['vector1'], vector2=vectors['vector2'])
        resp = stub.dotproduct(number)
        print(resp.dot_product)
    timer1_stop = perf_counter()

    total = timer1_stop - timer1_start
    avg = total / num_tests
    print(avg)
