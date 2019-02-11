# -*- coding: UTF-8 -*-

class Person:
    __name = "王小虎"  #私有变量在变量前面加两个"_"

    def getName(self):
        return self.__name


p = Person()
print p.getName()
print p._Person__name  #python私有机制 是伪私有，变量是可以被外部调用的