# -*- coding: utf-8 -*-

import re

def name_of_email(addr):
    m = re.match(r'(^<[\w ]+>)|(^[\w]+@)', addr).group()
    if m.find('<') == 0:
        return m[1:-1]
    else:
        return m[:-1]

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
