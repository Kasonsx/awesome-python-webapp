# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHtmlParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('handle_starttag:<%s>,attrs:%s' %(tag,attrs))
	def handle_endtag(self, tag):
		print('handle_endtag:</%s>' %tag)
	def handle_startendtag(self,tag,attrs):
		print('handle_startendtag:<%s/>' %tag)
	def handle_data(self,data):
		print('handle_data:',data)
	def handle_comment(self,data):
		print('handle_comment:<!--',data,'-->')
	def handle_entityref(self,name):
		print('handle_entityref:&%s;' %name)
	def handle_charref(self,name):
		print('handle_charref:&#%s;' %name)

parser = MyHtmlParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
	<div class="test"></div>
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

class MeetingParser(HTMLParser):
	def __init__(self):
		
	def handle_starttag(self,tag,attrs):
		#print('handle_starttag:<%s>,attrs:%s' %(tag,attrs))
		if tag=='ul' and attrs[0][1]=='list-recent-events menu':
			pass
	def handle_endtag(self, tag):
		print('handle_endtag:</%s>' %tag)
	def handle_startendtag(self,tag,attrs):
		print('handle_startendtag:<%s/>' %tag)
	def handle_data(self,data):
		print('handle_data:',data)
	def handle_comment(self,data):
		print('handle_comment:<!--',data,'-->')
	def handle_entityref(self,name):
		print('handle_entityref:&%s;' %name)
	def handle_charref(self,name):
		print('handle_charref:&#%s;' %name)