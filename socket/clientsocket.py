#-*- coding: utf-8 -*-
import socket

#udp test
s_handle=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
ip_port=("127.0.0.1", 4096)

while True:
	inp=raw_input('please input:')
	s_handle.sendto(inp, ip_port)
	data=[]
	try:
		data=s_handle.recv(1024)
		print(data)
	except Exception as e:
		continue
	finally:

		pass

s_handle.close()