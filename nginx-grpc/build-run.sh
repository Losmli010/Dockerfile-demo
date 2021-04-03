# 构建镜像
docker build -t nginx-html:v1.0 .
# 运行容器
docker container run -d --name docker-nginx-v1 -v nginx-volume:/var/log/nginx -p 8080:80 nginx-html:v1.0

# 更新网页信息，升级镜像
docker build -t nginx-html:v1.0 .
# 运行容器
docker container run -d --name docker-nginx-v2 -v nginx-volume:/var/log/nginx -p 8080:80 nginx-html:v1.0