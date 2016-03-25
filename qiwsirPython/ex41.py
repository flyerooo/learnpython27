#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 20:33

import gzip

def compress(file_in,file_out):
    with open(file_in,'rb') as f1:
        with gzip.open(file_out,'wb') as f2:
            f2.writelines(f1)
def decompress(zip_file,plain_file):
    with gzip.open(zip_file,'rb') as f1:
        with open(plain_file,'wb') as f2:
            f2.writelines(f1)
if __name__ =="__main__":
    compress('ex42.py','test.gz')
    decompress('test.gz','test1.py')

