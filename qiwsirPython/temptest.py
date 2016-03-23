#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/22 18:24

def showLines(f,input_num):
    count_lines = 0
    for i in f:
        count_lines += 1
        if input_num >= count_lines:
            print count_lines,i,
    print '\n',"---------------end-of-contents----------",'\n',"The full text of the number of rows:",count_lines
if __name__ == "__main__":
    while True:
        try:
            input_file = raw_input("Enter a filename: ")
            input_num = int(raw_input("Enter a line number: "))
            with open(input_file, 'r') as f:
                showLines(f,input_num)
            break
        except IOError as ex:
            print ex
        except ValueError as ex:
            print ex
        except:
            print "Something wrong in the input"
