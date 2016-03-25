#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 20:33


def copyFile(in_file, out_file):
    with open(in_file,'r') as f1:
        with open(out_file,'w') as f2:
            for line in f1:
                f2.write(line)

if  __name__ == "__main__":
    import sys
    copyFile(sys.argv[1], sys.argv[2])


