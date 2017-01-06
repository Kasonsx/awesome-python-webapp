#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module' #表示模块的文档注释
__author__='Kason'

import sys
def test():
	args = sys.argv
	if len(args)==1:
		print('Hello world!')
	elif len(args)==2:
		print('Hello,%s!' %args[1])
	else:
		print('Too many arguments!')
def _pvt(name):
	print('Hello,%s!' %name)

print(__name__)
if __name__=='__main__':
	test()

class Doctor(object):
	def __init__(self,name,sex,age):
		self.__name = name
		self.sex = sex
		self.age = age
	def getName(self):
		return self.__name

	def getInfo(self):
		print('%s-%s-%s' %(self.__name,self.sex,self.age))

doc1 = Doctor('Sun','male',22)
doc1.getInfo()	
#变量前加两个下划线变成私有变量
#无法直接访问私有变量print(doc1.__name)
print(doc1.getName())