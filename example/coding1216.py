# -*- coding: utf-8 -*-
import time,threading,random
count = 10000
def getMoney(n):
	global count
	count = count - n

def saveMoney(n):
	global count
	count = count + n

def run(n):
	for i in range(n):
		r = round(random.random())
		if r == 0:
			getMoney(200)
			print('get 200')
		elif r == 1:
			saveMoney(500)
			print('save 500')

t1 = threading.Thread(target=run, args=(5,)) 
t2 = threading.Thread(target=run, args=(4,)) 
t1.start()
t2.start()
t1.join()
t2.join()
print(count)