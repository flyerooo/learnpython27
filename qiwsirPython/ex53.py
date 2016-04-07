#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/5 15:57

# 53、编写迭代器，实现斐波那契数列。

class Fibs(object):
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == "__main__":
    fibs = Fibs(10)
    print list(fibs)