#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 23:19
# 39、自己创建一个比较大的文本文件，写一个逐页访问该文本文件的程序。要求提示输入文件名，然后显示该文件内容，
# 每次显示10行，并提示用户“按任意键继续”，按键后继续。

import sys

input_file = raw_input("Enter a file: ",)
with open(input_file, 'r') as f:
    for num,line in enumerate(f, start=1):
        print line,
        if num % 10 == 0:
            prompt = raw_input("--------Press any key to continue,press Q to quit---------")
            if prompt.lower() == 'q':
                sys.exit()
#测试了4M的文本文件，没什么发现什么问题