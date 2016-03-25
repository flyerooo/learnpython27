#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/25 8:22


import urllib2
if __name__ == "__main__":
    # send request
    url = "http://www.itdiffer.com/"
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    request = urllib2.Request(url =url, headers =headers)
    # receiver reponse
    response = urllib2.urlopen(request)
    print response.read()