#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/17 22:20
import random
lst = [random.randint(0,10) fo i in range(11)]
m = {}
for i in lst:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
print m
max_number = max(m.values())
for k,v in m.items():
    if v == max_number:
        print "众数是",k