#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/15 11:34

def wordNumber(string):
    return string[:140]
string = raw_input("请输入微博内容")
print wordNumber(string)