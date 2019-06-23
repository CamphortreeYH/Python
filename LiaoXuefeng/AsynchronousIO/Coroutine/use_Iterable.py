from collections import Iterable #可迭代对象
from collections import Iterator #迭代器

title = ['Python', 'Java', 'C++'] #列表是一个可迭代对象
print(isinstance(title, Iterable)) #True
a = iter(title) #由可迭代对象的iter方法返回一个迭代器
print(next(a))
print(next(a))
print(next(a))
print(next(a)) # 抛出StopIteration异常
