# -*- coding: utf-8 -*-
#example1
list = [1, 2, 3, 4]
it = iter(list)    #创建迭代器对象
print next(it)     #输出迭代器的下一个元素
print next(it)

#example2
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print x,

#example3
import sys
list = [1, 2, 3, 4]
it = iter(list)

while True:
    try:
        print next(it)
    except StopIteration:
        sys.exit()

#example4
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def next(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print next(myiter)
print next(myiter)
print next(myiter)
print next(myiter)
print next(myiter)

#example5
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def next(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print x

