#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/25 8:22


import urllib2
if __name__ == "__main__":
    # send request
    url = "http://www.itdiffer.com/"
    request = urllib2.Request(url =url)
    # receiver reponse
    response = urllib2.urlopen(request)
    print response.read()