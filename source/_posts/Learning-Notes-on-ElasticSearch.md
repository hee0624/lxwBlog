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
2. 


## FAQs
1. [Elasticsearch5.0 安装问题集锦](http://www.cnblogs.com/sloveling/p/elasticsearch.html)
2. [Elasticsearch 5.2.x 使用 Head 插件连接不上集群](http://www.cnblogs.com/zklidd/p/6433123.html)
3. [BindTransportException[Failed to bind to [9300-9400]]](https://discuss.elastic.co/t/bindtransportexception-failed-to-bind-to-9300-9400/65443)
