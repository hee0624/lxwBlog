---
title: Learning Notes on MySQL
date: 2016-08-16 11:06:16
tags: [Database, MySQL]
categories: [Database, MySQL]
---

### 1.[MySQL的语句执行顺序][MySQL的语句执行顺序]
MySQL的语句一共分为11步，如下所标注的那样，**最先执行的总是FROM操作，最后执行的是LIMIT操作**。其中每一个操作都会产生一张虚拟的表，这个虚拟的表作为一个处理的输入，只是这些虚拟的表对用户来说是透明的，但是只有最后一个虚拟的表才会被作为结果返回。如果没有在语句中指定某一个子句，那么将会跳过相应的步骤。
```sql
(8)SELECT (9)DISTINCT <select_list>
(1)FROM <left_table>
(3)<join_type> JOIN <right_table>
(2)ON <join_condition>
(4)WHERE <where_condition>
(5)GROUP BY <group_by_list>
(6)WITH {CUBE|ROLLUP}
(7)HAVING <having_condition>
(10)ORDER BY <order_by_list>
(11)LIMIT <limit_number>
```

查询处理的每一个阶段说明如下：

| SQL子句 | 说明 |
| --- | --- |
| `FROM` | 对FROM的左边的表和右边的表计算笛卡尔积。产生虚表VT1 |
| `ON` | 对虚表VT1进行ON筛选，只有那些符合<join-condition>的行才会被记录在虚表VT2中 |
| `JOIN `| 如果指定了OUTER JOIN（比如left join、 right join），那么保留表中未匹配的行就会作为外部行添加到虚拟表VT2中，产生虚拟表VT3, 如果from子句中包含两个以上的表的话，那么就会对上一个join连接产生的结果VT3和下一个表重复执行步骤1~3这三个步骤，一直到处理完所有的表为止 |
| `WHERE` | 对虚拟表VT3进行WHERE条件过滤。只有符合<where-condition>的记录才会被插入到虚拟表VT4中 |
| `GROUP BY` | 根据group by子句中的列，对VT4中的记录进行分组操作，产生VT5 |
| `WITH` | 对表VT5进行cube或者rollup操作，产生表VT6 |
| `HAVING` | 对虚拟表VT6应用having过滤，只有符合<having-condition>的记录才会被 插入到虚拟表VT7中 |
| `SELECT` | 执行select操作，选择指定的列，插入到虚拟表VT8中 |
| `DISTINCT` | 对VT8中的记录进行去重。产生虚拟表VT9 |
| `ORDER BY` | 将虚拟表VT9中的记录按照<order_by_list>进行排序操作，产生虚拟表VT10 |
| `LIMIT` | 取出指定行的记录，产生虚拟表VT11, 并将结果返回 |

也有人说正确的顺序是下面这样的：
```sql
FROM clause
WHERE clause
SELECT clause
GROUP BY clause
HAVING clause
ORDER BY clause
```
除了`SELECT`子句的执行顺序存在差异外，其他的子句执行顺序相同。在[StackOverflow][MySQL Order of Operations?]上查阅到的结果与最上面的说法是一致的。个人也更倾向于最上面的说法。

<!-- 1. References -->
[MySQL的语句执行顺序]: http://www.cnblogs.com/rollenholt/p/3776923.html
[MySQL Order of Operations?]: http://stackoverflow.com/questions/4001183/mysql-order-of-operations

### 2.MySQL Tips
1).在建立索引时，可能会因为数据量太大，导致索引建立的时间特别长；这时可以尝试重启mysqld服务，然后再建立索引，速度会快很多很多  
2).
```python
sql = "SELECT DISTINCT news.id AS anon_1, news.public_time, news.news_type, news.theme_type, news.history_similarity " \
              "FROM news FORCE INDEX (ix_news_public_time), relation_node_news " \
              "WHERE  relation_node_news.news_id = news.id " \
              "AND relation_node_news.node_type = %s " \
              "AND date(news.public_time) >= '%s' AND date(news.public_time) < '%s' %s " \
              "ORDER BY news.public_time DESC ;" % \
              (NODE_TYPE, start_time, end_time, cases)

```
date函数的效率是很低的，去掉date效率高了很多，检索速度快了很多

### 3.MySQL基本操作
```sql
CREATE DATABASE test_db;
SHOW DATABASES;
USE test_db;
SHOW TABLES;
DROP TABLE employee;
DROP DATABASE test_db;

CREATE TABLE employee (
  id INT(10) NOT NULL AUTO_INCREMENT,
  name varchar(20) NOT NULL,
  age integer,
  date_on_board datetime,
  income float,
  adult boolean,
  address text,
  update_time timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# update_time timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

SHOW CREATE TABLE employee;
SHOW COLUMNS FROM employee;
EXPLAIN employee;    # equals to "DESC employee;"

ALTER TABLE employee ADD PRIMARY KEY (id);
ALTER TABLE employee ADD UNIQUE (name);
ALTER TABLE employee ADD INDEX _ix_age (age);

SELECT * FROM employee;
INSERT INTO employee(name, age, date_on_board, income, adult, address) VALUES("Xiaowei Liu", 27, "20160713", 8000.1, TRUE, "北京市海淀区中关村南一街一号软件园1号楼");    # OK
INSERT INTO employee(name, age, date_on_board, income, adult, address) VALUES("Baoyi Li", 15, "20200612", 6010.1, False, "北京市海淀区中关村南一街一号软件园7号楼");    # OK
```

### 4.MySQL中的`DISTINCT`关键字是针对`SELECT`返回的整体结果进行的，而不仅仅是`DISTINCT`紧跟的那个字段  
```sql
SELECT age, sex
FROM table2;
/*
# age, sex
'1', 'F'
'2', 'F'
'2', 'M'
'3', 'M'
'3', 'F'
'4', 'M'
'4', 'F'
*/

SELECT DISTINCT age, sex
FROM table2;
/*
# age, sex
'1', 'F'
'2', 'F'
'2', 'M'
'3', 'M'
'3', 'F'
'4', 'M'
'4', 'F'
*/
```


### 5.EXPLAIN的使用
TODO
<!-- 4.Reference -->
[MySQL性能分析及explain的使用]: http://database.51cto.com/art/201108/284783.htm

