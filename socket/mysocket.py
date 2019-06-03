#-*- coding: utf-8 -*-
import socket

s_handle=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
ip_port=("127.0.0.1", 4096)
s_handle.bind(ip_port)
print('start...')
while True:
	data,address=s_handle.recvfrom(1024)
	print(data,address)
	s_handle.sendto('Service got data.', address)
	if data=='exit':
		break
		pass
	pass

s_handle.close()