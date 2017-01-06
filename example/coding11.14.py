#-*- coding: utf-8 -*-
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('Start to %s %s()' %(text,func.__name__))
			result = func(*args,**kw)
			print('Finish %s %s()' %(text,func.__name__))
			return result
		return wrapper
	return decorator

@log('execute')
def test():
	print('I am testing...')

test()

print(int('128',16))

maxmore=functools.partial(max,10)
print(maxmore(1))