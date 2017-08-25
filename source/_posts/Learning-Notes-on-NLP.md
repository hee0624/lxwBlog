---
title: Learning Notes on NLP
date: 2017-08-07 14:32:28
tags: [NLP]
categories: [NLP]
---

### [语言技术平台（Language Technology Platform，LTP）](http://www.ltp-cloud.com/intro/#ltp)
#### 1.分词(Word Segmentation, WS)
```
李克强/ 调研
李克/ 强调/ 研
```
切分歧义是分词任务中的主要难题。LTP的分词模块基于机器学习框架，可以很好地解决歧义问题。 同时，模型中融入了词典策略，使得LTP的分词模块可以很便捷地加入新词信息。  

#### 2.分词词典的使用效果测试
不锈钢/不锈钢材/不锈钢答  （使用“不锈钢答”是为了增加对比，“不锈钢答”分词一定会把“答”单独分出来）  
**1>不使用外部词典，验证分词结果**  
```python
def test_segmentation(self):
    segmentor = Segmentor()    # 初始化实例
    cws_model_path = os.path.join(self.LTP_MODEL_DIR, "cws.model")    # 分词模型路径，模型名称为`cws.model`

    # segmentor.load_with_lexicon(cws_model_path, "./my_lexicon.txt")    # 加载模型并使用外部词典
    segmentor.load(cws_model_path)

    words = segmentor.segment("不锈钢的价格很贵")
    print("|".join(words))

    words = segmentor.segment("不锈钢板的价格很贵")
    print("|".join(words))

    words = segmentor.segment("不锈钢答的价格很贵")
    print("|".join(words))

    segmentor.release()  # 释放模型
```
运行结果：
```bash
$ python pyltp_demo.py
不锈钢|的|价格|很|贵
不锈钢板|的|价格|很|贵
不锈钢|答|的|价格|很|贵
```
**2>使用外部词典，验证分词结果**  
```python
def test_segmentation(self):
    segmentor = Segmentor()    # 初始化实例
    cws_model_path = os.path.join(self.LTP_MODEL_DIR, "cws.model")    # 分词模型路径，模型名称为`cws.model`

    segmentor.load_with_lexicon(cws_model_path, "./my_lexicon.txt")    # 加载模型并使用外部词典
    # segmentor.load(cws_model_path)

    words = segmentor.segment("不锈钢的价格很贵")
    print("|".join(words))

    words = segmentor.segment("不锈钢板的价格很贵")
    print("|".join(words))

    words = segmentor.segment("不锈钢答的价格很贵")
    print("|".join(words))

    segmentor.release()  # 释放模型
```
1)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:19:56 loaded 1 lexicon entries
不锈钢|的|价格|很|贵
不锈钢|板|的|价格|很|贵
不锈钢|答|的|价格|很|贵
```
2)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢板
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:25:37 loaded 1 lexicon entries
不锈钢|的|价格|很|贵
不锈钢板|的|价格|很|贵
不锈钢|答|的|价格|很|贵
```
3)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢答
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:27:39 loaded 1 lexicon entries
不锈钢|的|价格|很|贵
不锈钢板|的|价格|很|贵
不锈钢答|的|价格|很|贵
```
4)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢
不锈钢板
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:30:04 loaded 2 lexicon entries
不锈钢|的|价格|很|贵
不锈钢板|的|价格|很|贵
不锈钢|答|的|价格|很|贵
```
5)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢
不锈钢答
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:28:47 loaded 2 lexicon entries
不锈钢|的|价格|很|贵
不锈钢|板|的|价格|很|贵
不锈钢答|的|价格|很|贵
```
6)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢板
不锈钢答
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:31:18 loaded 2 lexicon entries
不锈钢|的|价格|很|贵
不锈钢板|的|价格|很|贵
不锈钢答|的|价格|很|贵
```
7)查看外部词典：
```bash
$ cat my_lexicon.txt
不锈钢
不锈钢板
不锈钢答
```
运行结果：
```bash
$ python pyltp_demo.py
[INFO] 2017-08-25 11:31:54 loaded 3 lexicon entries
不锈钢|的|价格|很|贵
不锈钢板|的|价格|很|贵
不锈钢答|的|价格|很|贵
```
从1)和5)的实验结果可以看出，外部词典的优先级高于默认分词(外部词典中只有“不锈钢”，没有“不锈钢板”，“不锈钢板”被分开了)
