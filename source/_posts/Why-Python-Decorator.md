---
title: 为什么要使用装饰器Decorator?
date: 2017-03-20 21:24:17
tags: Python
categories: Python
---

为什么要用装饰器？*[减少代码改动](http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html)*，*[实现代码重用](http://www.cnblogs.com/xwang/p/3549039.html)*

### 场景
假设有两个文件`utils.py`和`run.py`，内容分别如下：
`utils.py`文件内容：
```python
#!/usr/bin/env python
#File Name: utils.py
#Author: A

def showNums():
    print [i for i in xrange(10)]
    #some code that may throw exception
```
`run.py`文件内容：
```python
#!/usr/bin/env python
#File Name: run.py
#Author: B

from utils import showNums

if __name__ == '__main__':
    showNums()
    print "A lot of codes here."
    showNums()
    print "A lot of codes here."
    showNums()
    print "A lot of codes here."
    showNums()
    print "A lot of codes here."
    showNums()
```
`utils.py`的作者是`A`和`run.py`的作者是`B`，假如某天作者`A`需要对`utils.py`中的`showNums()`函数的功能进行修改：想增加异常捕获功能（或者其他复杂得多的功能）。此时`A`可以直接修改`showNums()`函数，增加`try...except`代码。
*但如果有很多类似`showNums()`的函数都需要进行这样的处理，作者`A`该怎么办？逐个修改所有的这些函数似乎有点儿麻烦，而且有很多重复的代码*。因此，直接修改`showNums()`函数的方案不可取。

### 假方案
作者`A`可以重新定义一个函数`addTryExcept(func)`，将函数`showNums()`作为参数传递给它，然后在`addTryExcept(func)`中调用`showNums()`。这样，就达到了不改动`showNums()`函数的目的。按照这种思路，重写上述的`utils.py`文件。
修改后的`utils.py`文件内容：
```python
#!/usr/bin/env python
#File Name: utils.py
#Author: A

def showNums():
    print [i for i in xrange(10)]
    #some code that may throw exception

def addTryExcept(func):
    try:
        func()
    except Exception as e:
        print e
```
但此时显然需要通知`run.py`的作者`B`:`showNums()`函数更新了，新的调用方法是`addTryExcept(showNums)`。然后作者`B`在`run.py`将所有`showNums()`的调用修改为`addTryExcept(showNums)`（如果有其他类似的函数，`B`也需要进行相应的修改）。
**这种方案显然也是不可取的**，虽然作者`A`不用逐个修改所有的这些函数。**然而**，每次`A`对函数进行升级后，需要`B`做大量的修改工作。

### 一种方案
如果不修改调用代码（作者`B`的代码），也就意味着调用`showNums()`函数需要产生调用`addTryExcept(showNums)`的效果。我们可以想到将`addTryExcept(showNums)`赋值给`showNums`，**这就需要`addTryExcept(showNums)`不是直接产生调用效果，而是返回一个与`showNums`参数列表一致的函数([闭包](https://segmentfault.com/a/1190000002965736))。**并且，这样能够保证调用`showNums()`函数的代码完全不用修改！
重写上述的`utils.py`文件：
```python
#!/usr/bin/env python
#File Name: utils.py
#Author: A

def showNums():
    print [i for i in xrange(10)]
    #some code that may throw exception

def addTryExcept(func):
    def _func():
        try:
            print "in decorator."
            func()
        except Exception as e:
            print e
    return _func

showNums = addTryExcept(showNums)
```
我们发现这能够很好地满足作者`A`的需求。
这一方案其实就是Python中的**装饰器**思想。

### 装饰器`Decorator`方案
>在不修改函数本身的情况下，使某个函数整体增加异常捕获功能（或者在函数**前后**增加更加复杂的功能），并且不修改函数的对外接口。这一场景，我们可以采用`装饰器Decorator`来实现。

使用Python的[装饰器](http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html)思想重写`utils.py`文件：

```python
#!/usr/bin/env python
#File Name: utils.py
#Author: A

def addTryExcept(func):
    def _func():
        try:
            print "in decorator."
            func()
        except Exception as e:
            print e
    return _func

@addTryExcept
def showNums():
    print [i for i in xrange(10)]
    #some code that may throw exception
```
在上述代码中，第一个函数`addTryExcept`就是装饰函数，它的参数就是被装饰的函数对象。我们可以在`addTryExcept`函数内对传入的函数对象做一番“装饰”，然后返回这个对象（**一定要返回 ，不然外面调用func的地方将会无函数可用**）。
利用装饰器，只要在函数定义的上面加上`@decoratorFuncName`，而不用修改函数调用的地方。同时，原来的函数内的代码也不用改动。
如果有很多类似于`showNums()`的函数需要进行同样的处理，那么这些函数的定义处也需要增加`@decoratorFuncName`语句，看起来工作量不少，但相比于在所有的函数调用处进行修改，显然是要合理有效得多。
装饰器的确可以在`简化代码`、`重用代码`方面提供非常大的帮助。
