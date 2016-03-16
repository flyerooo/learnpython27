#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/1

d = {"name": "python","book": "python", "lang": "english" }
d = dict((value,key) for key,value in d.items())
print d