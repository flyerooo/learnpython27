#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/2 0:29

username = 'canglaoshi'

while True:
    s = raw_input("请输入用户名（按q退出）：")
    if s == username:
        print "用户名正确"
        break
    elif s == 'q':
        break
    else:
        print "用户名不正确"
