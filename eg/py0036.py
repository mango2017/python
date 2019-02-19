# -*- coding: UTF-8 -*-
#创建字典
a = {'name':'gaoqi','age':18,'job':'programmer'}
print(a)
b = dict(name='gaoqi',age=18)
print(b)
c = dict([('name','gaoqi'),('age',18)])
print(c)
d = {}
print(d)
e = dict()
print(e)

k = ['name','age']
v = ['gaoqi',19]
dd = dict(zip(k,v))
print(dd)

#通过fromkeys创建值为空的字典
aa = dict.fromkeys(['name','job'])
print(aa)

#获取字典的值
print(a['name'])
print(a.get('name'))
print(a.get('name1','aa'))
print(a.keys())
print(a.values())
print(len(a))
print('name' in a)

#字段元素添加，修改，删除
a['address'] = '大院'
print(a)


aaa = {'name':'gaoqi','age':18}
bbb = {'name':'jly','address':'嘿嘿'}
aaa.update(bbb)
print(aaa)

del(aaa['name'])
print(aaa)

bs = aaa.pop('address')
print(bs)
print(aaa)

print(a)

print(a.popitem())

print(a)