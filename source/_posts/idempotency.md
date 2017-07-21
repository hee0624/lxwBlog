---
title: 幂等性
date: 2016-12-10 18:18:18
tags: Network
categories: Network
---
### 定义
数学式的定义`f(f(x)) = f(x)`. 即x被函数f作用一次和作用无限次的结果是一样的. 幂等性应用在软件系统中可以理解为, 某个函数或接口使用相同参数调用一次或者无限次, 其产生的副作用是一样的. 在实际应用中一般针对于接口进行幂等性设计, 例如在系统中, 用户U调用系统的接口I进行扣费操作时, 由于网络不稳定, U重试了多次该请求, 那么无论接口I接收到多少次请求, 都应保证只会扣除该用户一次费用.

### TCP协议的幂等性
幂等性一般应用于协议设计, TCP协议支持幂等性. 在网络不稳定时, 操作系统可以肆无忌惮的重发TCP报文片段. TCP协议能够保证幂等性的关键在于[`Sequence number`](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)字段, 序列号的在较长时间内不会出现重复的情况. 对于应用层的协议设计, 原理与TCP协议类似, 我们需要一个不重复的序列号. 更广泛地说, 在一个业务流程的处理中, 我们需要一个不重复的业务流水号, 以保证幂等性.

### HTTP的幂等性
GET, DELETE, PUT是满足幂等性的, POST是不满足幂等性的
POST和PUT的区别: POST和PUT都可以用于创建资源, 多次POST会创建多个资源, 但多次PUT不会创建多个资源, 只会创建一个资源, 后面的PUT请求视为对所创建资源的更新操作.

常用的HTTP动词有下面五个（括号里是对应的SQL命令）:
GET（SELECT）：从服务器取出资源（一项或多项）
POST（CREATE）：在服务器新建一个资源（也可以用于更新资源）
PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）
PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）
DELETE（DELETE）：从服务器删除资源
还有两个不常用的HTTP动词:
HEAD：获取资源的元数据
OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的

### Reference
[理解HTTP幂等性](http://www.cnblogs.com/weidagang2046/archive/2011/06/04/2063696.html)   
[基础篇(一) 幂等性](http://blog.csdn.net/tjgamejx2/article/details/51011425)
[RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
