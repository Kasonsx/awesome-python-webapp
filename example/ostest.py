# -*- coding: utf-8 -*-
import os 
def findFile(filename,path = os.getcwd()):
	tmppath = os.getcwd()
	os.chdir(path)
	for x in os.listdir('.'):
		if os.path.isfile(x):
			if filename in os.path.splitext(x)[0]:
				print(os.path.relpath(x))
		elif os.path.isdir(x):
			path = os.path.abspath(x)
			findFile(filename,path)
			os.chdir(tmppath)

def search(path, word):
	for x in os.listdir(path):
		fullpath = os.path.join(path,x)
		if word in x :
			print(os.path.abspath(fullpath))
		else:
			if os.path.isdir(fullpath):
				search(fullpath,word)

search('D:\\study','cod')
if __name__ == '__main__':
	findFile('cod')
