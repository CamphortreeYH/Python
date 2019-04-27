#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    n = s.index('.')
    mod = len(s) - n - 1
    return reduce(lambda x, y: x * 10 + y, map(lambda m : DIGITS[m], s.replace('.', ''))) * 0.1 ** mod

print 'str2float(\'123.456\') =', str2float('123.456')
if abs(str2float('123.456') - 123.456) < 0.00001:
    print 'success'
else:
    print 'fail'
