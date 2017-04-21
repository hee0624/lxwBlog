---
title: scrapy learning notes
date: 2017-04-16 16:22:30
tags: [Python, Scrapy, Spider]
categories: [Python, Scrapy, Spider]
---

### Scrapy 1.3 documentation
1.
> XPath expressions are very powerful, and are the foundation of Scrapy Selectors. **In fact, CSS selectors are converted to XPath under-the-hood.**
[Scrapy Tutorial-XPath: a brief intro](https://docs.scrapy.org/en/latest/intro/tutorial.html#xpath-a-brief-intro)

2.
> What you see here is Scrapy’s mechanism of following links: when you yield a Request in a callback method, Scrapy will schedule that request to be sent and register a callback method to be executed when that request finishes.
[Scrapy Tutorial-Following links](https://docs.scrapy.org/en/latest/intro/tutorial.html#following-links)

3.
> Another interesting thing this spider demonstrates is that, even if there are many quotes from the same author, we don’t need to worry about visiting the same author page multiple times. **By default, Scrapy filters out duplicated requests to URLs already visited, avoiding the problem of hitting servers too much because of a programming mistake. This can be configured by the setting DUPEFILTER_CLASS.**
[Scrapy Tutorial-More examples and patterns](https://docs.scrapy.org/en/latest/intro/tutorial.html#more-examples-and-patterns)

### FAQs
1.[scrapy爬虫防止被禁止User-Agent切换](http://blog.csdn.net/haipengdai/article/details/48545231)
2.[Python下用Scrapy和MongoDB构建爬虫系统(1)](http://python.jobbole.com/81320/)


<!--References-->
[Scrapy Tutorial]: https://docs.scrapy.org/en/latest/intro/tutorial.html
