# -*- coding: UTF-8 -*-

# class BB:
# #     def printBB(self):
# #         print("hello bb")
# #
# # bb = BB()
# # bb.printBB()



class CC:
    def setXY(self,x,y):
        self.x = x
        self.y = y

    def printXY(self):
        print(self.x,self.y)

dd = CC()
dd.__dict__
CC.__dict__

