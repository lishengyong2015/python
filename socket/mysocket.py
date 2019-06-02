#-*- coding: utf-8 -*-
import socket

s_handle=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))