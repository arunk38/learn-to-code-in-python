__author__ = 'akalagar'

import smtplib

smtpObj = smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtpObj.ehlo() # 250: success

smtpObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ') # Turn turn-on less secure apps

smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com',
                 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely,Bob')

smtpObj.quit()
