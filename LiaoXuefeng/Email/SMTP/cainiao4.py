import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#第三方SMTP服务
mail_host = "smtp.qq.com" #设置服务器
mail_user = "xxx@qq.com" #用户名
mail_pass = "xxxxx" #口令

sender = 'xxx.com'
receivers = ['xxx@qq.com'] #接收邮件，可以设置为你的QQ邮箱或者其他邮箱

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')  #发送者
message['To'] = Header("测试", 'utf-8') #接收者
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

#构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octect-stream' #application/octet-stream:只能提交二进制，而且只能提交一个二进制，如果提交文件的话，只能提交一个文件,后台接收参数只能有一个，而且只能是流（或者字节数组）
#这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt' #为附件添加一个标题
message.attach(att1)

#构造附件2，传送当前目录下的runoob.txt文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25) #25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")