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

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()