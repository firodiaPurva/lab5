import grpc
from concurrent import futures
import time
from PIL import Image
import io

# import the generated classes
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

class rawimgServicer(sum_pb2_grpc.rawimgServicer):
    def rawimg(self, request, context):
        response = sum_pb2.rawimgMsg()
        img_data = io.BytesIO(request.img)
        response.image_size = len(img_data.getvalue())
        return response

class jsonimgServicer(sum_pb2_grpc.jsonimgServicer):
    def jsonimg(self, request, context):
        response = sum_pb2.jsonimgMsg()
        img_array = request.image_data
        response.json_image_size = len(img_array)
        return response

class dotproductServicer(sum_pb2_grpc.dotproductServicer):
    def dotproduct(self, request, context):
        response = sum_pb2.dotproductMsg()
        vec1 = request.vector1
        vec2 = request.vector2
        response.dot_product = sum(x * y for x, y in zip(vec1, vec2))
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

sum_pb2_grpc.add_addServicer_to_server(addServicer(), server)
sum_pb2_grpc.add_imageServicer_to_server(imageServicer(), server)
sum_pb2_grpc.add_rawimgServicer_to_server(rawimgServicer(), server)
sum_pb2_grpc.add_jsonimgServicer_to_server(jsonimgServicer(), server)
sum_pb2_grpc.add_dotproductServicer_to_server(dotproductServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
