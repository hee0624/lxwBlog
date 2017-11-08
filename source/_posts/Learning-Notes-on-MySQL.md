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

<!-- References -->
[MySQL的语句执行顺序]: http://www.cnblogs.com/rollenholt/p/3776923.html
[MySQL Order of Operations?]: http://stackoverflow.com/questions/4001183/mysql-order-of-operations

### 2.聚集索引和非聚集索引
聚集索引一个表只能有一个，而非聚集索引一个表可以存在多个  
聚集索引存储记录是物理上连续的，而非聚集索引是逻辑上的连续，物理存储并不连续  

在数据库中，聚集索引和非聚集索引是以二叉树的形式描述的：  
聚集索引的叶节点就是最终的数据节点，而非聚集索引的叶节仍然是索引节点，但它有一个指向最终数据的指针。

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

<!--### Reference-->
[聚集索引和非聚集索引的区别理解]: http://blog.csdn.net/liu_ben_qian/article/details/8472902
[聚集索引和非聚集索引（整理）]: http://www.cnblogs.com/aspnethot/articles/1504082.html
[50多条实用mysql数据库优化建议 ]: https://mp.weixin.qq.com/s?__biz=MzA3MDg0MjgxNQ==&mid=2652391032&idx=1&sn=1492e7fd23c32d15be4250617cac6616&chksm=84da46a8b3adcfbecaead4b8d050856507ec5e372445c867541bce8df5cc07f81c0b558f562d&mpshare=1&scene=1&srcid=0417sRhuuqmraD8rGV9sWdIP&pass_ticket=IuQgf49t22799QAeYgJ2ZdeUsJla%2FLxVmZNOco9%2BuZzB3Bn6ncIdFMQ5sxYwH%2FQA#rd
