---
title: '[Python3.6.*]Scrapy安装和使用'
date: 2017-04-10 15:23:03
tags: [Python, Spider, Scrapy]
categories: [Python, Spider, Scrapy]
---

> Don't use the `python-scrapy` package provided by Ubuntu, they are typically **too old and slow** to catch up with latest Scrapy.
>

本文所使用的`Scrapy`安装环境如下:
**OS**: Ubuntu 16.04 Desktop 64bits
**Python Version**: 3.6.1

### 安装
1.直接按照[Scrapy的安装文档][Installation guide](`pip install Scrapy`)进行安装，并运行quotesSpider.py程序后，出现了下面的错误信息：
```bash
Could not find a version that satisfies the requirement Twisted>=13.1.0 (from scrapy) (from versions: )
No matching distribution found for Twisted>=13.1.0 (from scrapy)
```
经[网上][stackoverflow-scrapy-twisted]查阅，发现是`Python3.6.*`在编译安装之前没有安装`libbz2-dev`。
详细的说明和解决方案在[这里](http://stackoverflow.com/questions/12806122/missing-python-bz2-module)： 简单说就是安装`libbz2-dev`(`sudo apt-get install libbz2-dev`)，然后重新编译安装`Python3.6.*`。
2.完成步骤1之后，运行quotesSpider.py程序，又出现了下面的错误：
```bash
ImportError: No module named _sqlite3
```
经[网上](http://stackoverflow.com/questions/1210664/no-module-named-sqlite3)查阅，发现还是`Python3.6.*`的问题，需要先安装`libsqlite3-dev`(`sudo apt-get install libsqlite3-dev`)，然后重新编译安装`Python3.6.*`。

应该可以在第1步和第2步都安装完成之后，再统一重新编译安装`Python3.6.*`(每次编译安装的时间比较长)。

### 示例代码(`quotesSpider.py`)
解决上面的两个问题之后，就可以正确运行quotesSpider.py程序了，具体的源代码如下。
```Python
#!/usr/bin/env python3
# coding: utf-8
# File: quotesSpider.py
# Author: lxw
# Date: 4/15/17 9:22 PM

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/tag/humor/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract_first(),
                "author": quote.css("span small.author::text").extract_first(),
            }
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
```

**运行**：
```bash
(py3.6.1scrapy1.3.3) lxw@lxw(00:05:04)scrapyDemo$ scrapy runspider quotesSpider.py -
o quotes.json
```

### References
[How Can I install Twisted + Scrapy on Python3.6 and CentOs][stackoverflow-scrapy-twisted]
[Installation guide][Installation guide]

[stackoverflow-scrapy-twisted]: http://stackoverflow.com/questions/42230070/how-can-i-install-twisted-scrapy-on-python3-6-and-centos/42239833#42239833
[Installation guide]: https://docs.scrapy.org/en/latest/intro/install.html
