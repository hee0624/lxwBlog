---
title: Shadowsocks-服务器&客户端配置
date: 2017-10-25 10:13:00
tags: [Ubuntu, Network]
categories: [Ubuntu, Network]
---
## 服务器配置
&emsp;&emsp;1.使购买境外服务器, 这里选用的是[VIRMACH](https://billing.virmach.com/cart.php?gid=1) 因为穷,所以买便宜的.
&emsp;&emsp;2.登录服务器并更改密码: `ssh@ip`
&emsp;&emsp;3.配置服务端:
```bash
$ wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
$ chmod +x shadowsocks.sh
$ ./shadowsocks.sh 2>&1 | tee shadowsocks.log    # 配置密码、协议等（建议选择7：aes-256-cfb）
$ vim /etc/shadowsocks.json    # "server"为服务器ip
$ ssserver -c /etc/shadowsocks.json -d restart    # 重启服务
```
## 客户端配置
&emsp;&emsp;使用[shadowsocks/shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows)在Windows的配置Shadowsocks的客户端是很简单的，但在Ubuntu上只找到了[shadowsocks/shadowsocks-qt5](https://github.com/shadowsocks/shadowsocks-qt5)，感觉比shadowsocks/shadowsocks-windows稍微麻烦一点(shadowsocks-qt5的优势是跨平台)。这里对如何在Ubuntu和优麒麟中配置Shadowsocks-Qt5客户端做个简单的总结。
### Ubuntu16.04上的安装和使用
&emsp;&emsp;按照[shadowsocks-qt5安装指南](https://github.com/shadowsocks/shadowsocks-qt5/wiki/安装指南)的操作安装shadowsocks-qt5客户端：
```bash
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```
&emsp;&emsp;按下super键（windows键）搜索shadowsocks应用，并执行。
### 优麒麟16.10上的安装和使用
&emsp;&emsp;在同学的Ubuntu优麒麟上尝试上面的方法，在`sudo add-apt-repositorG ppa:hzwhuang/ss-qt5`这一步就会出现问题。  
&emsp;&emsp;可以尝试修复上面的问题（应该是需要手动编译shadowsocks包），或者使用下面的方法（参考自[shadowsocks-qt5 Installation](https://github.com/shadowsocks/shadowsocks-qt5/wiki/Installation)）
```bash
chmod a+x Shadowsocks-Qt5-x86_64.AppImage
./Shadowsocks-Qt5-x86_64.AppImage
```
&emsp;&emsp;在shadowsocks中配置相应的服务器、端口、密码、加密方式（可以参考下图的配置）后，选择"连接（Connect）"，此时打开https://www.google.com/或http://www.youtube.com/进行测试，此时应该是无法打开这些网站的。  
![./ss_qt5_client_configuration.png](./ss_qt5_client_configuration.png)  
&emsp;&emsp;还需要配置本地的代理，有两种方法（参考自[不支持Ubuntu17.04](https://github.com/shadowsocks/shadowsocks-qt5/issues/490)）： 
 1. 【不推荐】在Ubuntu系统中打开System Settings->Netowork->Network proxy, 选择Manual, 参考下图的配置进行修改后，选择Apply system wide。此时再打开https://www.google.com/或http://www.youtube.com/就可以上网了。  
 ![./ubuntu_network_configuration.png](./ubuntu_network_configuration.png)  
 2. 【推荐】第二种方法是使用浏览器的插件，这里以Chrome/Chromium的Switchysharp插件为例进行说明（可以参考下图的配置，其实和方法1中的设置是一样的）。  
 ![./switchysharp_configuration.png](./switchysharp_configuration.png)  
 这样在需要科学上网时，只需要切换到相应的代理模式即可。

### 其他客户端配置
1. Iphone: 去加拿大的applestore下载wingy。(配置ip、协议、密码)
2. Android: https://github.com/shadowsocks/shadowsocks-android/releases/download/v4.2.5/shadowsocks-nightly-4.2.5.apk (配置ip、协议、密码)
