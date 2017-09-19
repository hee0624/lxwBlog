---
title: 'Learning Notes on RESTful API'
date: 2017-07-21 09:31:36
tags: [Architecture, RESTful API]
categories: [Architecture, RESTful API]
---

## 定义
REST -- REpresentational State Transfer  
首先，之所以晦涩是因为前面主语被去掉了，全称是 Resource Representational State Transfer.  
通俗来讲就是：资源在网络中以某种表现形式进行状态转移。分解开来：
Resource：资源，即数据（可以认为是网络的核心）。比如 newsfeed，friends等；  
Representational：某种表现形式，比如用JSON，XML，JPEG等；  
State Transfer：状态变化(通过HTTP动词实现)。  
REST的服务器是无状态的（stateless）

## RESTful API设计的Best Practice
1. URI使用名词而不是动词，且推荐用复数  
**BAD**:
/getProducts
/listOrders
/retrieveClientByOrder?orderId=1
**GOOD**:
GET /products : will return the list of all products  
POST /products : will add a product to the collection  
GET /products/4 : will retrieve product #4  
PATCH/PUT /products/4 : will update product #4  
2. 保证 HEAD 和 GET 方法是安全的，不会对资源状态有所改变（污染）。比如严格杜绝如下情况：
GET /deleteProduct?id=1
3. 在返回结果用明确易懂的文本（String。注意返回的错误是要给人看的，避免用 1001 这种错误信息），而且适当地加入注释。
4. 应该尽量将API部署在专用域名之下
```
https://api.example.com
```
如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下
```
https://example.org/api/
```
5. RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。
比如，当用户向api.example.com的根目录发出请求，会得到这样一个文档。
```json
{
  "link": {
    "rel":   "collection https://www.example.com/zoos",
    "href":  "https://api.example.com/zoos",
    "title": "List of zoos",
    "type":  "application/vnd.yourformat+json"
  }
}
```

## References
[怎样用通俗的语言解释REST，以及RESTful？]( https://www.zhihu.com/question/28557115)
[理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful.html)
[RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
