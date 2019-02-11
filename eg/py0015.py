# -*- coding: UTF-8 -*-

class A:
    pass

class B(A):
    pass


class C:
    def __init__(self,x=0):
        self.x = x


print issubclass(B,A)

print issubclass(B,B)

print issubclass(B,object)

print issubclass(B,C)

b1 = B()
print isinstance(b1,B)

print isinstance(b1,A)

print isinstance(b1,C)

print isinstance(b1,(A,B,C))


c1 = C()
print hasattr(c1,'x')
print getattr(c1,'x')
print delattr(c1,'x')
print hasattr(c1,'x')