# -*- coding:utf-8 -*-
def fib1(max):
	n,a,b=0,0,1
	while n < max:
		print(b)
		a, b = b, a+b
		n = n + 1
	return 'done'

def fib2(max):
	n,a,b=0,0,1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	print(b)
	return 'done'

fib1(6)
print(fib2(6))

def triangles():
	L = [1]
	while True:
		yield L
		L.append(0)
		length = len(L)
		L = [L[i-1] + L[i] for i in range(length)]

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break



	 