# -*- coding: utf-8 -*-
import os
# print('Process (%s) start...' %os.getpid())
# pid = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s.'%(os.getpid(),os.getppid()))
# else:
# 	print('I (%s) just created a child process (%s).'%(os.getpid(),pid))
#windows下没有fork方法
#使用Process模块代替
from multiprocessing import Process
def run_proc(name):
	print('Run child process %s (%s)...' %(name, os.getpid()))
#执行
# if __name__ == '__main__':
# 	print('Parent process %s.' %os.getpid())
# 	p = Process(target=run_proc, args=('test',))
# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')

#进程池Pool
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
	print('RUn task %s (%s)...'% (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)#random() return [0.0,1.0),sleep(seconds)
	end = time.time()
	print('Task %s run %0.2f seconds.'% (name,(end-start)))
if __name__ =='__main__':
	print('Parent process %s.' %os.getpid())
	p = Pool(4)
	for i in range(9):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')