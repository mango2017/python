# -*- coding: UTF-8 -*-
class A(object):
    bar = 1
    bar1 = 9

a = A()

print getattr(a,'bar')  #getattr() 函数用于返回一个对象属性值

print getattr(a,'bar1',5)

print getattr(a,'bar2',5)