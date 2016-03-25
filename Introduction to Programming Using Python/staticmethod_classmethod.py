#!/usr/bin/env python
#coding:utf-8
#Created by one on 2016/2/27

class StaticMethod(object):
    @staticmethod #表示下面的方法是静态方法
    def foo():
        print "this is static method foo()."

class ClassMethod(object):
    @classmethod #表示下面的方法是类方法
    def bar(cls):
        print " This is class method bar()."
        print "bar() is part of class:", cls.__name__

if __name__ == "__main__":
    static_foo = StaticMethod()
    static_foo.foo() # 实例调用静态方法
    StaticMethod.foo() # 通过类调用静态方法
    print "-----------"
    class_bar = ClassMethod()
    class_bar.bar()
    ClassMethod.bar()