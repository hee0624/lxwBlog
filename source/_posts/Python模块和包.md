---
title: Python模块和包
date: 2017-10-27 14:11:43
tags: [Python]
categories: [Python]
---

1.
Python的程序由包（package）、模块（module）和函数组成。包是由一系列模块组成的集合。模块是处理某一类问题的函数和类的集合。
2.
包必须至少含有一个__int__.py文件，该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包。
3.
一个文件即是一个模块。创建一个名为"my_module.py"的文件，即定义了一个名为"my_module"的模块。
4.
当Python导入一个模块时，Python**首先查找当前路径**，然后查找lib目录、site-packages目录(Python\Lib\site-packages)和环境变量PYTHONPATH设置的目录。
Python会在以下路径中搜索它想要寻找的模块：
+ 程序所在的文件夹
+ 标准库的安装路径
+ 操作系统环境变量PYTHONPATH所包含的路径
5. 使用模块可以避免函数名和变量名冲突。
6.
将自定义库的路径添加到Python的库路径中去，有如下两种方法：  
1).动态的添加库路径。在程序运行过程中修改sys.path的值，添加自己的库路径  
```python
import sys
sys.path.append(r'your_path') 
```
2).在Python安装目录下的\Lib\site-packages文件夹中建立一个.pth文件，内容为自己写的库路径。示例如下:  
"E":\\work\\Python\\http"  
"E:\\work\\Python\\logging"  






