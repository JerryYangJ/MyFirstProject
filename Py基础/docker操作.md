###1. 查看Docker版本  
docker version  
它用于查看Docker的客户端和服务器版本。如下图所示。
###2. 从Docker文件构建Docker映像
docker build -t image-name docker-file-location  
-t：它用于指定使用提供的名称来标记Docker映像。
###3. 运行Docker映像
docker run -d image-name  
如：  
docker run  -d --name nginx  -p 80:80   
-v /home/jerry123/docker/nginx/nginx.conf:/etc/nginx/nginx.conf  
-v /home/jerry123/docker/nginx/html:/usr/share/nginx/html  
-v /home/jerry123/docker/nginx/conf.d/default.conf:/etc/nginx/conf.d/default.conf nginx  
-d：用于创建守护程序进程。  
-p: 端口映射  
-v: 挂载目录
--name: 容器名称
###4. 查看可用的Docker映像  
docker images  
###5. 查看最近的运行容器
docker ps -l  
-l：它用于显示最新的可用容器。
###6. 查看所有正在运行的容器
docker ps -a  
-a：它用于显示所有可用的容器。
###7. 停止运行容器
docker stop container_id  
container_id：由Docker分配给容器的Id。
###8. 删除一个映像
docker rmi image-name  
###9. 删除所有映像
docker rmi $(docker images -q)  
###10. 强制删除所有映像
docker rmi -r $(docker images -q)  
-r：用于强制删除映像。
###11. 删除所有容器
docker rm $(docker ps -a -q)  
###12. 进入Docker容器
docker exec -it container-id bash
###13.查看容器状态
docker stats -a  
-a:显示所有容器  
###14.从容器中复制文件到宿主机(需要启动容器）：
docker cp 容器名称:文件path 目标path
###15.重新启动容器  
docker restart [options] container

