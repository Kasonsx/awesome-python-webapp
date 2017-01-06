#-*- coding: utf-8 -*-
from functools import reduce
#map函数
def f(x):
	return 2*x+1
l=[1,2,3,4,5,6,7,8,9]
print(list(map(f,l)))
#reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))

def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

print(str2int('13579'))

#利用map和reduce编写一个str2float函数，把字符串转换为浮点数
def str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

l=[4,5,6]
print(l)
print(l[::-1])

def is_odd(n):
	return n%2==1
def not_empty(s):
	return s and s.strip()
print(list(filter(is_odd,[1,2,4,5,6,9,10,15]))