def h():
    print('Wen Chuan', end=' ')
    m = yield 5 #Fighting!
    print(m)
    d = yield 12
    print('We are together!')

c = h()
m = next(c) # m获取了yield 5 的参数值5
d = c.send('Fighting!') #d获取了yield 12的参数值12
print('We will never forget the data', m, '.', d)