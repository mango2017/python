# -*- coding: UTF-8 -*-

class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    def climb(self):
        print "我正在很努力的向前爬..."

    def run(self):
        print "我正在飞快的向前跑...."

    def bite(self):
        print self
        print self.__class__
        print "咬死你...."

    def eat(self):
        print "有的吃，真满足...."

    def sleep(self):
        print "困了，睡了，晚安...."

tt = Turtle()
Turtle().bite();
tt.eat()
