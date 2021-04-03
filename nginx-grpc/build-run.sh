# 构建镜像
docker build -t grpc-helloworld:v1.0 .
# 运行容器
docker container run -d --name grpc-helloworld-v1 -v grpc-helloworld-volume:/app/log -p 50051:50051 grpc-helloworld:v1.0
