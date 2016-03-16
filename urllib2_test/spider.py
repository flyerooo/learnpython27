#!/usr/bin/env python
#coding:utf-8

import urllib2
import re
import os

class Spider(object):


    #构造方法
    def __init__(self):
        self.url =  "http://www.qiushibaike.com/textnew/page/%s?s=4851189"
        self.user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"}
    #获取网页源代码
    def get_page(self, page_index):
        headers ={"User-Agent": self.user_agent}

        try:
            request = urllib2.Request(url = self.url%str(page_index), headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()
    #分析网页源代码
    def analysis(self, content):
        pattern = re.compile('<div class="content">(.*?)<!--(.*?)-->.*?</div>', re.S)
        items = re.findall(pattern, content)
        return items

    #保存抓取的内容
    def save(self, items,path):
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
    #运行的方法
    def run(self):
        print "开始抓取内容了。。。"
        for i in range(1, 35):
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items,'qiubai')
        print "内容抓取完了"
if __name__ == '__main__':
    spider = Spider()
    spider.run()

