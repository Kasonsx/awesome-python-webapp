# -*- coding: utf-8 -*-
from types import MethodType
class Student(object):
	pass
	#__slots__=('name','age')#限制绑定的属性名称
s = Student()

def set_age(self,age):
	self.age = age

s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('Please input a integer')
		self._width=value
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('Please input a integer')
		self._height=value
	@property
	def resolution(self):
		return self._height*self._width
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution