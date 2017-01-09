# -*- coding:utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getContent(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.title
	except AttrbuteError as e:
		return None
	return title
# title = getContent("http://pythonscraping.com/pages/page1.html")
# if title == None:
# 	print('Title could not be found')
# else:
# 	print(title)

# html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
# bsObj = BeautifulSoup(html)
# # namelist = bsObj.findAll('span',{'class':'green'})
# # # findAll(tag,attribute, recursive,text,limit,keywords)
# # unique = []
# # for name in namelist:
# # 	unique.append(name.get_text())
# # nl = sorted(set(unique),key=unique.index)
# # for n in nl:
# # 	print(n)
# allclass = bsObj.findAll(class_="green")
# for c in allclass:
# 	print(c.get_text)

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for child in bsObj.find("table",{"id":"giftList"}).children:
	print(child)
