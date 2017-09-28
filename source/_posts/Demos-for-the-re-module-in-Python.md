---
title: Demos for the "re" module in Python
date: 2017-09-21 14:06:56
tags: [re, Python]
categories: [re, Python]
---

1.正则表达式修饰符 - 可选标志

| 修饰符 | 描述 |
| --- | --- |
| re.I | 使匹配对大小写不敏感 |
| re.M | 多行匹配，影响^和$ |
| re.S | 使.匹配包括换行在内的所有字符 |
| re.U | 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B |
| re.X | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解 |

2.
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
由于正则表达式通常都包含反斜杠，所以最好使用原始字符串来表示它们。模式元素(如 `r'\t'`，等价于 `'\\t'`)匹配相应的特殊字符。

3.正则表达式模式

| 模式 | 描述 |
| --- | --- |
| \w | 匹配字母数字及下划线 |
| \W | 匹配非字母数字及下划线 |
| \s | 匹配任意空白字符，等价于 [\t\r\n\f\v] |
| \S | 匹配任意非空字符 |
| \1...\9 | 匹配第n个分组的内容 |


4.re实例
```python
#!/usr/bin/env python3
# coding: utf-8
# File: re_demo.py
# Author: lxw
# Date: 9/21/17 11:24 AM
# Reference: http://www.runoob.com/python/python-reg-expressions.html


import re

def main():
    string = "hello, lxw. My name is 刘晓伟."

    # re.match() -----------------------------------------------------------------------------------
    # re.match(pattern, string, flags=0): re.match 尝试从字符串的**起始位置**匹配一个模式，**如果不是起始位置匹配成功的话，match()就返回none**。
    print("re.match():")
    # Method 1
    pattern = re.compile("\S*")    # type(pattern): <class '_sre.SRE_Pattern'>
    match_obj = re.match(pattern, string)    # type(match_obj): <class '_sre.SRE_Match'>

    # Method 2:
    match_obj = re.match(r"\S*", string)

    print(match_obj)    # <_sre.SRE_Match object; span=(0, 6), match='hello,'
    print(match_obj.span())    # (0, 6)
    print(match_obj.group())    # hello,
    print(match_obj.group(0))    # hello,
    # print(match_obj.group(1))    # IndexError: no such group

    # Group ---------------------------------------------------------------------------------------
    print("\nmatch_obj.group()")
    match_obj = re.match(r"(.*) lxw.*is (.*?)\.", string)
    if match_obj:
        print(match_obj.group())    # "hello, lxw. My name is 刘晓伟."
        print(match_obj.group(0))    # "hello, lxw. My name is 刘晓伟."
        print(match_obj.group(1))    # "hello,"
        print(match_obj.group(2))    # "刘晓伟"
        """
        match_obj.group() 等同于 match_obj.group(0)，表示匹配到的完整文本字符
        match_obj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
        match_obj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的
        因为只有匹配结果中只有两组，所以如果填 3 时会报错。
        """
    else:
        print("No match")

    # re.search() ----------------------------------------------------------------------------------
    # re.search(pattern, string, flags=0): re.search 扫描整个字符串并返回第一个成功的匹配。
    print("\nre.search():")
    match_obj =  re.search("\W+", string)    # type(match_obj): <class '_sre.SRE_Match'>
    print(match_obj.span())
    print(match_obj.group())
    print(match_obj.group(0))
    # print(match_obj.group(1))
    print(match_obj.groups())    # ()

    # difference between re.match() and re.search()------------------------------------------------
    """
    re.match与re.search的区别:
    re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    而re.search匹配整个字符串，直到找到**一个**匹配。
    """
    print("\nDifference between re.match() and re.search():")
    match_obj = re.match(r"lxw", string)
    if match_obj:
        print("re.match()->match_obj.group():", match_obj.group())
    else:
        print("re.match()->No match")

    match_obj = re.search(r"lxw", string)    # match_obj: <_sre.SRE_Match object; span=(7, 10), match='lxw'>
    if match_obj:
        print("re.search()->match_obj.group():", match_obj.group())
    else:
        print("re.search()->No match")

    # re.sub() ------------------------------------------------------------------------------------
    # re.sub(pattern, repl, string, count=0, flags=0): re.sub用于替换字符串中的匹配项
    print("\nre.sub():")
    new_string = re.sub(r"\W", "|", string)
    print(new_string)    # hello||lxw||My|name|is|刘晓伟|

    # repl 参数是一个函数
    def double(matched):
        # value = int(matched.group("val"))
        # value = str(matched.group("val"))    # OK
        value = matched.group("val")    # OK
        return str(value * 2)
    print(re.sub(r"(?P<val>\W+)", double, string))    # hello, , lxw. . My  name  is  刘晓伟.

    # 正则表达式模式
    target_string = "hello, lxw. My name is 刘晓伟."
    pattern_str = "\Ahello.*\Z"
    match_obj = re.search(pattern=pattern_str, string=target_string)
    if match_obj:
        print(match_obj)


def unicode_demo():
    string = "abcde 陕西省西安市dhshg雁塔区abbvcd"

    pattern = re.compile(r"[\u4e00-\u9fa5]+")    # OK
    # pattern = re.compile(r"[\u4e00-\u9fa5]*")    # NO, WHY???
    # pattern = re.compile(r"[a-z]*")
    # match_obj = pattern.search(string)
    match_obj = re.search(pattern, string)
    if match_obj:
        print("|{}|".format(match_obj))
        print("|{}|".format(match_obj.group()))
        print("|{}|".format(match_obj.group(0)))

    # match
    print("re.match()")
    match_obj = pattern.match(string)
    print("|{}|".format(match_obj))
    if match_obj:
        # print(match_obj.groups())  # NO
        print("|{}|".format(match_obj.group()))
        print("|{}|".format(match_obj.group(0)))


if __name__ == "__main__":
    main()
    # unicode_demo()
```