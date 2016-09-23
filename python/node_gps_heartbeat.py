#!/usr/bin/env python
import socket
import serial #python package for reading serial ports
ser=serial.Serial( '/dev/ttyUSB0', 4800, timeout = 5)#creates serial vairable and sets port to read from and speed to read from port. Timeout prevents program from waiting more than X seconds in case of infinite loop
ip_addr = '0.0.0.0'
port = 5557
while 1:
	line = ser.readline()#reads a line of data from port
	splitline= line.split(',')#splits the line when a comma is read
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientsocket.connect((ip_addr,port))
	msg = line
	print "running on ip: %s \nrunning on port: %s" % (ip_addr,port)
	filename = "gps.txt"
	if splitline[0] == '$GPGGA':#if line begins with $GPGGA
		print 'in if statement'
		print 'splitline[0]: ',splitline[0]
		f = open(filename,'w')
		f.write(line)
		f.close()
		time = splitline[1]#information we we wish to extract
		latitude= splitline[2]#line number is the order the data is written in the GPGGA line
		latDir=splitline[3]
		longitude=splitline[4]
		longDir=splitline[5]
		print 'time: ',time
		print 'lat: ', latitude
		print 'long: ', longitude
		print 'message being sent to server',msg
		clientsocket.send(msg)
		clientsocket.close()
	else:
		clientsocket.close()
		#break

