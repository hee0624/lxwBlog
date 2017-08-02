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

3.
三个函数
[`filter()`](http://www.cnblogs.com/Lambda721/p/6128424.html), [`map()`](http://www.cnblogs.com/Lambda721/p/6128351.html), [`reduce()`](http://www.cnblogs.com/Lambda721/p/6128384.html)
`Python 3`已经将`reduce()`函数从全局命名空间里移除了，现在被放置在`functools`模块中(`from functools import reduce`)

4.
P40
1).如果把迭代器对象(生成器对象也可以)传给内置的iter函数，那么iter函数会把该迭代器对象返回；  
2).如果传给iter函数的是个容器类型的对象(list/set/dict/tuple)，那么iter函数每次都会返回**新的**迭代器对象  
于是我们可以根据iter函数的这种行为来判断输入值是不是一个迭代器对象
**1)的验证:**
```python
In [1]: def func():
   ...:     for item in range(10):
   ...:         yield item
   ...:         

In [2]: type(func)
Out[2]: function

In [3]: type(func())
Out[3]: generator

In [4]: iter(func()) is iter(func())
Out[4]: False

In [5]: iter(func()) is func()
Out[5]: False

In [6]: temp_func = func()

In [7]: iter(temp_func) is temp_func
Out[7]: True

In [8]: iter(temp_func) is iter(temp_func)
Out[8]: True
```
注意`In/Out [4]&In/Out [5]`与`In/Out [7]&In/Out [8]`的区别，多次调用`func()`返回的是不同的生成器对象
```python
In [21]: a = func()

In [22]: b = func()

In [23]: a
Out[23]: <generator object func at 0x7f02a6f56f10>

In [24]: b
Out[24]: <generator object func at 0x7f02a7ab1728>
```
**2)的验证:**
```python
In [25]: a_list = [1, 2, 3]

In [26]: iter(a_list) is a_list
Out[26]: False

In [27]: iter(a_list) is iter(a_list)
Out[27]: False
```
从`In/Out [27]`我们能够看出如果传给iter函数的是个容器类型的对象(list/set/dict/tuple)，那么iter函数每次都会返回**新的**迭代器对象  

5.
P42
```python
In [37]: def func(*args):
    ...:     print(len(args))
    ...:     print(type(args))
    ...:     print(args)
    ...:     

In [38]: a_list
Out[38]: [1, 2, 3]

In [39]: func(a_list)
1
<class 'tuple'>
([1, 2, 3],)

In [40]: func(*a_list)
3
<class 'tuple'>
(1, 2, 3)

In [41]: *a_list
  File "<ipython-input-41-8d6ae4d8d4b3>", line 1
    *a_list
           ^
SyntaxError: can't use starred expression here
```

6.
