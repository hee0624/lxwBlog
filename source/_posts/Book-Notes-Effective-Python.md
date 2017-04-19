---
title: 'Book Notes: Effective Python'
date: 2017-02-18 21:51:43
tags: [Python, Reading]
categories: [Python, Reading]
---

1.
P5 第3条
`Python3`有两种表示字符串的类型： `bytes`和`str`，前者包含原始的8位值；后者包含Unicode字符。
`Python2`也有两种表示字符串的类型： `str`和`unicode`， 前者包含原始的8位值；后者包含Unicode字符。
注意`str`类型的字符串在`Python3`和`Python2`中包含的数据类型不同。

P6 下面的验证：
`Python3`:
```python
>>> a = "hello"
>>> b = u"hello"
>>> a
'hello'
>>> b
'hello'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> a == b
True
>>> c = a.encode("utf-8")
>>> c
b'hello'
>>> type(c)
<class 'bytes'>
>>> a == b
True
>>> a == c
False
>>> b == c
False
```

```python
>>> d = ""
>>> d
''
>>> type(d)
<class 'str'>
>>> e = "".encode("utf-8")
>>> e
b''
>>> type(e)
<class 'bytes'>
>>> d == e
False
```

`Python2`:
```python
>>> a = "hello"
>>> b = u"hello"
>>> a
'hello'
>>> b
u'hello'
>>> type(a)
<type 'str'>
>>> type(b)
<type 'unicode'>
>>> a == b
True
>>> c = a.encode("utf-8")
>>> c
'hello'
>>> type(c)
<type 'str'>
>>> a == b
True
>>> a == c
True
>>> b == c
True
```

```python
>>> d = ""
>>> d
''
>>> type(d)
<type 'str'>
>>> e = "".encode("utf-8")
>>> e
''
>>> type(e)
<type 'str'>
>>> d == e
True
>>> f = u""
>>> f
u''
>>> type(f)
<type 'unicode'>
>>> d == f
True
>>> e == f
True
```

2.
P14 下面
> 会多产生一份原数据的**浅拷贝**

验证

```python
>>> a = [[0, 10], [1, 11], [2, 12], [3, 1, 23]]
>>> a
[[0, 10], [1, 11], [2, 12], [3, 1, 23]]
>>> b = a[2:]
>>> b
[[2, 12], [3, 1, 23]]
>>> a
[[0, 10], [1, 11], [2, 12], [3, 1, 23]]
>>> a[2][0] = 0
>>> a
[[0, 10], [1, 11], [0, 12], [3, 1, 23]]
>>> b
[[0, 12], [3, 1, 23]]
>>> b[0][1] = 102
>>> b
[[0, 102], [3, 1, 23]]
>>> a
[[0, 10], [1, 11], [0, 102], [3, 1, 23]]
```

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = a[2:]
>>> a
[1, 2, 3, 4, 5]
>>> b
[3, 4, 5]
>>> a[2] = 6
>>> a
[1, 2, 6, 4, 5]
>>> b
[3, 4, 5]
>>> b[1] = 7
>>> b
[3, 7, 5]
>>> a
[1, 2, 6, 4, 5]
```

3.三个函数
[`filter()`](http://www.cnblogs.com/Lambda721/p/6128424.html), [`map()`](http://www.cnblogs.com/Lambda721/p/6128351.html), [`reduce()`](http://www.cnblogs.com/Lambda721/p/6128384.html)
`Python 3`已经将`reduce()`函数从全局命名空间里移除了，现在被放置在`functools`模块中(`from functools import reduce`)

4.
