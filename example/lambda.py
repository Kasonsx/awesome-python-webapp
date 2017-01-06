#-*- coding:utf-8 -*-
import functools
def build(x,y):
	return lambda:x*x+y*y
print(build(1,2)())

#装饰器
def log1(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' %func.__name__)
		return func(*args,**kw)
	return wrapper

def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s ():' %(text, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log2('execute')
def test():
	print('2016-11-11')

test()
