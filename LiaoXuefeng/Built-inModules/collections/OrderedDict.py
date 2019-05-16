from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od1 = OrderedDict()
od1['z'] = 1
od1['y'] = 2
od1['x'] = 3
list(od1.keys())
print(od1)