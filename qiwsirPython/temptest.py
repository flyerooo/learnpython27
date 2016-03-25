#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/22 18:24

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b ,a + b
    return a
for i in range(20):
    print fib(i),