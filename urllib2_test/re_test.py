#!/usr/bin/env python
#coding:utf-8

#import urllib
import urllib2
import re
import os

if __name__ == '__main__':
    print "开始抓取内容了..."
    num = 0
    for i in range(1, 21):
        url = "http://www.maiziedu.com/course/teachers/?page=%s"%i
        headers ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"}

        try:
            request = urllib2.Request(url = url, headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()

        pattern = re.compile('<p class="font20 color00 marginB14 t3out p">(.*?)<a href="/group/common/course/.*?/" class="go font12">.*?</a></p>.*?<p class="color66 marginB14"><span class="color99">(.*?)</span></p>.*?<p class="color66"><span class="color99">(.*?)</span>(.*?)</p>', re.S)
        items = re.findall(pattern, content)
        for item in items:
            num += 1
            item_new = "%d %s %s\n%s\n%s\n\n" %(num,item[0],item[1],item[2],item[3])
            path = 'teachersOfMaizi'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + 'infoOfTeachers' + '.txt'
            f = open(file_path, 'a')
            f.write(item_new)
            f.close
    print "内容抓取完了"
