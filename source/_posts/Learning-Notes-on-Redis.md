---
title: Learning Notes on Redis
date: 2017-04-26 09:11:34
tags: [Redis, Database]
categories: [Redis, Database]
---

### Redis Notes
1.Redis中集合是通过`哈希表`实现的，所以添加、删除、查找的复杂度都是O(1)


### Redis命令
1.`keys *`: 查看Redis中所有的key
如果有大量的key, 尽可能不要在生产环境下用`keys`指令, 太占用资源了.
`keys link*`, `keys name*`, `keys n*`
2.
1)Installing redis-dump
```bash
$ [sudo] npm install redis-dump -g
```
Reference: [redis-dump](https://www.npmjs.com/package/redis-dump)
2)`redis-dump -h 192.168.1.29 -p 6379 > 29redis-dump.txt`
3)`cat 29redis-dump.txt|redis-cli`
