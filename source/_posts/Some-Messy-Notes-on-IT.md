---
title: Some Messy Notes on IT
date: 2017-09-13 10:10:10
tags: [IT]
categories: [IT]
---

1.
消息队列应用场景:
异步处理（注册服务中短信/邮件发送）
应用解耦（订单系统与库存系统中发布与订阅）
流量削锋（抢购活动）
日志处理（如典型的kafka消息队列）
消息通讯（消息队列的两种消息模式，点对点或发布订阅模式）
[Reference](http://blog.csdn.net/shaobingj126/article/details/50585035)

2.
ActiveMQ currently outperforms RabbitMQ for messaging usage in Python.
[PYTHON MESSAGING: ACTIVEMQ AND RABBITMQ](http://sensatic.net/activemq/python-messaging-activemq-and-rabbitmq.html)

3.
[几种进程间的通信方式](http://www.cnblogs.com/mydomain/archive/2010/09/23/1833369.html):
+ 管道(pipe): 管道是一种半双工的通信方式，数据只能单向流动，而且**只能在具有亲缘关系的进程间使用**。进程的亲缘关系通常是指父子进程关系。
+ 命名管道(named pipe): 命名管道也是半双工的通信方式，但它**允许无亲缘关系进程间的通信**。
+ 信号量(semaphore): 信号量是一个计数器，可以用来控制多个进程对共享资源的访问。**它常作为一种锁机制**，防止某进程正在访问共享资源时，其他进程也访问该资源。因此，主要作为进程间以及同一进程内不同线程之间的同步手段。
+ 消息队列(message queue): 消息队列是一种存储消息的数据结构，存放在内存中并由消息队列标识符标识。**消息队列克服了信号传递信息少、管道只能承载无格式字节流以及缓冲区大小受限等缺点**。
+ 信号(sinal): 信号是一种比较复杂的通信方式，用于通知接收进程某个事件已经发生。
+ 共享内存(shared memory): 共享内存就是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创建，但多个进程都可以访问。**共享内存是最快的IPC方式，它是针对其他进程间通信方式运行效率低而专门设计的**。**它往往与其他通信机制(如信号量)配合使用，来实现进程间的同步和通信**。
+ 套接字(socket): 套解字也是一种进程间通信机制，与其他通信机制不同的是，它可用于不同机器间的进程通信。

4.
[CGI, FastCGI, WSGI, uWSGI, uwsgi简述](https://www.cnblogs.com/wswang/p/6044978.html)  
**CGI**  
通用网关接口（Common Gateway Interface/CGI）是一种重要的互联网技术，可以让一个客户端，从网页浏览器向执行在网络服务器上的程序请求数据。CGI描述了服务器和请求处理程序之间传输数据的一种标准。  
CGI程序可以用任何脚本语言或者是完全独立编程语言实现，只要这个语言可以在这个系统上运行。  
**一句话总结： 一个标准，定义了客户端服务器之间如何传数据**  

**FastCGI**  
快速通用网关接口（Fast Common Gateway Interface／FastCGI）是一种让交互程序与Web服务器通信的协议。FastCGI是早期通用网关接口（CGI）的增强版本。  
FastCGI致力于减少网页服务器与CGI程序之间互动的开销，从而使服务器可以同时处理更多的网页请求。  
使用FastCGI的服务器： Apache HTTP Server (部分), Cherokee HTTP Server, Hiawatha Webserver, Lighttpd, Nginx, LiteSpeed Web Server, Microsoft IIS  
**一句话总结： CGI的升级版**  

**WSGI**  
Web服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。  
**一句话总结： 为Python定义的web服务器和web框架之间的接口标准，如Apache和Django这种东西（虽然很少有人这么用）**  

**uWSGI**  
**一句话总结： 一个Web Server，即一个实现了WSGI的服务器，大体和Apache是一个类型的东西，处理发来的请求。**

**uwsgi**  
**一句话总结： uWSGI自有的一个协议**  

这篇文章[CGI FastCGI WSGI 学习笔记](https://blog.callmewhy.com/2015/12/07/what-is-wsgi-and-cgi/)比较详细，比较清楚，推荐看。
