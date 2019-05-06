# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 80 and self.score <= 100:
            return 'A'
        elif self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 0 and self.score < 60:
            return 'C'
        else:
            raise ValueError('value is not between 0 and 100')

