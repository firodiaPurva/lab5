import grpc
from concurrent import futures
import time
from PIL import Image
import io
import json
import numpy as np

# Import the generated classes
import sum_pb2
import sum_pb2_grpc

class addServicer(sum_pb2_grpc.addServicer):
    def add(self, request, context):
        response = sum_pb2.addMsg()
        response.a = request.a + request.b
        return response

class imageServicer(sum_pb2_grpc.imageServicer):
    def image(self, request, context):
        response = sum_pb2.addMsg()
        ioBuffer = io.BytesIO(request.img)
        i = Image.open(ioBuffer)
        response.a = i.size[0]
        response.b = i.size[1]
        return response

class rawImageServicer(sum_pb2_grpc.rawImageServicer):
    def rawimg(self, request, context):
        response = sum_pb2.rawImageMsg()
        img_data = np.frombuffer(request.img, dtype=np.uint8)
        response.image_size = len(img_data)
        return response

class jsonImageServicer(sum_pb2_grpc.jsonImageServicer):
    def jsonimg(self, request, context):
        response = sum_pb2.jsonImageMsg()
        json_data = json.loads(request.img.decode('utf-8'))
        img_array = np.array(json_data['image_data'], dtype=np.uint8)
        response.json_image_size = img_array.size
        return response

class dotProductServicer(sum_pb2_grpc.dotProductServicer):
    def dotproduct(self, request, context):
        response = sum_pb2.dotProductMsg()
        vec1 = np.array(request.vector1)
        vec2 = np.array(request.vector2)
        dot_product = np.dot(vec1, vec2)
        response.dot_product = dot_product
        return response

# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

sum_pb2_grpc.add_addServicer_to_server(
    addServicer(), server)
sum_pb2_grpc.add_imageServicer_to_server(
    imageServicer(), server)
sum_pb2_grpc.add_rawImageServicer_to_server(
    rawImageServicer(), server)
sum_pb2_grpc.add_jsonImageServicer_to_server(
    jsonImageServicer(), server)
sum_pb2_grpc.add_dotProductServicer_to_server(
    dotProductServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# Since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
