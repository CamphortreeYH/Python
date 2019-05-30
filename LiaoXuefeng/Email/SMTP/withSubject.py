from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

'''
email.utils.parseaddr(address)
解析地址 - 它应该是其构成的真名和电子邮件中的一些包含地址的字段的值，例如To或Cc 地址部分。返回该信息的元组，除非解析失败，在这种情况下返回（''， ''）的2元组。
email.utils.formataddr(pair, charset='utf-8')
parseaddr()的倒数，它采用形式为（realname， email_address）的2元组返回适用于To或Cc头的字符串值。如果对的第一个元素为假，那么第二个元素将不被修改。
Optional charset is the character set that will be used in the RFC 2047 encoding of the realname if the realname contains non-ASCII characters. 可以是str或Charset的实例。默认为utf-8。
我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
'''

def _format_addr(s):
    name, addr = parseaddr(s)
    return  formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

# 参数1.邮件正文  参数2MIME的subtype,plain表示纯文本，最终的MIME就是text/plain，
# 最后一定要用utf-8编码保证多语言的兼容性
# 如果发送HTML邮件 把HTML字符串传进去 把plain变为html
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
# 你看到的收件人的名字很可能不是我们传入的管理员，因为很多邮件服务商在显示邮件时，
# 会把收件人名字自动替换为用户注册的名字，但是其他收件人名字的显示不受影响。
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
# 发邮件，可以发给多个人，所以是一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
