#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/5 15:57
# 55、应用os模块，对存储在计算机内的文件依次进行如下操作，并将操作过程和结果记录下来（作业提交内容就是记录指令和结果）
# 对文件重命名
# 删除文件
# 显示目录中的文件
# 改变当前工作目录
# 创建目录
# 删除目录
# 查看某文件属性
# 打开浏览器
# 如果完成有困难，可以参考《跟老齐学Python》的第6章，254页内容。

import os
#1 rename
# os.renames('ex54.py','ex54-test.py')

#2 delete file
# os.remove('teacher_cang.txt')

#3 List files in directory
# os.listdir(r'D:\learnpython27')

#4 change working directory
# os.chdir(r'D:\learnpython27\teachers')
# os.getcwd() #Return current working directory

#5 Create directory
# os.mkdir(r'D:\learnpython27\teachers')

#6 Remove directory
# os.rmdir(r'D:\learnpython27\teachers')

#7 Get file attributes
# os.stat(r'D:\learnpython27\ex15.py')

#8 Open explore
os.startfile(r"C:\Program Files (x86)\Internet Explorer\iexplore.exe")