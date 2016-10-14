#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import matplotlib.pyplot as plt
import math
import time
import numpy
import sys
import os


def fix_lat_long(lat,long,latdir,longdir):
    #reformat latitude
    print 'old lat ', lat
    lat = ''.join(lat.split('.'))
    if latdir == 'S':
        lat = float('-'+lat[:2]+'.'+lat[2:])
    else:
        lat = float(lat[:2] + '.' + lat[2:])
    print 'new lat ',lat
    print 'new lat type ',type(lat)
    #reformat longitude
    print 'old long ', long
    long = ''.join(long.split('.'))
    if longdir == 'W':
        long = float('-'+long[:3]+'.'+long[3:])
    else:
        long = float(long[:2] + '.' + long[2:])
    print 'new long ',long
    print 'new long type ',type(long)
    return [lat,long]

def reformat(msg):

    splitline= msg.split(',')#splits the line when a comma is read
    if splitline[4] == '$GPGGA':#if line begins with $GPGGA
        node_time = splitline[0]
        angle = splitline[1]
        node_num = splitline[2]
        test_name = splitline[3]
        time = splitline[5]#information we we wish to extract
        latitude= splitline[6]#line number is the order the data is written in the GPGGA line
        latDir=splitline[7]
        longitude=splitline[8]
        longDir=splitline[9]
        #print 'total msg: ',msg#prints the entire line
        print 'node time: ', node_time
        print 'angle: ',angle
        node_num = int(node_num)
        print 'node number: ',node_num
        print 'test name: ',test_name
        print 'time: ',time
        print 'lat: %s latDir: %s' % (latitude, latDir)
        print 'long: %s longDir: %s' % (longitude, longDir)
        new_info = fix_lat_long(latitude,longitude,latDir,longDir)
        print 'new info: ',new_info



#get ip addr and port #
ip_addr = '0.0.0.0'
msg_num = 1
if len(sys.argv) == 1:
    print 'you didnt type a port number argument when you ran the script'
    port = int(raw_input("what port# would you like to listen to?"))
elif int(sys.argv[1]) > 999:
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
    print '\nmsg #: %d' % msg_num
    msg_num += 1
    reformat(msg)



