#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/15 11:34

def origami(n):
    thinkness = (2.0 ** n * 1/200) / 100
    return thinkness
n = int(raw_input("请输入折叠次数:"))
print "厚度为",format(origami(n),".2f"),"米"
