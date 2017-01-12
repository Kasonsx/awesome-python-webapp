# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root',db='db',charset='utf-8')
cur = conn.cursor()
cur.execute("USE db")

# 返回链接在数据库中的id，不存在就先插入
def insertPageIfNotExists(url):
	cur.execute("select * from pages where url = %s",(url))
	if cur.rowcount == 0:
		cur.execute("insert into pages (url) values (%s)",(url))
		conn.commit()
		return cur.lastrowid
	else:
		return cur.fetchone()[0]
# 数据库中保存两个链接的id
def insertLink(fromPageId, toPageId):
	cur.execute("select * from links where fromPageId = %s and toPageId = %s",(int(fromPageId),int(toPageId)))
	if cur.rowcount == 0:
		cur.execute("insert into links (fromPageId,toPageId) values (%s,%s)",(int(fromPageId),int(toPageId)))
		cur.commit()
pages = set()
def getLinks(pageUrl,recursionLevel):
	global pages
	if recursionLevel > 4:
		return;
	pageId = insertPageIfNotExists(pageUrl)
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html)
	for link in bsObj.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
		insertLink(pageId,insertPageIfNotExists(link.attrs['href']))
		if link.attrs['href'] not in pages:
			newPage = link.attrs['href']
			pages.add(newPage)
			getLinks(newPage, recursionLevel+1)

getLinks('/wiki/Kevin_Bacon',0)
cur.close()
conn.close()
