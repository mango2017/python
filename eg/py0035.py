# -*- coding: UTF-8 -*-
import io

s = "hello,stx"
sio = io.StringIO(s)
print(sio)
print(sio.getvalue())
sio.seek(7)
sio.write('g')
print(sio.getvalue())
