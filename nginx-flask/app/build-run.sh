# 构建镜像
docker build -f Dockerfile.uwsgi -t flask-uwsgi:v1.0 .
# 运行
docker container run -d --name flask-uwsgi-v1 -p 8008:8008 flask-uwsgi:v1.0