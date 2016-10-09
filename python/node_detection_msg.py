#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
import serial
import sys
import os.path


def socksend(msg):
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect((ip_addr, port))
	clientsocket.send(msg)

filename = '/home/ben/Desktop/senior_design/python/detection.txt'
try:
	os.remove(filename)
except OSError:
	pass

if len(sys.argv) < 2:
	port = int(raw_input('port number = '))
	ip_addr = raw_input('ip address = ')
	real_or_fake = int(raw_input('do you want real data or fake data?\n press 1 for real, press 2 for fake'))
else:
	port = int(sys.argv[1])
	ip_addr = sys.argv[2]
	real_or_fake = int(sys.argv[3])
n = 1

if real_or_fake == 1:#real
	while os.path.isfile(filename) == False:
		print 'waiting for detection ...'
		time.sleep(1)
	data = open(filename, 'r')
	msg = data.readline()
	socksend(msg)
	data.close()
	print 'sending real detection data to server: \n'
	print str(msg)
else:#fake
	print 'sending fake detection data to the server'
	msg = '1475978415.01,5.40390060322,1,school.testing.10.08.16,$GPGGA,205704.000,3849.3529,N,07701.5355,W,1,08,1.2,10.0,M,-33.5,M,,0000*54'
	time.sleep(1)
	socksend(msg)
