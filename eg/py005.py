# -*- coding: UTF-8 -*-

class MyList(list):
    pass

list2 = MyList();
list2.append(5)
list2.append(9)
list2.append(0)
print list2
list2.sort()
print list2  #改变原数组
print list2[0]