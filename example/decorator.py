#-*- coding: utf-8 -*-
import functools
def log(func):
	def dcr(*args,**kw):
		print('begin call')
		result = func(*args,**kw)
		print('end call')
		return result
	return dcr

@log
def f(name):
	print('I am %s.'%name)

f('kason')

#编写一个适用于有无参数皆可的装饰器
def logn(text=None):
	flag=isinstance(text,str)
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			if flag:
				print('%s %s()' %(text,func.__name__))
			else:
				print('call %s()' %func.__name__)
			return func(*args,**kw)
		return wrapper
	if flag:
		return decorator
	else:
		return decorator(text)



@logn('execute')
def now():
	print('I am now')

@logn
def random():
	print('I am random')

now()
random()