# -*- coding:utf-8 -*-
import orm
import asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
	yield from orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	# u = User(name='Kason', email='test3@example.com', passwd='1234567890',image='about:blank')
	# yield from u.save()
	# r1 = yield from User.findAll()
	# print('All users:',r1)
	# r2 = yield from User.findAll(name='Kason')
	# print('User Kason:',r2)
	# 销毁连接池
	yield from orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
# for x in test():
# 	pass