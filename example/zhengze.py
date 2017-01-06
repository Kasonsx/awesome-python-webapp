# -*- coding: utf-8 -*-
import re
#\s 空格
#\w 字母或数字
#
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())

re_email = re.compile(r'(^\w[a-zA-Z0-9\.\_]+)@([a-zA-Z0-9]+)\.com$')
print(re_email.match('someone@gmail.com').groups())
print(re_email.match('bill.gates@microsoft.com').groups())
print(re_email.match('sxk6446@163.com').groups())

re_email2 = re.compile(r'(^<[\w\s]*>)\s([\w]+)@([\w]+)\.(org|com|net)$')
print(re_email2.match('<Tom Paris> tom@voyager.org').groups())

