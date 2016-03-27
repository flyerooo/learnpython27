#! /usr/bin/env python
#coding:utf-8
#!/usr/bin/env python

import re
f = open('who.txt','r')
for eachLine in f.readlines():
    print re.split('\s\s+', eachLine)
f.close()