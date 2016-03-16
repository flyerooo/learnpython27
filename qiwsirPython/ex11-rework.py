#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/6 19:02

with open("teacher_cang.txt",'r') as f:
    newline = []
    for line in f:
        newline.extend(line.replace('love', 'hate')) #这种情况用extend()和append()没发现区别，请问建议使用哪种？
with open("teacher_cang2.txt",'w') as f1:
    f1.writelines(newline)