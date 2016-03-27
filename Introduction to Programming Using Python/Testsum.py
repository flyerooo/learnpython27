#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/25 10:34

sum = 0
i = 0.01
while i < 1.0:
    sum += i
    i +=0.01
print "The sum is",sum

"以上程序是有问题的，注意这种最小化数值错误"