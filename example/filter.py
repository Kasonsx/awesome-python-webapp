#-*- coding: utf-8 -*-
#生成器
def odd_iter():
	n=1
	while True:
		n=n+2
		yield n
#筛选器
def not_divisable(n):
	return lambda x:x%n>0
#最后生成器
def primes():
	yield 2
	it = odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(not_divisable(n),it)
#打印1000以内的素数
for n in primes():
	if n<1000:
		print(n)
	else:
		break
