# -*- coding: UTF-8 -*-

class C:
    def x(self):
        print("x-man")

c = C()
c.x()
c.x = 1  #当属性的名字和方法名相同时，属性的名字会覆盖方法名
print c.x

c.x()