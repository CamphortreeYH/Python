# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己辩解的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口为8000,处理函数是application
httpd = make_server('', 8000, application)
print('Server HTTP on port 8000...')

# 开始监听HTTP请求:
httpd.serve_forever()