---
title: Learning Notes on Docker
date: 2017-08-30 22:00:15
tags: Docker
categories: Docker
---

1.Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。
Docker 容器通过 Docker 镜像来创建。
容器与镜像的关系类似于面向对象编程中的对象与类。

| Docker | 面向对象 |
| --- | --- |
| 容器 | 对象 |
| 镜像 | 类 |
2.`docker run`命令来在容器内运行一个应用程序
```bash
$ docker run ubuntu:15.10 /bin/echo "Hello world"
```
各个参数解析：
+ docker: Docker 的二进制执行文件。
+ run:与前面的 docker 组合来运行一个容器。
+ ubuntu:15.10指定要运行的镜像，Docker首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
+ /bin/echo "Hello world": 在启动的容器里执行的命令

以上命令完整的意思可以解释为：Docker 以 ubuntu15.10 镜像创建一个新容器，然后在容器里执行 bin/echo "Hello world"，然后输出结果。
3.
`$ docker run -i -t ubuntu:15.10 /bin/bash`
各个参数解析：
+ -t:在新容器内指定一个伪终端或终端
+ -i:允许你对容器内的标准输入(STDIN)进行交互

```bash
$ docker run ubuntu:15.10 echo "hello world"
hello world
```
4.
```bash
$ docker run -d ubuntu:15.10 bash -c "while true; do echo hello world; sleep 1; done"    # 启动容器
04b096ad230216737573c08a162b426bb53f5b689972b04ef50ec22cdf616a2a
$ docker ps    # 查看运行的容器
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
04b096ad2302        ubuntu:15.10        "bash -c 'while true;"   6 seconds ago       Up 4 seconds                            evil_shirley
$ docker logs 04b096ad2302    # 查看容器内的标准输出(同样docker logs evil_shirley也可以)
hello world
hello world
...
hello world
$ docker stop 04b096ad2302    # 停止容器(同样docker stop evil_shirley也可以)
04b096ad2302
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
$ docker stats --help    # --help查看某个具体命令的用法
```
5.运行一个Web应用
```bash
$ docker run -d -P training/webapp python app.py
Unable to find image 'training/webapp:latest' locally
latest: Pulling from training/webapp

e190868d63f8: Pull complete
909cd34c6fd7: Pull complete
0b9bfabab7c1: Pull complete
a3ed95caeb02: Pull complete
10bbbc0fc0ff: Pull complete
fca59b508e9f: Pull complete
e7ae2541b15b: Pull complete
9dd97ef58ce9: Pull complete
a4c1b0cb7af7: Pull complete
Digest: sha256:06e9c1983bd6d5db5fba376ccd63bfa529e8d02f23d5079b8f74a616308fb11d
Status: Downloaded newer image for training/webapp:latest
d1a4c95dceb36103e440ef6a30d9bf66c3ba2fcc9ad87278bcff21ffeb67605e
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                     NAMES
d1a4c95dceb3        training/webapp     "python app.py"     About a minute ago   Up About a minute   0.0.0.0:32768->5000/tcp   angry_hodgkin
$ docker port angry_hodgkin    # 查看容器端口的映射情况
5000/tcp -> 0.0.0.0:32768
```
参数说明:
+ -d:让容器在后台运行
+ -P:将容器内部使用的网络端口映射到我们使用的主机上
+ -p:是容器内部端口绑定到指定的主机端口。(`docker run -d -p 5000:5000 training/webapp python app.py`)

Docker 开放了 5000 端口（默认 Python Flask 端口）映射到主机端口 32768 上, 这时我们可以通过浏览器访问WEB应用
6.
```bash
$ docker logs -f angry_hodgkin
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
192.168.1.41 - - [30/Aug/2017 14:45:26] "GET / HTTP/1.1" 200 -
192.168.1.41 - - [30/Aug/2017 14:45:26] "GET /favicon.ico HTTP/1.1" 404 -
192.168.1.41 - - [30/Aug/2017 14:48:20] "GET / HTTP/1.1" 200 -
192.168.1.41 - - [30/Aug/2017 14:48:23] "GET / HTTP/1.1" 200 -
```
-f: 让 dokcer logs 像使用 tail -f 一样来输出容器内部的标准输出。
7.
```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
d1a4c95dceb3        training/webapp     "python app.py"     6 minutes ago       Up 6 minutes        0.0.0.0:32768->5000/tcp   angry_hodgkin
$ docker stop d1a4c95dceb3
d1a4c95dceb3
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
$ docker start d1a4c95dceb3
d1a4c95dceb3
(py2712askbot) lxw@lxw askbot-devel on git:master o [22:50:16]
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
d1a4c95dceb3        training/webapp     "python app.py"     7 minutes ago       Up 8 seconds        0.0.0.0:32769->5000/tcp   angry_hodgkin
```
docker ps -l 查询最后一次创建的容器
8.
```bash
$ docker rm angry_hodgkin    # 删除容器时，容器必须是停止状态，否则会报如下错误
Error response from daemon: You cannot remove a running container d1a4c95dceb36103e440ef6a30d9bf66c3ba2fcc9ad87278bcff21ffeb67605e. Stop the container before attempting removal or use -f
$ docker stop angry_hodgkin
angry_hodgkin
$ docker rm angry_hodgkin
angry_hodgkin
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
$ docker rmi <image id>    # 删除images，通过image的id来指定删除谁
```
9.使用 docker images 来列出本地主机上的镜像。
```bash
$ docker images
REPOSITORY           TAG                  IMAGE ID            CREATED             SIZE
scrapinghub/portia   latest               b505e2ff0a71        5 months ago        756.5 MB
centos               monitor_standalone   dcf18899ee16        8 months ago        950.9 MB
ubuntu               15.10                9b9cb95443b5        13 months ago       137.2 MB
hello-world          latest               c54a2cc56cbb        14 months ago       1.848 kB
training/webapp      latest               6fae60ef3446        2 years ago         348.8 MB
```
各个选项说明:
+ REPOSTITORY：表示镜像的仓库源
+ TAG：镜像的标签
+ IMAGE ID：镜像ID
+ CREATED：镜像创建时间
+ SIZE：镜像大小

同一仓库源可以有多个 TAG，代表这个仓库源的不同个版本，如ubuntu仓库源里，有15.10、14.04等多个不同的版本，我们使用 REPOSTITORY:TAG 来定义不同的镜像(如ubuntu:15.10)。
如果不指定一个镜像的版本标签，例如只使用ubuntu，docker 将默认使用 ubuntu:latest 镜像。
10.
1)想下载某个镜像，可以使用docker pull命令
```bash
$ docker pull ubuntu:16.04
```
2)使用 docker search 命令来搜索镜像
```bash
$ docker search httpd
```
11.当我们从docker镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改:
 + 1) 从已经创建的容器中更新镜像，并且提交这个镜像
 + 2) 使用 Dockerfile 指令来创建一个新的镜像

 **1)更新镜像**
 运行容器，并进行系统更新
 ```bash
 $ docker run -t -i ubuntu:15.10 /bin/bash
 root@26c5edd45e9b:/# apt-get update
 root@26c5edd45e9b:/# exit
 exit
 $ docker images
 REPOSITORY           TAG                  IMAGE ID            CREATED             SIZE
 ubuntu               16.04                ccc7a11d65b1        2 weeks ago         120.1 MB
 scrapinghub/portia   latest               b505e2ff0a71        5 months ago        756.5 MB
 centos               monitor_standalone   dcf18899ee16        8 months ago        950.9 MB
 ubuntu               15.10                9b9cb95443b5        13 months ago       137.2 MB
 hello-world          latest               c54a2cc56cbb        14 months ago       1.848 kB
 training/webapp      latest               6fae60ef3446        2 years ago         348.8 MB
 $ docker commit -m="apt-get update" -a="xiaoweiliu" 26c5edd45e9b lxw/ubuntu1510
 sha256:e9d03b3bcea583a14a23dade498cc930f4dd297104743544c4f234fb2c22f380
 $ docker images
 REPOSITORY           TAG                  IMAGE ID            CREATED              SIZE
 lxw/ubuntu1510       latest               e9d03b3bcea5        22 seconds ago       159.4 MB
 ubuntu               16.04                ccc7a11d65b1        2 weeks ago          120.1 MB
 scrapinghub/portia   latest               b505e2ff0a71        5 months ago         756.5 MB
 centos               monitor_standalone   dcf18899ee16        8 months ago         950.9 MB
 ubuntu               15.10                9b9cb95443b5        13 months ago        137.2 MB
 hello-world          latest               c54a2cc56cbb        14 months ago        1.848 kB
 training/webapp      latest               6fae60ef3446        2 years ago          348.8 MB
 ```
 各个参数说明：
 + -m:提交的描述信息
 + -a:指定镜像作者
 + 26c5edd45e9b：容器ID

 lxw/ubuntu1510:指定要创建的目标镜像名

 **2)构建镜像**
 使用命令 docker build，从零开始来创建一个新的镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建镜像。
 ```bash
 $ cat Dockerfile
 FROM    centos:6.7
 MAINTAINER      Fisher "fisher@sudops.com"

 RUN     /bin/echo 'root:lxw' |chpasswd
 RUN     useradd lxw
 RUN     /bin/echo 'lxw:lxw' |chpasswd
 RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
 EXPOSE  22
 EXPOSE  80
 CMD     /usr/sbin/sshd -D
 $ docker build -t lxw/centos:6.7 $(pwd)
 ...
 $ docker images
 REPOSITORY           TAG                  IMAGE ID            CREATED             SIZE
 lxw/centos           6.7                  97b1b8d9e2e1        2 minutes ago       190.6 MB
 ...
 ```
 每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。
 第一条FROM，指定使用哪个镜像源
 RUN 指令告诉docker 在镜像内执行命令，安装了什么
 然后使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像
 参数说明：
 + -t： 指定要创建的目标镜像名
 + $(pwd)： Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径
 ```bash
 $ docker run -t -i lxw/centos:6.7 /bin/bash
 [root@b3c42f1fd599 /]# id lxw
 uid=500(lxw) gid=500(lxw) groups=500(lxw)
 ```


### References:
[Docker教程](http://www.runoob.com/docker/docker-tutorial.html)
