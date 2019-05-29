from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return  formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = 'smtp.qq.com'
smtp_port = 587


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, smtp_port)
#SMTP.starttls(keyfile=None,certfile=None)：启用TLS安全传输模式，所有SMTP指令都将加密传输，如使用gmail的smtp服务时需哟啊启动此项才能正常发送邮件。
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()