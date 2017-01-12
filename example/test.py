# #-*- coding: utf-8 -*-
# #筛选回文数，如121，45654
# def is_palindrome(n):
# 	return n==int(str(n)[::-1])
# output=filter(is_palindrome,range(1,1000))
# #print(list(output))

# #闭包
# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def f():
# 			return i*i
# 		fs.append(f)
# 	return fs
# f1,f2,f3=count()
# #print(f1())
# #print(f2())
# #print(f3())

# def outer(func):
# 	def inner():
# 		print('I am inner')
# 	return inner#若返回inner()则会执行
# def foo():
# 	print('I am foo')

# outer(foo)
# #outer(foo())
# for n in range(2,2):
# 	print(n)
# # for n in range(2,10):
# # 	print(n)

num = set()
for i in range(10):
	num.add(i)

for n in range(-3,5):
	num.add(n)

for n in num:
	print(n)