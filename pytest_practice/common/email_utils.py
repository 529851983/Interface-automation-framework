import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.moudle import BASEDIR
import traceback


class EmailUtil(object):

    def __init__(self):
        pass

    def send_email(self, smtpserver, username, receiver):
        # 1.定义smtp服务器、发送 邮箱用户名和密码、接收邮箱、邮件主题等
        smtpserver = smtpserver
        username = username
        passpord = 'hlviwxmhfmwsbief'
        receiver = receiver

        # 2.创建邮件对象（邮件对象、邮件主题等）
        message = MIMEMultipart('related')  # 这相当于创建了一个内容为空的带附件的邮件对象
        subject = '接口自动化测试报告'
        attach = MIMEText(open('%s/output/report.zip' % BASEDIR, 'rb').read(), _subtype='html', _charset='utf-8')
        attach['Content-Type'] = 'application/octet-stream'
        attach['Content-Disposition'] = 'attachment;filename="report.zip"'

        # 3.把邮件的信息组装到邮件对象里
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(MIMEText('啊啊啊啊'))
        message.attach(attach)

        # 4.登录smtp服务器，并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user=username, password=passpord)
        try:
            smtp.sendmail(from_addr=username, to_addrs=receiver, msg=message.as_string())
            print('发送邮件成功！')
            smtp.quit()
        except Exception as e:
            print(e, traceback.format_exc())



smtpserver = 'smtp.qq.com'
username = '529851983@qq.com'
receiver = '18534518046@163.com'

if __name__ == '__main__':
    email = EmailUtil()
    email.send_email(smtpserver, username, receiver)



