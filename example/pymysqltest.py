# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',db='db',charset='utf8')
cur = conn.cursor()
cur.execute("USE db")
random.seed(datetime.datetime.now())

def store(title, content):
	cur.execute("INSERT INTO pages (title,content) values (\"%s\",\"%s\")",(title,content))
	cur.connection.commit()

def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html)
	title = bsObj.find("h1").get_text()
	content = bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
	store(title,content)
	return bsObj.find("div", {"id":"bodyContent"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
	while len(links) > 0:
		newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
		print(newArticle)
		links = getLinks(newArticle)
finally:
	cur.close()
	conn.close()