#!/usr/bin/env python

'''

    Author:
        Kyle Wu <imkylewu@gmail.com>
        http://www.kylewu.net
 
    File:             rtm.py
    Create Date:      Thu Dec  2 20:32:00 2010


    A simple python script for adding task in RTM

    usage: python rtm.py [msg]
    
    example: python rtm.py go shopping at 10 pm

'''

import sys
import smtplib
from email.mime.text import MIMEText

# My email and RTM mail
FROM = 'wenbin87@gmail.com'
TO = 'kyle.wu+08be61@rmilk.com'

# MSG body and title
msg = MIMEText('RTM')
msg['Subject'] = " ".join(sys.argv[1:])
msg['From'] = FROM
msg['To'] = TO

# Login and send
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('wenbin87@gmail.com', 'example')
server.sendmail(FROM, [TO], msg.as_string())
server.quit()
