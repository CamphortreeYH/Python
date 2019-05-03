# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
newL1 = sorted(L, key = lambda l: l[0])
newL2 = sorted(L, key = lambda l: l[1], reverse=True)
print newL1
print newL2



