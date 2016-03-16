#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/3 11:13

# 1、准备文本文件(.txt)，内容如下：
# You love canglaoshi.
# I love canglaoshi, too.
# we all love canglaoshi.
# 读取此文本，并输入每一行，但是，在输出的时候，将love替换为hate，同时将替换之后的内容，写入到一个新的文本文件中。

import os.path
import sys
def main():
    while True:
        try:
            filename = raw_input("请输入文件名").strip()
            f1 = open(filename, 'r')
            break
        except IOError:
            print "文件不存在,重新输入"
    #判断是否已经存在同名文件
    if os.path.isfile("teacher_cang2.txt"):
        print "teacher_cang2.txt exists"
        sys.exit()
    f2 = open('teacher_cang2.txt', 'w')
    #逐行读取文本并把love替换为hate，写入f2
    for line in f1:
        print line,
        newline = line.replace('love','hate')
        f2.write(newline)
    f1.close()
    f2.close()
main()