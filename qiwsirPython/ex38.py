#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 23:19

# 38、根据行数访问指定文件。键盘输入数字n和文件名，显示该文件的前n行，再显示该文件的总行数。
'''
这样的程序我想尝试用函数写，但我还是搞不清，应该把哪部分放进函数中,感觉分不开

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
'''
if __name__ == "__main__":
    while True:
        try:
            input_file = raw_input("Enter a filename: ")
            input_num = int(raw_input("Enter a line number: "))
            with open(input_file, 'r') as f:
                count_lines = 0
                for i in f:
                    count_lines += 1
                    if input_num >= count_lines:
                        print count_lines,i,
                print '\n',"---------------end-of-contents----------",'\n',"The full text of the number of rows:",count_lines

            break
        except IOError as ex:
            print ex
        except ValueError as ex:
            print ex
        except:
            print "Something wrong in the input"
