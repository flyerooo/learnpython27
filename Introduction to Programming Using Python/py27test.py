#! /usr/bin/env python
#coding:utf-8
#!/usr/bin/env python

import re
import urllib2
req = urllib2.urlopen("http://www.imooc.com/course/list")
buf = req.read()
# print buf
listurl = re.findall(r'http:.+\.jpg',buf)
i = 0
for url in listurl:
    f = open(str(i)+'.jpg','wb')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1
