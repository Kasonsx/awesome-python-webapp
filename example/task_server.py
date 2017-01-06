# -*- coding: utf-8 -*-
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()

#QueueManager
class QueueManager(BaseManager):
	pass
def return_task_queue():
	global task_queue
	return task_queue
def return_result_queue():
	global result_queue
	return result_queue

def server():
	QueueManager.register('get_task_queue',callable=return_task_queue)
	QueueManager.register('get_result_queue',callable=return_result_queue)
	
	manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
	#启动Queue
	manager.start()
	#获取Queue对象
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	#task Queue取任务，result Queue写结果
	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d...'%n)
		task.put(n)

	print('Try get results...')
	for i in range(10):
		r = result.get(timeout=10)
		print('Result: %s' % r)

	#close manager
	manager.shutdown()
	print('master exit.')

if __name__ == '__main__':
	freeze_support()
	server()