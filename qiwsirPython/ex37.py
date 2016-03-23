#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 23:18
# 37、文件过滤。读取一个python文件（.py），显示这个文件的所有行的内容以及行数，忽略以#符号开头的行。

with open("ex36.py",'r') as f:
    num = 1
    for line in f:
        if not line.startswith('#'): #skip the comment line
            print num,line,
            num += 1

