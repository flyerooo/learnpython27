#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/9 0:02

import datetime

year = int(raw_input("year:"))
month = int(raw_input("month:"))
day = int(raw_input("day:"))
correctDate = None
try:
    newDate = datetime.datetime(year, month, day)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))
#自己判断的话，条件感觉比较多，所以参考了stackoverflow上的回答