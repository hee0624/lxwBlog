---
title: scrapy learning notes
date: 2017-04-12 16:22:30
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

4.使用Selenium(PhantomJS/Chrome)进行数据爬取时，如果使用User-Agent池，那么User-Agent Middleware的优先级必须要比Selenium的优先级高，否则User-Agent无法加到Selenium的请求中
[fintech_spider/demo/PhantomJSTests/PhantomJSScrapy/PhantomJSScrapy/settings.py](https://github.com/hee0624/fintech_spider/blob/master/demo/PhantomJSTests/PhantomJSScrapy/PhantomJSScrapy/settings.py)

5.
+ yield重复的GET请求，Scrapy会将其自动过滤掉
+ yield重复的POST请求(完全相同的POST请求:URL和参数都相同)也会被Scrapy自动过滤掉; 不同的POST body不会被Scrapy过滤掉

6.
1).XPath解析：  
html网页源文件中各个标签的id属性必须是唯一的（但对于不规范的网页来说，id相同也是有可能的）  
class通常都是不唯一的，如果要用class需要在源代码中检索一下  
所以使用XPath进行定位时，一般先定位到一个离目标标签最近的具有id属性的父级标签(包括但不局限于div标签)然后再通过该标签定位到目标标签  
2).可以把“右键->查看网页源代码”的源代码拷贝到sublime或者pycharm，就可以折叠代码了  
3).[注意事项][Scrapy使用以及Xpath的一些坑, 再入剁手]  
如果在某个xpath对象下继续使用xpath规则提取, 当提取某个对象下的所有tr标签.
```python
html = response.xpath("/html/body")
tr = html.xpath(".//tr") #搜索body下的所有tr必须加上'.', 否则搜索的是整个文档的所有tr
```

7.scrapy shell url  
注意利用view(response)在浏览器中观察爬虫看到的网页是否和我们看到的网页一样，其实大部分都是不相同的。  

8.CSS selector:  

|表达式|说明|
|---|---|
|*|选择所有节点|
|#container|选择id为container的节点|
|.container|选择所有class**包含**container的节点|
|li a|选取所有li下的所有a节点(li和a是父子节点)|
|ul + p|选取ul后面的第一个p节点(ul和p是兄弟节点)|
|div#container > ul|选取id为container的div节点下的**第一个**ul子节点|
|ul ~ p|选取与ul相邻的所有p节点|
|a[title]|选取所有有title属性的a节点|
|a[href="http://jobbole.com"]|选取所有href属性值为"http://jobbole.com"的a节点|
|a[href*="jobbole"]|选取所有href属性值包含"jobbole"的a节点|
|a[href^="http"]|选取所有href属性值以"http"开头的a节点|
|a[href$=".jpg"]|选取所有href属性值以".jpg"结尾的a节点|
|input[type=radio]:checked|选取状态为选中的radio节点|
|div:not(#container)|选取所有id不为container的div节点|
|li:nth-child(3)|选取第三个li节点|
|tr:nth-child(2n)|选取第偶数个tr|

### FAQs
1.[scrapy爬虫防止被禁止User-Agent切换](http://blog.csdn.net/haipengdai/article/details/48545231)
2.[Python下用Scrapy和MongoDB构建爬虫系统(1)](http://python.jobbole.com/81320/)
3.[讲解Python的Scrapy爬虫框架使用代理进行采集的方法](http://www.jb51.net/article/79666.htm)
4.
`Spider` - a browser like program that downloads web pages.
`Crawler` – a program that automatically follows all of the links on each web page.
Robots - An automated computer program that visit websites & perform predefined task.

`Crawler(scrapy.crawler)` is the main entry point to Scrapy API. It provides access to all Scrapy core components, and it's used to hook extensions functionality into Scrapy.
`Scraper(scrapy.core.scraper)` component is responsible for parsing responses and extracting information from them. It's being run from the Engine, and it's used to run your spiders.
`scrapy.spiders` is a module containing base Spider implementation (that you use to write your spiders), together with some common spiders available out of the box (like the CrawlSpider for ruleset-based crawling, the SitemapSpider for sitemap based crawling, or XMLFeedSpider for crawling the XML feeds).

[what is difference between spider, crawler and robots?](http://www.webdeveloper.com/forum/showthread.php?278773-what-is-difference-between-spider-crawler-and-robots)
[Difference between scraper, crawler and spider in the context of Scrapy](http://stackoverflow.com/questions/34260886/difference-between-scraper-crawler-and-spider-in-the-context-of-scrapy)



<!--References-->
[Scrapy Tutorial]: https://docs.scrapy.org/en/latest/intro/tutorial.html
[Scrapy使用以及Xpath的一些坑, 再入剁手]: http://www.cnblogs.com/Bright-Star/p/4163107.html?utm_source=tuicool&utm_medium=referral
