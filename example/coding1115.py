# -*- coding: utf-8 -*-
class Person(object):
	count=0
	person_list=[]
	def __init__(self,name):
		self.name=name

	def info(self):
		print('I am %s' %self.name)
def get(name):
	pass
def add(person,**kw):
	for k,v in kw.items():
		setattr(person,k,v)
	Person.count += 1
	person_list.append(person)
	print('Added %s,there\'re %d people now.'%(getattr(person,'name'),Person.count))

class Teacher(Person):
	def info(self):
		print('I am a teacher,my name is %s' %self.name)
class Student(Person):
	def info(self):
		print('I am a student,my name is %s' %self.name)

def intro(person):
	person.info()

intro(Person('Akun'))
intro(Teacher('Bkun'))
intro(Student('Ckun'))

#print(dir('ABC'))
#print(dir(Person()))
p=Person('Dkun')
if hasattr(p,'info'):
	m = getattr(p,'info')
	m()
add(Person('A'))
add(Teacher('B'))
add(Student('C'))

print(type(Person))
print(type(p))
print(type(m))