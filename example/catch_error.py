# -*- coding: utf-8 -*-
import logging
import pdb
logging.basicConfig(level=logging.INFO)
try:
	print('try...')
	num = input('enter a number:')
	result = 100/int(num)
	print('result is ',result)
except ValueError as e:
	print('exception is ',e)
finally:
	print('Finally..')
print('The end.')

def foo1():
	n = int(input('enter a number:'))
	if n==0:
		raise ValueError('Can\'t divide a zero')
	return 10/n

def foo2():
	n = int(input('enter a number:'))
	logging.info('n=%d'%n)
	print(10/n)

def foo3():
	s='0'
	n=int(s)
	pdb.set_trace()
	print(10/n)
foo1()
foo2()
foo3()

