#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/4 10:20

def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, 'r')
    counts = 26 * [0]
    for line in infile:
        countLetters(line.lower(), counts)
    for i in range(len(counts)):
        print i
        if counts[i] != 0:
            print chr(ord('a') + i) + " appears " + str(counts[i]) + (" time" if counts[i] == 1 else "times")
    infile.close()

def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

main()
