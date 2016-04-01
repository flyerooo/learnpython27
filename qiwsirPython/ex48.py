#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/1 21:27

# 48、在Python脚本内部调用外部命令，比如在Unix/Linux shell命令行或者在Windows命令提示符中键入外部命令，能够在Python脚本中使用。
# 比如在Linux中，有列出当前目录下的内容的命令：ls，打算将这个命令写入到Python脚本中，并能够实现操作。
# 如果你的计算机操作系统是windows，也有：dir，实现同样功能的命令。
# 参考：subprocess模块或者os.system


import subprocess

p=subprocess.Popen("dir",shell=True)  #Windows