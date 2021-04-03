from grpc_tools import protoc


def run():
    command = [
            'grpc_tools.protoc',
            '--proto_path={}'.format(''),
            '--proto_path={}'.format('./protos'),
            '--python_out={}'.format('./pb'),
            '--grpc_python_out={}'.format('./pb'),
        ] + ['./protos/helloworld.proto']
    protoc.main(command)


if __name__ == '__main__':
    run()
