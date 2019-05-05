from functools import reduce
import logging

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        # print('Error:', e)
        logging.exception(e)
    finally:
        print('finally...')


main()

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise  FooError('invalid value: %s' % s)
    return 10/n

foo(0)

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' %s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
