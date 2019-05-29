import smtplib
from email.mime.image import  MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#第三方SMTP服务
mail_host = "smtp.qq.com" #设置服务器
mail_user = "xxx.com" #用户名
mail_pass = "xxxxx" #口令

sender = 'xxx@qq.com'
receivers = ['xxx@qq.com'] #接收邮件，可以设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')  #发送者
msgRoot['To'] = Header("测试", 'utf-8') #接收者
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = '''
<p>Python 邮件发送测试……</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"</p>
'''
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

#指定图片为当前目录
fp = open('runoob.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

#定义图片ID，在HTML文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25) #25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")