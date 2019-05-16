# -*- coding:utf-8 -*-

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("x:", p.x)
print("y:", p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print("x:", c.x)
print("y:", c.y)
print("r:", c.r)