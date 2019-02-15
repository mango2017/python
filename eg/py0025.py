# -*- coding: UTF-8 -*-
from datetime import datetime

print(datetime.now())
dt = datetime(2019,2,12,8,12,50)
print(dt)
print(dt.timestamp())
print(dt.fromtimestamp(1549930370.0))