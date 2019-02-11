# -*- coding: UTF-8 -*-
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？ true
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？ false
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？true
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y' 19
print('obj.y =', obj.y) # 获取属性'y' 19

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404 404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f()) #81