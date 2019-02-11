# -*- coding: UTF-8 -*-

class Ball:
    def __init__(self,name):
        self.name = name

    def setName(self,name):
        self.name = name

    def kick(self):
        print("我叫%s" % self.name)


# a = Ball()
# a.setName("球A")
# b = Ball()
# b.setName("球B")
c = Ball("土豆")
# a.kick()
# b.kick()
c.kick()

