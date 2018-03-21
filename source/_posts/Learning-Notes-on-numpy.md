---
title: Learning Notes on numpy
date: 2018-01-27 23:32:09
tags: [numpy, Machine Learning]
categories: [numpy, Machine Learning]
---

Reference: [NumPy-快速处理数据](http://old.sebug.net/paper/books/scipydoc/numpy_intro.html)  

1.标准安装的Python中用列表(list)保存一组值，可以用来当作数组使用，不过由于列表的元素可以是任何对象，因此列表中所保存的是对象的指针。这样为了保存一个简单的`[1,2,3]`，需要有3个指针和三个整数对象。对于数值运算来说这种结构显然比较浪费内存和CPU计算时间。  
 Python还提供了一个array模块，array对象和列表不同，它直接保存数值，和C语言的一维数组比较类似。但是由于它不支持多维，也没有各种运算函数，因此也不适合做数值运算。  
2.Numpy traps and pitfalls:  
1).reshape()返回的新数组**与原数组共享数据空间**


```python
import numpy as np

a = np.arange(1, 5)
print(a)
b = a.reshape(2, 2)
print(b)
```

    [1 2 3 4]
    [[1 2]
     [3 4]]



```python
a[1] = -1
print(a)
print(b)
```

    [ 1 -1  3  4]
    [[ 1 -1]
     [ 3  4]]


**数组a和b其实共享数据存储内存区域，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容**  
2).切片操作返回的新数组**与原数组共享数据空间**


```python
a = np.arange(10)
print(a)
b = a[3:7]
print(b)
```

    [0 1 2 3 4 5 6 7 8 9]
    [3 4 5 6]



```python
a[5] = -1
print(a)
print(b)
```

    [ 0  1  2  3  4 -1  6  7  8  9]
    [ 3  4 -1  6]


和Python的list数据类型不同，在numpy中**通过下标范围(切片)获取的新的数组是原始数组的一个视图，它与原始数组共享同一块数据空间**。

3).使用**整数序列**作为下标获得的数组**不和原数组共享数据空间**


```python
arr = np.arange(10)
print(arr)
# 1. arr1和arr2是两种不同但等价的用法
arr1 = arr[[1, 2, 1, -1]]
print(arr1)
arr2 = arr[np.array([1, 2, 1, -1])]
print(arr2)
arr1[1] = -10
# 2. arr和arr1和arr2不共享数据空间，因此只有arr1中的数据发生了改变
print(arr)
print(arr1)
print(arr2)
# 3. 整数序列下标也可以用来修改元素的值
arr[[3, 5, 1]] = -3, -5, -1
print(arr)
print(arr1)
print(arr2)
```

    [0 1 2 3 4 5 6 7 8 9]
    [1 2 1 9]
    [1 2 1 9]
    [0 1 2 3 4 5 6 7 8 9]
    [  1 -10   1   9]
    [1 2 1 9]
    [ 0 -1  2 -3  4 -5  6  7  8  9]
    [  1 -10   1   9]
    [1 2 1 9]


4).使用**布尔数组**作为下标获得的数组**不和原数组共享数据空间**，注意这种方式只能使用布尔**数组(numpy.ndarray)**，不能使用布尔**列表(list)**


```python
arr = np.arange(5)
print(arr)
# 1. 只对应于布尔数组(numpy.ndarray)，不能使用布尔列表(list)
arr1 = arr[np.array([True, False, True, False, False])]
print(arr1)
# 2. NOTE： 网址上的说明是：若为布尔列表(list)，则True为1, False为0，按照整数序列获取arr中的元素
# 但实际的测试结果是：布尔数组与整数序列的使用方式相同，都是两种（既可以使用list也可以使用ndarray）
arr2 = arr[[True, False, True, False, False]]
print(arr2)
arr3 = arr[[1, 0, 1, 0, 0]]
print(arr3)
```

    [0 1 2 3 4]
    [0 2]
    [0 2]
    [1 0 1 0 0]


布尔数组一般不是手工产生，而是使用布尔运算的ufunc函数产生


```python
# 产生一个长度为5，元素值为0-1的随机数的数组
rand_ndarray = np.random.rand(5)
print(rand_ndarray)
# 数组中的每个元素和0.5进行大小比较，得到一个布尔数组，True表示对应的值大于0.5
print(rand_ndarray > 0.5)
# 使用rand_ndarray > 0.5返回的布尔数组收集x中的元素，结果:数组中所有大于0.5的元素
arr1 = rand_ndarray[rand_ndarray > 0.5]
print(arr1)
```

    [ 0.30882553  0.62608515  0.97691458  0.79139355  0.54452488]
    [False  True  True  True  True]
    [ 0.62608515  0.97691458  0.79139355  0.54452488]

