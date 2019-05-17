# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    a = len(s) % 4
    s += a * b'='
    return base64.b64decode(s)
    # while len(s) % 4 != 0:
    #     s += b'='
    # r = base64.urlsafe_b64decode(s)
    # index = len(r)
    # for c in r[:-1]:
    #     if c == '=':
    #         index -= 1
    # return r[:index]

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')