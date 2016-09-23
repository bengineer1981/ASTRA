#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import matplotlib.pyplot as plt
import math
import time
import numpy
import sys
import os


def reformat(msg):
	splitline= msg.split(',')#splits the line when a comma is read
	if splitline[0] == '$GPGGA':#if line begins with $GPGGA
		time = splitline[1]#information we we wish to extract
		latitude= splitline[2]#line number is the order the data is written in the GPGGA line
		latDir=splitline[3]
		longitude=splitline[4]
		longDir=splitline[5]
		print 'total msg: ',msg#prints the entire line
		print 'time: ',time
		print 'lat: ', latitude
		print 'long: ', longitude


#get ip addr and port #
ip_addr = '0.0.0.0'
print int(sys.argv[1])
if int(sys.argv[1]) > 999:
    port = int(sys.argv[1])
else:
    print 'you entered a port number less than 1000'
    port = int(raw_input("what port# would you like to listen to? "))
print "listening on IP address: ", ip_addr
print "listening on port: ", port
#build socket using above user input
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((ip_addr, port))
#serversocket.listen(5) # become a server socket, maximum 5 connections
while 1:
	msg = serversocket.recv(128)
	reformat(msg)



