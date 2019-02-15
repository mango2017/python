# -*- coding: UTF-8 -*-
import base64
s = base64.b64encode('在python中使用base 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在python中使用base 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)