---
title: Learning-Notes-on-Sentiment-Analysis
date: 2018-06-03 15:52:45
tags: [NLP]
categories: [NLP]
---
目前常见的情感极性分析方法主要是两种：**基于情感词典的方法**和**基于机器学习的方法**。  
## 1.基于情感词典的方法
基于情感词典的情感极性分析影响准确度的一个重要原因就是**同一个词在不同的语境下可能代表完全相反的情感意义(一词多义、反语等)**。  
同一个词可作多种词性，那么情感分数也不应相同，例如:
```
这部电影真垃圾
垃圾分类
```
显然在第一句中`垃圾`表现强烈的贬义，而在第二句中表示中性，**单一评分对于这类问题的分类难免有失偏颇**。  
情感值计算公式:   
```python
final_senti_score = ((-1) ** num_of_notwords) * degree_value * senti_score
final_score = sum(final_senti_score)
```
`num_of_notwords`是否定词的个数，`degree_value`程度副词的数值，`senti_score`词的情感分值  

## 2.基于机器学习的方法
基于机器学习的方法也存在**同一个词在不同的语境下可能代表完全相反的情感意义(一词多义、反语等)**的情况，但相比于基于词典的情感分析方法，基于机器学习的方法更为客观

## References
[Python做文本情感分析之情感极性分析](https://www.jianshu.com/p/4cfcf1610a73)