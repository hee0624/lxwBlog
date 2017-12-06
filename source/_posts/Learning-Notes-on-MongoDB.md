---
title: Learning Notes on MongoDB
date: 2016-09-06 11:07:57
tags: [MongoDB, Database]
categories: [MongoDB, Database]
---

### 1.创建新用户
```bash
$ mongo 100.100.100.100:27017
> db.createUser(
{
    user: "user_name",
    pwd: "change_the_password",
    roles: [ { role: "read", db: "db1" }, { role: "read", db: "db2" }, { role: "read", db: "db3" }]
}
)
```
数据库帐号是跟着数据库来走的，哪里创建哪里认证：例如，在admin下创建的帐号，不能直接在其他库验证，只能在帐号创建库（admin）下认证，再去其他库进行操作。
[MongoDB 3.0 用户创建](https://www.cnblogs.com/zhoujinyi/p/4610050.html)

### 2.已存在用户增加新的数据库
```bash
> db.system.users.update({"_id": "admin.user_name"}, {$set: {"roles" : [ { "role" : "dbOwner", "db" : "db1" }, { "role" : "dbOwner", "db" : "db2" } ]}})
```
### 3.mongo创建索引
```bash
> db.news_steel.ensureIndex({"news_link": 1})
```