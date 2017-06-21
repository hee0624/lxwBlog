---
title: 'pymongo.errors.DuplicateKeyError: E11000 duplicate key error'
date: 2017-06-21 14:45:04
tags: [Python, MongoDB]
categories: [Python, MongoDB]
---

&emsp;&emsp;最近在写[裁判文书网的爬虫代码](https://github.com/hee0624/fintech_spider/tree/master/Spiders/CJOSpider)，最开始的版本是使用Scrapy写的，爬取了120万条案例数据之后，网站改版了：反爬虫机制得到升级，必须使用Cookie和IP代理来进行爬取，否则无法爬取到所需要的数据，因此对爬虫代码进行了重构，并总结在[这里](http://xiaoweiliu.cn/2017/06/03/%E4%B8%AD%E5%9B%BD%E8%A3%81%E5%88%A4%E6%96%87%E4%B9%A6%E7%BD%91-China-Judgements-Online-%E6%95%B0%E6%8D%AE%E7%88%AC%E5%8F%96%E6%80%BB%E7%BB%93-%E6%8A%93%E5%8F%96%E6%80%9D%E8%B7%AF-%E6%9E%B6%E6%9E%84%E4%BC%98%E5%8C%96/)。
&emsp;&emsp;在重构时不再使用Scrapy（使用multiprocessing的进程池，并沿用Redis完成代码的重构）：因为在写第一版时发现使用Scrapy有很多不可控的地方（可能是我对Scrapy了解的还太浅），例如：请求何时才会被Scheduler发送到Engine进而发送到Middleware真正发起请求，也就是请求在请求队列中等待的时间是不确定的；此外，使用Scrapy时所有的请求都放到Redis中，为了区分各种情况（请求成功，请求失败，失败重试的次数，上次请求的时间戳等），需要对Redis中的值增加多个标志位，很是繁琐和复杂。重构后的代码在[这里](https://github.com/hee0624/fintech_spider/blob/master/Spiders/CJOSpider/CJOSpider_wo_scrapy_new.py)。
&emsp;&emsp;本篇文章是重构完成后，进行爬取时，发现错误日志中有这样的信息`'pymongo.errors.DuplicateKeyError: E11000 duplicate key error collection: *.* index: _id_ dup key: { : ObjectId('*') }'`。刚开始以为是因为使用了`multiprocessing`导致的，后来在网上查阅后，发现与`pymongo`的工作方式有关，个人感觉通过`pymongo`操作`MongoDB`数据库时非常容易犯这样的错误，因此形成了这篇文章，并做一个总结。
&emsp;&emsp;问题的解决方案有三种，可以参见[StackOverflow上给出的解决方案](https://stackoverflow.com/questions/21119928/getting-err-e11000-duplicate-key-error-when-inserting-into-mongo-using-the)。我对这三种解决方案分别写了几段代码进行测试，证明可行。总结起来，出现问题的原因如下：
> The problem is that PyMongo injects an `_id` field into the document, if the `_id` field does not exist, before inserting it (_id is always generated client side with 10gen drivers). **That means that the first time through the loop _id is added by the insert method. Since doc is defined outside the loop, each subsequent pass through the loop uses the same value for _id.**

### 问题重现
&emsp;&emsp;在给出三种解决方案的代码前，先通过如下代码重现该问题：  
```python
import pymongo

class WriteIntoMongoTest:
    def into_mongo(self, db, data_dict):
        print(data_dict)
        print(len(data_dict))    # Not 2, but 3.
        db["test_write"].insert(data_dict)
        print(data_dict)    # NOTE: the key "_id" is added into data_dict automatically here.
        print(len(data_dict))    # Not 2, but 3.

    def write_into_mongo(self):
        # pymongo.errors.DuplicateKeyError: E11000 duplicate key error collection: scrapy.test_write index: _id_ dup key: { : ObjectId('5949e2812759391e00ab43df')
        conn = pymongo.MongoClient("192.168.1.41", 27017)
        db = conn.scrapy    # dbname: scrapy
        result_dict = {}
        for i in range(10):
            result_dict["key1"] = str(i)
            result_dict["key2"] = str(i)
            self.into_mongo(db, result_dict)

if __name__ == "__main__":
    twim = WriteIntoMongoTest()
    twim.write_into_mongo(
```
&emsp;&emsp;运行结果是只能成功插入一条，后面的数据插入报错，程序退出了。运行上述代码后`MongoDB`中的数据如下：
```bash
> db.test_write.count()
1
> db.test_write.find()
{ "_id" : ObjectId("594a22a127593904723a970a"), "key1" : "0", "key2" : "0" }
```
### 三种解决方案
##### 解决方案1
&emsp;&emsp;把`result_dict = {}`从for循环外面拿到for循环里面，代码如下：  
```python
import pymongo

class WriteIntoMongoTest:
    def into_mongo(self, db, data_dict):
        print(data_dict)
        print(len(data_dict))    # Not 2, but 3.
        db["test_write"].insert(data_dict)
        print(data_dict)    # NOTE: the key "_id" is added into data_dict automatically here.
        print(len(data_dict))    # Not 2, but 3.

    def write_into_mongo(self):
        # OK: method 1.
        conn = pymongo.MongoClient("192.168.1.41", 27017)
        db = conn.scrapy    # dbname: scrapy
        for i in range(10):
            result_dict = {}    # NOTE HERE
            result_dict["key1"] = str(i)
            result_dict["key2"] = str(i)
            self.into_mongo(db, result_dict)

if __name__ == "__main__":
    twim = WriteIntoMongoTest()
    twim.write_into_mongo()
```
&emsp;&emsp;运行上述代码后，数据全部插入成功，`MongoDB`中的数据如下：  
```bash
> db.test_write.drop()
true
> db.test_write.count()
0
> db.test_write.count()		# 执行代码后，执行该命令
10
> db.test_write.find()
{ "_id" : ObjectId("594a250827593907bab68aeb"), "key1" : "0", "key2" : "0" }
{ "_id" : ObjectId("594a250827593907bab68aec"), "key1" : "1", "key2" : "1" }
{ "_id" : ObjectId("594a250827593907bab68aed"), "key1" : "2", "key2" : "2" }
{ "_id" : ObjectId("594a250827593907bab68aee"), "key1" : "3", "key2" : "3" }
{ "_id" : ObjectId("594a250827593907bab68aef"), "key1" : "4", "key2" : "4" }
{ "_id" : ObjectId("594a250827593907bab68af0"), "key1" : "5", "key2" : "5" }
{ "_id" : ObjectId("594a250827593907bab68af1"), "key1" : "6", "key2" : "6" }
{ "_id" : ObjectId("594a250827593907bab68af2"), "key1" : "7", "key2" : "7" }
{ "_id" : ObjectId("594a250827593907bab68af3"), "key1" : "8", "key2" : "8" }
{ "_id" : ObjectId("594a250827593907bab68af4"), "key1" : "9", "key2" : "9" }
```

##### 解决方案2
&emsp;&emsp;原理上与解决方案1相同，判断`result_dict`中是否已经存在`_id`键，如果存在将其删除，代码如下：  
```python
import pymongo

class WriteIntoMongoTest:
    def into_mongo(self, db, data_dict):
        print(data_dict)
        print(len(data_dict))    # Not 2, but 3.
        db["test_write"].insert(data_dict)
        print(data_dict)    # NOTE: the key "_id" is added into data_dict automatically here.
        print(len(data_dict))    # Not 2, but 3.

    def write_into_mongo(self):
        # OK: method 2.
        conn = pymongo.MongoClient("192.168.1.41", 27017)
        db = conn.scrapy    # dbname: scrapy
        result_dict = {}
        for i in range(10):
            if "_id" in result_dict:
                print("_id in result_dict")
                del result_dict["_id"]    # NOTE HERE
            result_dict["key1"] = str(i)
            result_dict["key2"] = str(i)
            self.into_mongo(db, result_dict)

if __name__ == "__main__":
    twim = WriteIntoMongoTest()
    twim.write_into_mongo()
```
&emsp;&emsp;代码运行结果与解决方案1相同，此处略。  
##### 解决方案3
&emsp;&emsp;原理上与解决方案1相同，在`result_dict`中使用自定义的`_id`键，代码如下：  
```python
import pymongo
from bson.objectid import ObjectId

class WriteIntoMongoTest:
    def into_mongo(self, db, data_dict):
        print(data_dict)
        print(len(data_dict))    # Not 2, but 3.
        db["test_write"].insert(data_dict)
        print(data_dict)    # NOTE: the key "_id" is added into data_dict automatically here.
        print(len(data_dict))    # Not 2, but 3.

    def write_into_mongo(self):
        # OK: method 3.
        conn = pymongo.MongoClient("192.168.1.41", 27017)
        db = conn.scrapy    # dbname: scrapy
        result_dict = {}
        for i in range(10):
            result_dict["_id"] = ObjectId()    # NOTE HERE
            result_dict["key1"] = str(i)
            result_dict["key2"] = str(i)
            self.into_mongo(db, result_dict)

if __name__ == "__main__":
    twim = WriteIntoMongoTest()
    twim.write_into_mongo()
```
&emsp;&emsp;代码运行结果与解决方案1相同，此处略。  

本文完。
