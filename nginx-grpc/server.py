#!/usr/bin/env python
# -*-coding: utf-8 -*-
import logging
import time
from concurrent import futures

import grpc

from pb.helloworld_pb2_grpc import add_HelloWorldServiceServicer_to_server, HelloWorldServiceServicer
from pb.helloworld_pb2 import HelloRequest, HelloReply
from response.hello import reply


class Hello(HelloWorldServiceServicer):

    # 这里实现我们定义的接口
    def SayHello(self, request, context):
        res = reply(request)
        return HelloReply(message=res.get('message'))


def serve():
    # 这里通过thread pool来并发处理server的任务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 将对应的任务处理函数添加到rpc server中
    add_HelloWorldServiceServicer_to_server(Hello(), server)

    # 这里使用的非安全接口，世界gRPC支持TLS/SSL安全连接，以及各种鉴权机制
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
