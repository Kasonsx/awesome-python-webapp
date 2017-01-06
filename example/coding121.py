# -*- coding: utf-8 -*-
class Person(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'My name is %s' %self.name
	__repr__ = __str__

print(Person('Kason'))

class Fatigue(object):# fatigue damage
	#num:牌库数，now:现疲劳，turn：抽牌数
	def __init__(self,num,now,turn):
		self.count = 0
		self.num = num
		self.now = now
		self.turn = turn
	def __iter__(self):
		return self
	def __next__(self):
		if self.num-self.turn>=0 or self.turn ==0:
			print('There still have cards.')
			raise StopIteration()
		self.now = self.now + 1
		self.count = self.count + self.now
		self.turn -= 1
		return self.count

#for n in Fatigue(0,0,8):
#	print(n)

class Chain(object):
	def __init__(self, path='website:'):
		self._path = path
	def users(self,name):
		return Chain('%s/users/:%s' %(self._path,name))
	def __getattr__(self,path):
		return Chain('%s/%s' %(self._path,path))
	def __str__(self):
		return self._path
	__repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)


