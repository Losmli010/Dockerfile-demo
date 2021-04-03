# 基础镜像
FROM nginx:1.16-alpine
# 时区
ENV TZ=Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 配置
COPY conf/nginx-dev.conf /etc/nginx/conf.d/default.conf
COPY html /usr/share/nginx/html