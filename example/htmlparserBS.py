# -*- coding:utf-8 -*-
# 获取Python官网的议会详情
# import requests
# from bs4 import BeautifulSoup
# reqs = requests.get('https://www.python.org/events/python-events/')
# soup = BeautifulSoup(reqs.text, 'html.parser')

# for li in soup.select('.list-recent-events > li'):
# 	print('title:',li.find('a').text)
# 	print('time:',li.find('time').text)
# 	print('location:',li.select_one('.event-location').text)
# 	print('*'* 100)

from urllib import request
with request.urlopen('http://www.baidu.com') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k,v in f.getheaders():
		print('%s: %s' %(k,v))
	print('Data:',data.decode('utf-8'))