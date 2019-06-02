#-*- coding: utf-8 -*-
import socket

s_handle=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
s_handle.settimeout(3000)

s_handle.bind(('127.0.0.1', 5555))