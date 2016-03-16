#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/6 20:43

# 9、x>1，求最大整数k，使得2^k（2的k次幂）小于等于x
import math

x = float(raw_input("请输入大于1的数"))
if x > 1:
    k = int(math.log(x, 2))
    print "最大整数为",k
else:
    "输入错误"
