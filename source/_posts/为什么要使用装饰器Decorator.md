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

def show_nums():
    print([i for i in range(10)])
    # some code that may throw exception
```
`run.py`文件内容：
```python
#!/usr/bin/env python
#File Name: run.py
#Author: B

from utils import show_nums


if __name__ == '__main__':
    show_nums()
    print("A lot of codes here.")

    show_nums()
    print("A lot of codes here.")

    show_nums()
    print("A lot of codes here.")

    show_nums()
    print("A lot of codes here.")

    show_nums()
    print("A lot of codes here.")
```
`utils.py`的作者是`A`和`run.py`的作者是`B`，假如某天作者`A`需要对`utils.py`中的`show_nums()`函数的功能进行修改：想增加异常捕获功能（或者其他复杂得多的功能）。此时`A`可以直接修改`show_nums()`函数，增加`try...except`代码。
*但如果有很多类似`show_nums()`的函数都需要进行这样的处理，作者`A`该怎么办？逐个修改所有的这些函数似乎有点儿麻烦，而且有很多重复的代码*。因此，直接修改`show_nums()`函数的方案不可取。

### 假方案
作者`A`可以重新定义一个函数`add_try_except(func)`，将函数`show_nums()`作为参数传递给它，然后在`add_try_except(func)`中调用`show_nums()`。这样，就达到了不改动`show_nums()`函数的目的。按照这种思路，重写上述的`utils.py`文件。
修改后的`utils.py`文件内容：
```python
#!/usr/bin/env python
#File Name: utils.py
#Author: A

def show_nums():
    print([i for i in range(10)])
    # some code that may throw exception

def add_try_except(func):
    try:
        func()
    except Exception as e:
        traceback.print_exc()
```
但此时显然需要通知`run.py`的作者`B`:`show_nums()`函数更新了，新的调用方法是`add_try_except(show_nums)`。然后作者`B`在`run.py`将所有`show_nums()`的调用修改为`add_try_except(show_nums)`（如果有其他类似的函数，`B`也需要进行相应的修改）。
**这种方案显然也是不可取的**，虽然作者`A`不用逐个修改所有的这些函数。**然而**，每次`A`对函数进行升级后，需要`B`做大量的修改工作。

### 一种方案
如果不修改调用代码（作者`B`的代码），也就意味着调用`show_nums()`函数需要产生调用`add_try_except(show_nums)`的效果。我们可以想到将`add_try_except(show_nums)`赋值给`show_nums`，**这就需要`add_try_except(show_nums)`不是直接产生调用效果，而是返回一个与`show_nums`参数列表一致的函数([闭包](https://segmentfault.com/a/1190000002965736))。**并且，这样能够保证调用`show_nums()`函数的代码完全不用修改！
重写上述的`utils.py`文件：
```python
#!/usr/bin/env python
#File Name: utils.py
#Author: A

def show_nums():
    print([i for i in range(10)])
    # some code that may throw exception


def add_try_except(func):
    def _func():
        try:
            print("in decorator.")
            func()
        except Exception as e:
            traceback.print_exc()

    return _func

show_nums = add_try_except(show_nums)
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

def add_try_except(func):
    def _func():
        try:
            print("in @ decorator.")
            func()
        except Exception as e:
            traceback.print_exc()
    return _func


@add_try_except
def show_nums():
    print([i for i in range(10)])
    # some code that may throw exception
```
在上述代码中，第一个函数`add_try_except`就是装饰函数，它的参数就是被装饰的函数对象。我们可以在`add_try_except`函数内对传入的函数对象做一番“装饰”，然后返回这个对象（**一定要返回 ，不然外面调用func的地方将会无函数可用**）。
利用装饰器，只要在函数定义的上面加上`@decorator_func_name`，而不用修改函数调用的地方。同时，原来的函数内的代码也不用改动。
如果有很多类似于`show_nums()`的函数需要进行同样的处理，那么这些函数的定义处也需要增加`@decorator_func_name`语句，看起来工作量不少，但相比于在所有的函数调用处进行修改，显然是要合理有效得多。
装饰器的确可以在`简化代码`、`重用代码`方面提供非常大的帮助。
