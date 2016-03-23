#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/20 9:02
'''
33、回文（palindrome）是正读或者反读都相同的单词或但与，忽略空格和字母大小写。例如，下面的示例都是回文：
warts n straw
radar
Able was I ere I saw Elba
xyzczyx
编写一个程序，判断输入的字符串是否是回文。
'''

def toLetters(string):
    '''remove non letter character '''
    letters = ''
    for c in string:
        if c.isalpha():
            letters += c
    return letters

def isPalindrome(string):

    low = 0 #first letter
    high = len(string) - 1 # last letter
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True

if __name__=="__main__":
    string = raw_input("Enter a string:").lower()
    if isPalindrome(toLetters(string)): #一个函数要调用另一个函数值这么写吗? 对函数之间的调用不太会
        print string,"is a  palindrome"
    else:
        print string,"is not a palindrome"