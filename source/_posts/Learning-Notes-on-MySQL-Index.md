---
title: Learning Notes on MySQL INDEX
date: 2017-05-20 16:18:01
tags: [Database, MySQL]
categories: [Database, MySQL]
---

### 1.**索引**的作用
在索引列上，除了有序查找之外，数据库利用各种各样的快速定位技术，能够大大提高查询效率。特别是当数据量非常大，查询涉及多个表时，使用索引往往能使查询速度加快成千上万倍。
例如，有3个未索引的表t1、t2、t3，分别只包含列c1、c2、c3，每个表分别含有1000行数据组成，指为1～1000的数值，查找对应值相等行的查询如下所示:
```mysql
SELECT c1,c2,c3 FROM t1,t2,t3 WHERE c1=c2 AND c1=c3
```
此查询结果应该为1000行，每行包含3个相等的值。在无索引的情况下处理此查询，必须寻找3个表所有的组合，以便得出与WHERE子句相配的那些行。而可能的组合数目为1000×1000×1000（十亿），显然查询将会非常慢。
如果对每个表进行索引，就能极大地加速查询进程。利用索引的查询处理如下:  
(1)从表t1中选择第一行，查看此行所包含的数据。  
(2)使用表t2上的索引，直接定位t2中与t1的值匹配的行。类似，利用表t3上的索引，直接定位t3中与来自t1的值匹配的行。  
(3)扫描表t1的下一行并重复前面的过程，直到遍历t1中所有的行。  
在此情形下，仍然对表t1执行了一个完全扫描，但能够在表t2和t3上进行索引查找直接取出这些表中的行，比未用索引时要快一百万倍。  
利用索引，MySQL加速了WHERE子句满足条件行的搜索，而在多表连接查询时，在执行连接时加快了与其他表中的行匹配的速度。

### 2.MySQL索引基本操作
1) 添加索引
ALTER TABLE用来创建普通索引、UNIQUE索引或PRIMARY KEY索引; CREATE INDEX可对表增加普通索引或UNIQUE索引, 不能用CREATE INDEX语句创建PRIMARY KEY索引。
```mysql
ALTER TABLE table_name ADD PRIMARY KEY (column_list);
ALTER TABLE table_name ADD UNIQUE (column_list);
ALTER TABLE table_name ADD INDEX index_name (column_list);

CREATE INDEX index_name ON table_name (column_list);
CREATE UNIQUE INDEX index_name ON table_name (column_list);
```
2) 删除索引
```mysql
DROP INDEX index_name ON talbe_name;
ALTER TABLE table_name DROP INDEX index_name;
ALTER TABLE table_name DROP PRIMARY KEY;
```
其中，前两条语句是等价的，删除掉table_name中的索引index_name。  
第3条语句只在删除PRIMARY KEY索引时使用，因为一个表只可能有一个PRIMARY KEY索引，因此不需要指定索引名。如果没有创建PRIMARY KEY索引，但表具有一个或多个UNIQUE索引，则MySQL将删除第一个UNIQUE索引。  
如果从表中删除了某列，则索引会受到影响。对于多列组合的索引，如果删除其中的某列，则该列也会从索引中删除。如果删除组成索引的所有列，则整个索引将被删除。
3) 查看索引
```mysql
SHOW INDEX FROM tblname;
SHOW KEYS FROM tblname;
```
| 字段 | 说明 |
| --- | --- |
| Table | 表的名称 |
| Non_unique | 如果索引不能包括重复词，则为0。如果可以，则为1 |
| Key_name | 索引的名称 |
| Seq_in_index | 索引中的列序列号，从1开始 |
| Column_name | 列名称 |
| Collation | 列以什么方式存储在索引中。在MySQL中，有值'A'（升序）或NULL（无分类） |
| Cardinality | 索引中唯一值的数目的估计值。通过运行ANALYZE TABLE或myisamchk -a可以更新。基数根据被存储为整数的统计数据来计数，所以即使对于小型表，该值也没有必要是精确的。基数越大，当进行联合时，MySQL使用该索引的机会就越大 |
| Sub_part | 如果列只是被部分地编入索引，则为被编入索引的字符的数目。如果整列被编入索引，则为NULL |
| Packed | 指示关键字如何被压缩。如果没有被压缩，则为NULL |
| Null | 如果列含有NULL，则含有YES。如果没有，则该列含有NO |
| Index_type | 用过的索引方法（BTREE, FULLTEXT, HASH, RTREE） |


### 3.Demo
创建测试数据表`test_table`，并插入测试数据：
```mysql
CREATE TABLE test_table (
  id INT(10) NOT NULL,
  name varchar(20),
  age integer,
  sex varchar(10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# DROP TABLE test_table;

SELECT * FROM test_table;
INSERT INTO test_table(id, name, age, sex) values(1, "Xiaowei Liu", 27,  "M");
INSERT INTO test_table(id, name, age, sex) values(2, "Xiaolong Wang", 30,  "M");

# EXPLAIN test_table;    # OK
SHOW CREATE TABLE test_table;
```
输出结果如下：
```mysql
# SHOW CREATE TABLE test_table;
'test_table', 'CREATE TABLE `test_table` (
  `id` int(10) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8'
```
此时，执行下面的命令，添加PRIMARY KEY（主键索引）：
```mysql
ALTER TABLE test_table ADD PRIMARY KEY (id);
SHOW CREATE TABLE test_table;
```
输出结果如下：
```mysql
'test_table', 'CREATE TABLE `test_table` (
  `id` int(10) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8'
```
此时，执行下面的命令，添加UNIQUE(唯一索引)：
```mysql
ALTER TABLE test_table ADD UNIQUE (name);
SHOW CREATE TABLE test_table;
```
输出结果如下：
```mysql
'test_table', 'CREATE TABLE `test_table` (
  `id` int(10) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8'
```
此时，执行下面的命令，添加INDEX(普通索引)
```mysql
ALTER TABLE test_table ADD INDEX lxw_index_name (age);
SHOW CREATE TABLE test_table;
```
输出结果如下：
```mysql
'test_table', 'CREATE TABLE `test_table` (
  `id` int(10) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `lxw_index_name` (`age`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8'
```
执行下面的命令，查看test_table表结构:
```mysql
EXPLAIN test_table;
```
输出结果如下:
```mysql
# EXPLAIN test_table;
Field,Type,Null,Key,Default,Extra
id,int(10),NO,PRI,NULL,
name,varchar(20),YES,UNI,NULL,
age,int(11),YES,MUL,NULL,
sex,varchar(10),YES,,NULL,
```
简单解释一下：如果Key是MUL，那么该列的值可以重复，该列是一个非唯一索引的前导列(第一列)或者是一个唯一性索引的组成部分但是可以含有空值NULL。

4.添加FULLTEXT(全文索引)
```
ALTER TABLE `table_name` ADD FULLTEXT (`column`);
```
5.添加多列索引
```mysql
ALTER TABLE test_table ADD INDEX ix_name_age(name, age);
SHOW INDEX FROM test_table;
```
输出结果如下:
```mysql
Table,Non_unique,Key_name,Seq_in_index,Column_name,Collation,Cardinality,Sub_part,Packed,Null,Index_type,Comment,Index_comment
test_table,0,PRIMARY,1,id,A,2,NULL,NULL,,BTREE,,
test_table,0,name,1,name,A,2,NULL,NULL,YES,BTREE,,
test_table,1,ix_age,1,age,A,2,NULL,NULL,YES,BTREE,,
test_table,1,ix_name_age,1,name,A,2,NULL,NULL,YES,BTREE,,
test_table,1,ix_name_age,2,age,A,2,NULL,NULL,YES,BTREE,,
```
<!-- 1. 2. 3. Reference -->
[MySQL性能分析及explain的使用]: http://database.51cto.com/art/201108/284783.htm
[MySQL查看、创建和删除索引的方法]: http://www.jb51.net/article/73372.htm

### 4.聚集索引和非聚集索引
聚集索引一个表只能有一个，而非聚集索引一个表可以存在多个
聚集索引存储记录是物理上连续的，而非聚集索引是逻辑上的连续，物理存储并不连续

在数据库中，聚集索引和非聚集索引是以二叉树的形式描述的：
聚集索引的叶节点就是最终的数据节点，而非聚集索引的叶节点仍然是索引节点，但它有一个指向最终数据的指针。

总结如下:

| 动作描述 | 使用聚集索引 | 使用非聚集索引 |
| :--- | :---: | :---: |
| 列经常被分组排序 | 应 | 应 |
| 返回某范围内的数据 | 应 | 不应 |
| 一个或极少不同值 | 不应 | 不应 |
| 小数目的不同值 | 应 | 不应 |
| 大数目的不同值 | 不应 | 应 |
| 频繁更新的列 | 不应 | 应 |
| 外键列 | 应 | 应 |
| 主键列 | 应 | 应 |
| 频繁修改索引列 | 不应 | 应 |
详细内容和几个不错的知识点可以参考[这里][聚集索引和非聚集索引的区别理解]。

<!-- 4. Reference-->
[聚集索引和非聚集索引的区别理解]: http://blog.csdn.net/liu_ben_qian/article/details/8472902
[聚集索引和非聚集索引（整理）]: http://www.cnblogs.com/aspnethot/articles/1504082.html
[50多条实用mysql数据库优化建议 ]: https://mp.weixin.qq.com/s?__biz=MzA3MDg0MjgxNQ==&mid=2652391032&idx=1&sn=1492e7fd23c32d15be4250617cac6616&chksm=84da46a8b3adcfbecaead4b8d050856507ec5e372445c867541bce8df5cc07f81c0b558f562d&mpshare=1&scene=1&srcid=0417sRhuuqmraD8rGV9sWdIP&pass_ticket=IuQgf49t22799QAeYgJ2ZdeUsJla%2FLxVmZNOco9%2BuZzB3Bn6ncIdFMQ5sxYwH%2FQA#rd

