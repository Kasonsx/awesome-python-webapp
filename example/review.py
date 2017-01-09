# -*- coding:utf-8 -*-
# 集合set,去除重复元素
a = set('sjadhakjsdanv')
print(a)

# zip，同时循环两个或以上序列，用zip整体打包
list1 = ['Z','s','u','g']
list2 = ['ad','asda','wetw','kjsn']
for a,b in zip(list1,list2):
	print('list1:{0} and list2: {1}'.format(a,b))
