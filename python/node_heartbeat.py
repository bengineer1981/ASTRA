#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
import serial
import sys
import os
import errno
from socket import error as socket_error


def socksend(msg):
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #clientsocket.connect((ip_addr, port))
		# uncomment .connect and change sendto(msg,ip,port) to send(msg)
        clientsocket.sendto(msg,(ip_addr, port))
        return 1
    except socket_error as serr:
        if serr.errno != errno.ECONNREFUSED:
            raise serr
        print '***NO CONNECTION***'
        return 0

if len(sys.argv) < 5:
    port = int(raw_input('port number = '))
    ip_addr = raw_input('ip address = ')
    node_number = int(raw_input('node # = '))
    real_or_fake = int(raw_input('do you want real data or fake data?\n press 1 for real, press 2 for fake'))
else:
    port = int(sys.argv[1])
    ip_addr = sys.argv[2]
    node_number = int(sys.argv[3])
    real_or_fake = int(sys.argv[4])
print '\n\n*************************'
print "port: ",port
print "ip address: ",ip_addr
print "node number: ",node_number
if real_or_fake ==1:
    print "real data (option 1)"
else:
    print "fake data (option 2)"
print '*************************\n'
n = 1

detect_filename = '/home/ben/Desktop/senior_design/python/detection.txt'
try:
    os.remove(detect_filename)
except OSError:
    pass


if real_or_fake == 1: #real
    while os.path.isfile(detect_filename) == False:
        ser = serial.Serial('/dev/ttyUSB0', 4800, timeout=5)
        msg = ser.readline()
        splitline = msg.split(',')
        if splitline[0] == '$GPGGA':  # if line begins with $GPGGA
            filename = "/home/ben/Desktop/senior_design/python/gps.txt"
            f = open(filename, 'w')
            f.write(msg)
            f.close()
            # print 'splitline[0]: ',splitline[0]
            gps_time = splitline[1]  # information we we wish to extract
            latitude = splitline[2]  # line number is the order the data is written in the GPGGA line
            latDir = splitline[3]
            longitude = splitline[4]
            longDir = splitline[5]
            print 'time: ', gps_time
            print 'lat: ', latitude
            print 'long: ', longitude
            print 'sending real heartbeat info to server'
            msg = str(time.time())+',,'+str(node_number)+',no test number,'+str(msg)
            socksend(msg)
            print 'MESSAGE #: ' + str(n) + '\nthis is the non-detect message with GPS from the puck: \n' + msg
            n += 1
    data = open(detect_filename, 'r')
    msg = data.readline()
    socksend(msg)
    data.close()
    print 'sending real detection data to server: \n'
    print str(msg)

else: # 2 -->fake
    m = 1
    while m < 10:
        msg = str(time.time())+',,1,school.testing.10.08.16,$GPGGA,205704.000,3849.3529,N,07701.5355,W,1,08,1.2,10.0,M,-33.5,M,,0000*54'
        time.sleep(1)
        x = socksend(msg)
        if x == 1:
            print 'sending fake GPS data to the server'
            n += 1
            m += 1
        else:
            print 'not sending data'
    print 'sending fake DETECTION data to the server'
    msg = str(time.time())+',5.40390060322,1,school.testing.10.08.16,$GPGGA,205704.000,3849.3529,N,07701.5355,W,1,08,1.2,10.0,M,-33.5,M,,0000*54'
    socksend(msg)
