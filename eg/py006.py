# -*- coding: UTF-8 -*-

class A:
    def fun(self):
        print "我是小A"

class B(A):
    def fun(self):
        print "我是小B"


a = A()
b = B()
a.fun()
b.fun()