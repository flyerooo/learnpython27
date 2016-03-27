#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/25 9:29

data = eval(raw_input("Enter an inter (the input ends" + "if it is 0): "))
sum = 0
while data != 0:
    sum += data
    data = eval(raw_input("Enter an inter (the input ends" + "if it is 0): "))
print "The sum is,",sum