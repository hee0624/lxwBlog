---
title: Learning Notes on Python
date: 2017-06-06 15:06:39
tags: Python
categories: Python
---

1.[Multiprocessing and multithreading in Python 3](https://www.ploggingdev.com/2017/01/multiprocessing-and-multithreading-in-python-3/)

+ **The CPython implementation has a Global Interpreter Lock (GIL) which allows only one thread to be active in the interpreter at once.** This means that threads cannot be used for parallel execution of Python code. **While parallel CPU computation is not possible, parallel IO operations are possible using threads. __This is because performing IO operations releases the GIL.__** To learn more about the GIL refer [here](http://www.dabeaz.com/python/UnderstandingGIL.pdf).

+ Threads should not be used for CPU bound tasks. Using threads for CPU bound tasks will actually result in worse performance compared to using a single thread.

2.super()函数
Java中的super
1). super 调用基类中的某一个构造函数（应该为构造函数中的第一条语句） 
2). super()和this()均需放在构造方法内第一行
3). 尽管可以用this调用一个构造器，但却不能调用两个
4). this和super不能同时出现在一个构造函数里面，因为this必然会调用其它的构造函数，其它的构造函数必然也会有super语句的存在，所以在同一个构造函数里面有相同的语句，就失去了语句的意义，编译器也不会通过
5). this()和super()都指的是对象，所以，均不可以在static环境中使用。包括：static变量,static方法，static语句块。

Python中的super
1). super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，产生了一个super对象；
2). super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
3). super(B, self).func的调用并不是用于调用当前类的父类的func函数；
4). Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数只调用一次（如果每个类都使用super）；
5). 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一个父类函数被调用多次。
Reference: [Python中的super用法详解](http://www.jb51.net/article/66912.htm)