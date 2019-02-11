# -*- coding: UTF-8 -*-

class Base1:
    def foo1(self):
        print("我是foo1，我为base1代言")


class Base2:
    def foo2(self):
        print("我是foo2，我为base2代言")


class C(Base1,Base2):
    pass

c = C()
c.foo1()
c.foo2()
