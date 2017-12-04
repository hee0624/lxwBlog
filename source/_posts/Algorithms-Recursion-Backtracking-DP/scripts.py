#!/usr/bin/env python3
# coding: utf-8
# File: scripts.py
# Author: lxw
# Date: 12/4/17 10:25 AM

import turtle as tl

def recursion_fibonacci(n):
    """
    # Fibonacci
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
    
    f(1) = 1
    f(2) = 1
    f(3) = f(2) + f(1)
    f(n) = f(n-1) + f(n-2)
    """
    if n < 3:
        return 1
    return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)


def iterative_fibonacci(n):
    if n < 3:
        return 1
    a = 1
    b = 1
    while n > 2:
        b = a + b
        a = b - a
        n -= 1
    return b




def main():
    print(recursion_fibonacci(13))
    print(iterative_fibonacci(13))


if __name__ == '__main__':
    main()