---
title: Learning Notes on Python
date: 2017-06-06 15:06:39
tags: Python
categories: Python
---

1.[Multiprocessing and multithreading in Python 3](https://www.ploggingdev.com/2017/01/multiprocessing-and-multithreading-in-python-3/)

+ **The CPython implementation has a Global Interpreter Lock (GIL) which allows only one thread to be active in the interpreter at once.** This means that threads cannot be used for parallel execution of Python code. **While parallel CPU computation is not possible, parallel IO operations are possible using threads. __This is because performing IO operations releases the GIL.__** To learn more about the GIL refer [here](http://www.dabeaz.com/python/UnderstandingGIL.pdf).

+ Threads should not be used for CPU bound tasks. Using threads for CPU bound tasks will actually result in worse performance compared to using a single thread.