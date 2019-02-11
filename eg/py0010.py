# -*- coding: UTF-8 -*-
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置：",self.x,self.y)



class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃")
            self.hungry = False
        else:
            print("太撑了，吃不下了")

fish = Fish()
fish.move()
fish.move()
fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat()
shark.move()
shark.move()

