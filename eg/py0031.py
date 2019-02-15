# -*- coding: UTF-8 -*-

import psutil
print(psutil.cpu_count()) #获取cpu逻辑数量

print(psutil.cpu_count(logical=False))