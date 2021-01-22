# encoding=utf-8
import yagmail

def sendmail():
    yag = yagmail.SMTP(user='642826959@qq.com', password='sapnykyzwjldbeeg', host='smtp.qq.com')
    img_dir = 'C:/Users/吕发发/Pictures/1.png'
    contents = ['我就想给你发QQ邮箱', yagmail.inline(img_dir)]
    attachments = ['C:/Users/吕发发/Downloads/fushi.doc']
    persons = [ '642826959@qq.com']
    yag.send(to=persons, subject='测试自动发邮件', contents=contents, attachements=attachments)

if __name__ == '__main__':
  sendmail()