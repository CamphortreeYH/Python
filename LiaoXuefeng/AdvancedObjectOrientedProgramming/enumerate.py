# -*- coding: utf-8 -*-
#python 3
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print("Sucess")
else:
    print ("Fail")

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print (name, '=>', member, ',', member.value)

from enum import Enum

class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
    red_alias = 1

for color in Color.__members__.items():
    print(color)