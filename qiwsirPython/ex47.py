#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/27 17:08

import os

def ensureDirectory(directory):
    if os.path.exists(directory):
        print directory,"exists"
    else:
        os.makedirs(directory)
if __name__ == "__main__":
    directory = raw_input("Enter a directory: ").strip()
    ensureDirectory(directory)
