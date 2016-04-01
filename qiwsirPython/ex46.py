#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/27 17:08
# 46、熟悉CSV模块。并用该模块写一段程序（自己拟定内容），要求使用csv.reader和
# csv.writer。


import csv

with open('your.csv', 'wb')as f:
    writer_file = csv.writer(f)
    writer_file.writerow(['Age', 'Name', 'Language'])
    lines = [range(3) for i in range(5)]
    for line in lines:
        writer_file.writerow(line)

reader_file = csv.reader(file('your.csv', 'rb'))
for line in reader_file:
    print line
