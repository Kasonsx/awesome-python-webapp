# -*- coding:utf-8 -*-
import socket
import threading,time
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5) #指定等待连接的最大数量
print('Waiting for connection...')

while True:
	sock,addr = s.accept() # accept()返回(conn, address),conn是新的接受返回数据的socket对象
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()



