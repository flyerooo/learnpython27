#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/9 10:23

def f(n):
    return int(n + n//6)

n = float(raw_input("请输入买棒棒糖的金额："))
print n, '元共能买', f(n), '棒棒糖'