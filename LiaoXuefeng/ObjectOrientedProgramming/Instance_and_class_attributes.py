# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print "fail"
else:
    bart = Student('Bart')
    if Student.count != 1:
        print "fail"
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print "fail"
        else:
            print('Students:', Student.count)
            print "success"
