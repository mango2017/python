# -*- coding: UTF-8 -*-
class Reacangle:
    # def __init__(self,x):
    #     self.x = x

    def __getattr__(self, item):
        print("getattr")

    def __setattr__(self, key, value):
        print("setattr")

r = Reacangle()
r.y = 10