# -*- coding:utf-8 -*-
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html)
# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
# for image in images:
# 	print(image["src"])
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datatime
import random
import re
# Kevin_Bacon下的所有链接
random.seed(datetime.datetime.now())
def getLinks(acticleUrl):
	html = urlopen("http://en.wikipedia.org"+acticleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div",{"id":"bodyContent"}).findAll("a",
		href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
	newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)

# wiki网站采集,链接去重
pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html)
	for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")

