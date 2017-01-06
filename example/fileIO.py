# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO
try:
	f = open('d:/study/test.txt','r')
	print(f.read())
finally:
	if f :
		f.close()

#easy way to read file
def readFile(path):
	with open(str(path),'r') as f:
		print(f.read())
def writeFile(path,content):
	with open(str(path),'a',encoding='utf-8',errors='ignore') as f:
		f.write(content)

path = 'd:/study/test.txt'
content = 'I am writing something in this file.'
writeFile(path,content)
readFile(path)
writeFile(path,content)
readFile(path)

#内存中读写
#读写str
mf = StringIO()
mf.write('hello')
mf.write(' ')
mf.write('world!')
print(mf.getvalue())
#读写二进制数据
bf = BytesIO()
bf.write('中文'.encode('utf-8'))
print(bf.getvalue())
