#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 20:33
# 42、编写一段程序，抓取www.itdiffer.com首页的内容。


import urllib2

if __name__ == "__main__":
    # send request
    url = "http://www.itdiffer.com/"
    request = urllib2.Request(url =url)
    # receiver reponse
    response = urllib2.urlopen(request)
    print response.read()