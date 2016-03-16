#!/usr/bin/env python
#coding:utf-8

#import urllib
import urllib2
import re
import os
if __name__ == '__main__':
    #设置Request的url信息和头部信息
    print "开始抓取内容了..."
    for i in range(1, 35):

        url = "http://www.qiushibaike.com/textnew/page/"+ str(i) +"/?s=4851189"
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

        pattern = re.compile('<div class="content">(.*?)<!--(.*?)-->.*?</div>', re.S)
        items = re.findall(pattern, content)
        for item in items:
            #item[0] 文本的信息
            #item[1] 时间戳的信息
            #保存之前先去掉多余的换行符，再把<br.替换为/n
            item_new = item[0].replace('\n','').replace('<br/>','\n')
            path = 'qiubai'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + item[1] + '.txt'
            f = open(file_path, 'w')
            f.write(item_new)
            f.close
    print "内容抓取完了"

