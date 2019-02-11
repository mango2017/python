# -*- coding: UTF-8 -*-

class Parent:
    def hello(self):  #self是对象
        print("正在调用父类的方法...")

class Child(Parent):  #继承父类
    def hello(self):
        print("正在调用子类的方法...")

p = Parent()
p.hello()

c = Child()
c.hello()