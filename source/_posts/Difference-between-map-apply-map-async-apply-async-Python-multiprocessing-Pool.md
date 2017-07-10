---
title: Difference between map, apply, map_async, apply_async(Python multiprocessing.Pool)
date: 2017-07-04 09:39:02
tags: [multiprocessing, Python]
categories: [multiprocessing, Python]
---

在`multiprocessing.Pool`中有4种方法可以用来将任务分给到各个子进程，分别是`apply`，`apply_async`，`map`，`map_async`，4种方法的对比请见下表([原文中的表][apply_apply_async_map_map_async])：

||Multi-args|**Concurrence**|Blocking|Ordered-results|
|------|------|------|------|------|
|apply|YES|**NO**|YES|NO|
|apply_async|YES|YES|NO|**NO**|
|map|NO|YES|YES|**YES**|
|map_async|NO|YES|NO|**YES**|
需要说明的是，最后一列`Ordered-results`表示各个方法**返回的结果**是否是有序的，而不是执行的顺序。也就是说（以下面的程序为例）不是表示程序中`print`语句的执行顺序是否有序（`print`的结果不一定有序），而是表示**各个函数的返回值是否是按照_调用的顺序_返回的**。

对4种方法分别进行了下面的测试，测试代码如下：

```python
import multiprocessing
# import sys
import time

def func(num):
    print(num, end=" ", flush=True)    # 增加flush=True才能体现出多进程和进程池
    # sys.stdout.flush()    # 增加这条语句才能体现出多进程和进程池
    time.sleep(1)

results = []

def collect_result(result):    # 只能带一个参数
    results.append(result)

def authors_code():
    """
    带返回值的多进程
    """
    global results
    COUNT = 20
    print("\napply", "--" * 20)
    t = time.time()
    results = []
    with multiprocessing.Pool(5) as pool:
        for i in range(COUNT, 0, -1):
            results.append(pool.apply(func, (i,)))  # 不是多进程
    print("\n{}".format(results))
    print("apply:", time.time() - t, "\n")

    print("\napply_async", "--" * 20)
    t = time.time()
    results = []
    with multiprocessing.Pool(5) as pool:
        for i in range(COUNT, 0, -1):
            pool.apply_async(func, (i,), callback=collect_result)  # 多进程, callback
        pool.close()
        pool.join()
    print("\n{}".format(results))
    print("apply_async:", time.time() - t, "\n")

    print("\nmap", "--" * 20)
    t = time.time()
    with multiprocessing.Pool(5) as pool:
        results = pool.map(func, range(COUNT, 0, -1))
        pool.close()
    print("\n{}".format(results))
    print("map:", time.time() - t, "\n")
    """
    20 19 17 16 18 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1   # NOTE: print的结果是无序的
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1  # NOTE: 但返回的结果是有序的]
    """

    print("\nmap_async", "--" * 20)
    t = time.time()
    results = []
    with multiprocessing.Pool(5) as pool:
        pool.map_async(func, range(COUNT, 0, -1), callback=collect_result)  # 多进程
        pool.close()
        pool.join()
    print("\n{}".format(results))
    print("map_async:", time.time() - t, "\n")

    print('end')

if __name__ == "__main__":
    authors_code()
```
代码运行结果如下：
```bash
apply ----------------------------------------
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
apply: 20.073657989501953


apply_async ----------------------------------------
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1    # 有序
[19, 17, 20, 18, 16, 15, 14, 13, 11, 12, 9, 10, 7, 8, 6, 3, 5, 4, 2, 1]    # 无序
apply_async: 4.017202854156494


map ----------------------------------------
20 19 17 16 18 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1    # 无序
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]    # 有序
map: 4.1325297355651855


map_async ----------------------------------------
20 18 17 16 19 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1    # 无序
[[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]    # 有序
map_async: 4.0203177928924568

end
```

<!-- Reference -->
[apply_apply_async_map_map_async]: http://blog.shenwei.me/python-multiprocessing-pool-difference-between-map-apply-map_async-apply_async/
