# -*- coding: UTF-8 -*-
class A(object):
    bar = 1

a = A()
print getattr(a,'bar')

setattr(a,'bar',5)
print a.bar