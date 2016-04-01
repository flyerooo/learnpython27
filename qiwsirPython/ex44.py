#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/27 17:08
# 44、在网上搜索一篇英文的文章，至少要有500个以上的词汇量。然后
# （1）统计这篇文章有多少个不重复的单词。186
# （2）每个单词的出现次数。/242

import re
import requests
from bs4 import BeautifulSoup

#get  web article
def getArticle():
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    string = requests.get(r'http://www.wired.co.uk/magazine/archive/2012/04/features/inside-the-clone-factory',headers=headers)
    soup = BeautifulSoup(string.text,'html.parser',from_encoding='utf8')
    return soup.get_text()

#word count
def wordCount(article):
    wordcounts ={}
    wordlist = re.findall(r"\b\w+'?\w+\b",article)
    for word in wordlist:
        if word in wordcounts:
            wordcounts[word] += 1
        else:
            wordcounts[word] = 1
    return wordcounts

#word sort
def wordSort(wordcounts):
    pairs = list(wordcounts.items())
    items = [(x,y) for (y,x) in pairs]
    items.sort()
    for i in range(len(items)-1,0,-1):
        print items[i][1] + '\t' + str(items[i][0])

if __name__ == "__main__":
    article = getArticle()
    print "Total number of words: ",len(wordCount(article))
    wordSort(wordCount(article))
#文章内容有部分匹配的有问题，但不知道怎么去掉