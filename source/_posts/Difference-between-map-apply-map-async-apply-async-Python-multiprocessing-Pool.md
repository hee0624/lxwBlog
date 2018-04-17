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
1. 需要说明的是，最后一列`Ordered-results`表示各个方法**返回的结果**是否是有序的。也就是说(以下面的程序为例)不是表示程序中`print`语句的执行顺序是否有序(`print`的结果不一定有序)，而是表示**各个函数的返回值是否是按照_调用的顺序_返回的**。
2. Note that `map` and `map_async` are called for a list of jobs in one time, but `apply` and `apply_async` can only called for one job. However, `apply_async` execute a job in background therefore in parallel.

对4种方法分别进行了下面的测试，测试代码如下：

```python
def func(num):
    # print("[func()]pid:", os.getpid())
    print(num, end=" ", flush=True)    # 增加flush=True才能体现出多进程和进程池
    # sys.stdout.flush()    # 增加这条语句才能体现出多进程和进程池
    # time.sleep(0.5)
    return num


results = []


def collect_result(result):    # NOTE: 只能带一个参数
    global results
    # print("[collect_result()]pid:", os.getpid())
    results.append(result)


def apply_map_async_demo():
    """
    带返回值的多进程
    """
    COUNT = 20

    print("\napply", "--" * 20)
    t = time.time()
    local_results = []
    with multiprocessing.Pool(5) as pool:
        for i in range(COUNT, 0, -1):
            # NOTE: pool.apply不支持并发: 但多个进程串行地执行每个任务(仍然是多进程执行)
            local_results.append(pool.apply(func, (i,)))
        pool.close()
    print("\n{}".format(local_results))
    print("apply time cost:", time.time() - t, "\n", "**"*30)

    print("\napply_async", "--" * 20)
    t = time.time()
    with multiprocessing.Pool(5) as pool:
        for i in range(COUNT, 0, -1):
            pool.apply_async(func, (i,), callback=collect_result)    # 并发. callback是可选的, 可以不使用该字段
        pool.close()
        pool.join()
    global results
    print("\n{}".format(results))
    """
    # NOTE: print的结果是无序的 
    20 19 18 17 16 14 13 15 12 11 10 9 7 6 8 5 4 3 2 1
    # NOTE: 返回的结果也是无序的(apply_async不保证返回值的顺序)
    [20, 18, 19, 16, 17, 14, 13, 12, 11, 10, 9, 7, 6, 5, 4, 3, 15, 2, 8, 1]
    """
    print("apply_async time cost:", time.time() - t, "\n", "**"*30)

    print("\nmap", "--" * 20)
    t = time.time()
    with multiprocessing.Pool(5) as pool:
        results = pool.map(func, range(COUNT, 0, -1))    # 并发
        pool.close()
    print("\n{}".format(results))
    """
    # NOTE: print的结果是无序的
    20 19 17 16 18 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
    # NOTE: 但返回的结果是有序的(map能够保证返回值的顺序按照函数调用的顺序)
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    print("map:", time.time() - t, "\n", "**"*30)

    print("\nmap_async", "--" * 20)
    t = time.time()
    results = []
    with multiprocessing.Pool(5) as pool:
        pool.map_async(func, range(COUNT, 0, -1), callback=collect_result)    # 并发. callback是可选的, 可以不使用该字段
        pool.close()
        pool.join()
    print("\n{}".format(results))
    """
    # NOTE: print的结果是无序的
    20 19 17 18 16 15 13 14 10 12 9 8 7 6 11 5 4 3 2 1 
    # NOTE: 但返回的结果是有序的(map_async能够保证返回值的顺序按照函数调用的顺序)
    # map和map_async的结果是以list的形式返回的, 所以只会调用collect_result一次，因此结果是list of list
    [[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
    """
    print("map_async:", time.time() - t, "\n", "**"*30)

    print("end")


if __name__ == "__main__":
    apply_map_async_demo()
```
代码运行结果如下：
```bash
apply ----------------------------------------
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1    # 不保证有序
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]    # 不保证有序
apply time cost: 0.13375353813171387 
 ************************************************************

apply_async ----------------------------------------
20 19 18 17 16 14 13 15 12 11 10 9 7 6 8 5 4 3 2 1    # 无序
[20, 18, 19, 16, 17, 14, 13, 12, 11, 10, 9, 7, 6, 5, 4, 3, 15, 2, 8, 1]    # 无序
apply_async time cost: 0.10675978660583496 
 ************************************************************

map ----------------------------------------
20 19 17 16 18 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1    # 无序
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]    # 有序
map: 0.10820269584655762 
 ************************************************************

map_async ----------------------------------------
20 19 17 18 16 15 13 14 10 12 9 8 7 6 11 5 4 3 2 1    # 无序
[[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]    # 有序
map_async: 0.11021280288696289 
 ************************************************************
end
```

<!-- Reference -->
[apply_apply_async_map_map_async]: http://blog.shenwei.me/python-multiprocessing-pool-difference-between-map-apply-map_async-apply_async/
