---
title: Learning Notes on ElasticSearch
date: 2017-07-19 14:03:29
tags: ElasticSearch
categories: ElasticSearch
---
## "ELK Stack深入浅出视频"总结
1. [01] 11'43"
索引的名字必须是小写
2. ![](./mysql_vs_ES.png)
3. Solr支持的文本格式比ES多, 但ES的实时搜索比Solr好
4. mapping映射: 创建索引时,可以预先定义字段的**类型**以及**相关属性**
5. [11] 19'52"
尽可能使用filter查询（减少使用基本查询），能够大大提高查询的性能
ElasticSearch在执行带有filter的查询时，会打开索引的每个segment文件（Lucene底层文件），然后判断各文档是否符合filter要求。
注意：
 + 1).旧的segment文件不会变，新来的数据会产生新的segment文件。
 + 2).Scriptfilters, Geo-filters, Date ranges这样的过滤方式开启cache无意义； exists, missing, range, term, terms查询默认是开启cache的。

6. must: 条件必须满足，相当于and
   should: 条件可以满足也可以不满足，相当于or
   must_not: 条件不需要满足， 相当于not

## "[Elasticsearch: 权威指南](https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html)"总结
1. 一个集群是一组拥有相同cluster.name的节点，他们能一起工作并共享数据，还提供容错与可伸缩性。
2. 你也许已经注意到 索引 这个词在 Elasticsearch 语境中包含多重意思， 所以有必要做一点说明：
 + 索引（名词）：
  如前所述，一个 索引 类似于传统关系数据库中的一个 数据库 ，是一个存储关系型文档的地方。 索引 (index) 的复数词为 indices 或 indexes。
 + 索引（动词）：
  索引一个文档 就是存储一个文档到一个 索引 （名词）中以便它可以被检索和查询到。这非常类似于 SQL 语句中的 INSERT 关键词，除了文档已存在时新文档会替换旧文档情况之外
3. 
```json
PUT /es_demo/employee/1
{
    "first_name" : "John",
    "last_name" :  "Smith",
    "age" :        25,
    "about" :      "I love to go rock climbing",
    "interests": [ "sports", "music" ]
}
```
路径 /es_demo/employee/1 包含了三部分的信息：
es_demo: 索引名称
emp	loyee: 类型名称
1: 特定雇员的ID

4. 有两种形式的 搜索 API：一种是"轻量的"**查询字符串** 版本，要求在查询字符串中传递所有的 参数，另一种是更完整的 **请求体** 版本，要求使用 JSON 格式和更丰富的查询表达式作为搜索语言。
查询字符串版本优点就是简洁，但可读性差（url编码后），并且这种精简让调试更加晦涩和困难。而且很脆弱，一些查询字符串中很小的语法错误，像 -，:，/或者" 不匹配等，将会返回错误而不是搜索结果。查询字符串搜索允许任何用户在索引的任意字段上执行可能较慢且重量级的查询，这可能会暴露隐私信息，甚至将集群拖垮。**因为这些原因，不推荐直接向用户暴露查询字符串搜索功能，除非对于集群和数据来说非常信任他们。**在生产环境中更多地使用功能全面的请求体版本查询API，除了能完成以上所有功能，还有一些附加功能。
[轻量搜索](https://www.elastic.co/guide/cn/elasticsearch/guide/current/search-lite.html) GET all employees whose last_name **is** "Smith"(精确匹配)
```json
GET /es_demo/employee/_search?q=last_name:Smith
```
领域特定语言（DSL），指定了使用一个 JSON 请求。可以像如下代码重写上述查询：
```json
GET /es_demo/employee/_search
{
  "query":{
    "match":{
      "first_name": "Smith"
    }
  }
}
```
5. 

## FAQs
1. [Elasticsearch5.0 安装问题集锦](http://www.cnblogs.com/sloveling/p/elasticsearch.html)
2. [Elasticsearch 5.2.x 使用 Head 插件连接不上集群](http://www.cnblogs.com/zklidd/p/6433123.html)
3. [BindTransportException[Failed to bind to [9300-9400]]](https://discuss.elastic.co/t/bindtransportexception-failed-to-bind-to-9300-9400/65443)
