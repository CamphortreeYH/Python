# -*- coding: utf-8 -*-

# from urllib import request
#
# with request.urlopen('https://www.python.org') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)#status:服务器返回的状态代码; reason:服务器返回的原因短语
#     for k, v in f.getheaders(): #获取页面的头信息
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone: CPU iPhone OS 8_0 linke Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
