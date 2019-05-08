#!/usr/bin/env python
# -*- coding: utf-8 -*-

#实现 dir -l功能
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

#列出MyPath下.py格式的文件信息
import os.path
import glob
from datetime import datetime

pyfiles = glob.glob('*.py')
MyPath = 'D:\\Automation\\LiaoXuefeng\\IO'

name_sz_date = [(name, os.path.getsize(name), os.path.getatime(name)) for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M'))

file_metadate = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadate:
    print(name, meta.st_size, datetime.fromtimestamp(meta.st_mtime).strftime('%Y-%m-%d %H:%M'))
