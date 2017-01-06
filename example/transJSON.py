# -*- coding: utf-8 -*-
import pickle
import json
#序列化
d = dict(name='Bob',age=20,score=88)
pickle.dumps(d)
with open('dump.txt','wb') as f:
	pickle.dump(d,f)
with open('dump.txt','rb') as f:
	print(pickle.load(f))
#json
d = dict(name='Bob',age=22,score=89)
json.dumps(d)

json_str = '{"age":20,"score":88,"name":"Bob"}'
json.loads(json_str)

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

s = Student('Bob',22,90)
print(json.dumps(s,default=student2dict))
print(json.loads(json_str,object_hook=dict2student))