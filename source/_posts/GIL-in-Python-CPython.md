---
title: GIL in Python(CPython)
date: 2018-04-17 15:05:41
tags: [Python, CPython, GIL]
categories: [Python, CPython, GIL]
---

## 1. GIL是什么
首先需要明确的一点是GIL并不是Python的特性, Python完全可以不依赖于GIL. GIL(Global Interpreter Lock)是在实现**Python解析器(CPython)**时所引入的一个概念. 对于Python而言, 同一段代码可以通过CPython, PyPy, JPython等不同的Python执行环境来执行, **像其中的JPython就没有GIL**. 然而因为CPython是大部分环境下默认的Python执行环境, 所以在很多人的概念里CPython就是Python, 也就想当然的把GIL归结为Python语言的缺陷.   
官方给出的解释如下:
> In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

## 2. 如何减少受到GIL的影响
1. 用multiprocessing替代Thread
multiprocessing库的出现很大程度上是为了弥补thread库因为GIL而低效的缺陷. 它完整的复制了一套thread所提供的接口方便迁移. 唯一的不同就是它使用了多进程而不是多线程. **每个进程有自己的独立的GIL, 因此也不会出现进程之间的GIL争抢**. 
2. 用其他解析器
之前也提到了既然GIL只是CPython的产物, 那么其他解析器是不是更好呢？没错, 像JPython和IronPython这样的解析器由于实现语言的特性, 他们不需要GIL的帮助. 然而由于用了Java/C#用于解析器实现, 他们也失去了利用社区众多C语言模块有用特性的机会. 所以这些解析器也因此一直都比较小众. 毕竟功能和性能大家在初期都会选择前者, `Done is better than perfect`. 

## 3. 总结
1. Python的多线程在多核CPU上, 只对于IO密集型计算产生正面效果；而当至少有一个CPU密集型线程存在时, 多线程效率会由于GIL而大幅下降. 
2. Python GIL其实是功能和性能之间权衡后的产物, 它有其存在的合理性, 也有较难改变的客观因素. GIL在较长一段时间内将会继续存在, 但是会不断改进
3. 如果对并行计算性能要求较高的程序可以考虑把核心部分写成C模块, 或者索性用其他语言实现

## 4. References
1. [Python的GIL是什么鬼, 多线程性能究竟如何](http://cenalulu.github.io/python/gil-in-python/)
