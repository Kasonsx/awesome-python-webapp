# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

from_addr = "sxk644653293@163.com"
password = input('password:')
to_addr = "sxk644653293@163.com"
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
	
def sendEmail(subject, body):
	msg = MIMEText(body)
	msg['From'] = _format_addr('Kason <%s>' % from_addr)
	msg['To'] = _format_addr('Test <%s>' % to_addr)
	msg['Subject'] = Header(subject,'utf-8').encode()

s = smtplib.SMTP("smtp.163.com",25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()