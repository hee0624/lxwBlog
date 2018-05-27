---
title: Python模块和包
date: 2017-10-27 14:11:43
tags: [Python]
categories: [Python]
---

1. Python的程序由包(package)、模块(module)和函数组成。包是由一系列模块组成的集合。模块是处理某一类问题的函数和类的集合, 使用模块可以避免函数名和变量名冲突(不同模块可以使用相同的函数名和变量名)
2. 包必须至少含有一个`__init__.py`文件，该文件的内容可以为空。`__init__.py`用于标识当前文件夹是一个包
3. 一个文件即是一个模块。创建一个名为`my_module.py`的文件，即定义了一个名为`my_module`的模块
4. 当Python导入一个模块时，Python**首先查找当前路径**，然后查找lib目录、site-packages目录(python\lib\site-packages)和环境变量PYTHONPATH设置的目录  
 Python会在以下路径中搜索它想要寻找的模块：
 + 程序所在的文件夹
 + 标准库的安装路径
 + 操作系统环境变量PYTHONPATH所包含的路径
5. 将自定义库的路径添加到Python的库路径中去，有如下两种方法:   
 1).动态的添加库路径。在程序运行过程中修改`sys.path`的值，添加自己的库路径  
 ```python
 import sys
 sys.path.append(r'your_path') 
 ```
 2).在Python安装目录下的\lib\site-packages文件夹中建立一个.pth文件，内容为自己写的库路径。示例如下:  
 `E:\\work\\Python\\logging`  
6. **相对路径import**  
 **包含相对路径import的Python脚本不能直接运行**，只能作为module被引用。原因正如手册中描述的，所谓相对路径指的是相对于当前module的路径，但如果直接执行脚本，这个module的name就是`"__main__"`, 而不是module原来的name，这样相对路径也就不是原来的相对路径了，导入就会失败，出现错误“ValueError: Attempted relative import in non-package”
 > Note that relative imports are based on the name of the current module. Since the name of the main module is always `"__main__"`, modules intended for use as the main module of a Python application **must** always use absolute imports.

 **Reference:**  
 + [python import相对路径](https://blog.csdn.net/cugb1004101218/article/details/38892809)
 + [Modules](https://docs.python.org/3.6/tutorial/modules.html)