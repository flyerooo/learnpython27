#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/5 15:57

# 52、编写类，实现计算两个分数的加法的功能。
# 注意，这个类，需要用到类的特殊方法，相关内容，不知道你是否已经学习过。
# 如果没有，可以查看官方文档中的内容

from fractions import Fraction
class Add(object):
    def __init__(self,a,b):
        self.a = Fraction(a)
        self.b = Fraction(b)
    def add(self):
        return self.a + self.b

if __name__ == "__main__":
    f = Add('1/2','1/3')
    print f.add()
