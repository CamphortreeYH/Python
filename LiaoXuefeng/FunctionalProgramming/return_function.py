# -*- coding: utf-8 -*-

def createCounter():
    s = [0]
    def counter():
        s[0] = s[0]+1
        return s[0]
    return counter

counterA = createCounter()
print counterA(), counterA(), counterA(), counterA(), counterA()
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('success!')
else:
    print('fail!')