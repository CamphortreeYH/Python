# -*- coding: utf-8 -*-
#example 1
import sys

def fibonacci(n): #生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f是一个迭代器，由生成器返回生成

while True:
    try:
        print next(f),
    except StopIteration:
        sys.exit()

#简单输出斐波那契哦数列前N个数 （没有用生成器）
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fab(5)

#输出斐波那契哦数列前N个数 （没有用生成器）
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        print b
        a, b = b, a + b
        n = n + 1
    return L

for n in fab(5):
    print n

#利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a , self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

for n in Fab(5):
    print n

#使用 yield
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b    #使用yield
        a, b = b, a + b
        n = n + 1

for n in fab(5):
    print n
