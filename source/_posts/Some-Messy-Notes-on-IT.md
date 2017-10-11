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
