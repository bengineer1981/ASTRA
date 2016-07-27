#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
short_list = []
node_count = 0
while node_count < 2:
	try:
		sock.settimeout(10)
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		short_list.append(data)
		node_count =+1
	except socket.timeout:
		print 'socket timed out'
		break
index = 0
for msg in short_list:
	print 'msg #%d: %s' % (index +1,msg)
	index +=1
