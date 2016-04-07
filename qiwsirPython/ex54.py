#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/5 15:57

# 54、编写一个生成器函数，实现斐波那契数列。
def fibs(max):
    n, a,b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

if __name__ == "__main__":
    f= fibs(10)
    for i in f:
        print i,