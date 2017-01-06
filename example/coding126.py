# -*- coding: utf-8 -*-
from enum import Enum,unique
Week = Enum('Week',('Sun','Mon','Tue','Wed','Thu','Fri','Sat'))


#精确控制
@unique
class Week(Enum):
	Sun = 0
	Mon = 1 
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

for name,member in Week.__members__.items():
	print(name,'=>',member,',',member.value)

class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
	pass

L = MyList()
L.add(2)
L.add(1)
print(L)


