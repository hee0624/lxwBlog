---
title: Email Spoofing(Forged Sender/Recipients/CCs/BCCs)
date: 2017-12-27 20:55:06
tags: [Python, Network]
categories: [Python, Network]
---
如何发送一封完全伪造的电子邮件，伪造的发件人、收件人、伪造的抄送、密送、伪造的主题、正文、附件等。  
Talk is cheap, here is the code.  

```python
#!/usr/bin/env python3
# coding: utf-8
# File: email_spoofing.py
# Author: lxw
# Date: 12/27/17 6:08 PM

import smtplib
import traceback
from email.message import Message


def send_email(subject, content):
    try:
        real_sender, passwd, server = "real_sender@abc.cn", "password", "smtp.abc.cn"
        fake_sender = "fake_sender@abc.cn"
        real_recipients = ["real_recipient1@abc.cn", "real_recipient2@abc.cn", "real_recipient3@abc.cn"]
        fake_recipients = ["fake_recipient1@abc.cn", "fake_recipient2@abc.cn"]

        message = Message()
        message["Subject"] = subject
        message["From"] = fake_sender
        message["To"] = ";".join(fake_recipients)
        #Copy to
        #message["CC"] is only for display, to send the email we must specify it in the method "SMTP.sendmail".
        #message["CC"] = "real_recipients1@abc.cn,real_recipients2@abc.cn"
        message.set_payload(content)
        message.set_charset("utf-8")
        msg = message.as_string()

        sm = smtplib.SMTP(server)
        sm.set_debuglevel(0)    #sm.set_debuglevel(1)
        sm.ehlo()
        sm.starttls()
        sm.ehlo()
        sm.login(real_sender, passwd)

        sm.sendmail(fake_sender, real_recipients, msg)    # 注意： 这里必须是fake_sender，否则会出现"由XXX代发"的问题。
        sm.quit()
        return 0
    except Exception as e:
        traceback.print_exc()
        return 1


def main():
    subject = "明天上午会议取消"
    content = "伪造收件人、发件人、抄送人、邮件主题、邮件内容..."
    if send_email(subject, content) == 0:
        print("邮件发送成功")
    else:
        print("邮件发送失败")


if __name__ == '__main__':
    main()
```
**注意**： `sendmail()`的第一个参数必须是`fake_sender`不能是`real_sender`，否则会出现"由 \*\*\*@\*\*\* 代发"的问题(如下图所示)。  
</br>
![./forged_email.png](./forged_email.png)

### 20180129补充
今天一位同事尝试了上面的代码，发现收件人总是不能成功地收到伪造的邮件，**经测试发现针对上面的代码`fake_sender`与`real_sender`必须是同一个邮件域名下的邮箱(`fake_sender`可以是不存在的邮箱)**，否则就会导致收件人无法收到伪造的邮件。  
关于**能否以及如何**伪造不同域名下的邮箱`fake_sender`，我会尽快查阅并补充