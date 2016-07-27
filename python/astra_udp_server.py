#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import matplotlib.pyplot as plt
import math
import time
import numpy
import sys
import os


#function to plot based on received information
def plot_more_stuff(theta,node_num):
    theta = math.radians(theta)
    # # Polar plotting
    fig = plt.figure(node_num)  # Size
    ax = plt.subplot(111, polar=True)  # Create subplot
    plt.grid(color='#888888')  # Color the grid
    ax.set_theta_zero_location('N')  # Set zero to North
    mic1 = math.radians(0)
    mic2 = math.radians(0)
    mic3 = math.radians(-120)
    mic4 = math.radians(120)
    ax = plt.subplot(111,polar=True)
    ycoords = [0,100,100,100]
    xcoords = [mic1,mic2,mic3,mic4]
    ax.plot((0,theta),(0,200) , c = 'r', linewidth = 3)
    ax.plot((0,mic2),(0,100) , c = 'b', linewidth = 3)
    ax.plot((0,mic3),(0,100) , c = 'b', linewidth = 3)
    ax.plot((0,mic4),(0,100) , c = 'b', linewidth = 3)
    ax.scatter(xcoords,ycoords, c = 'b', linewidth = 7)
    ax.annotate('detector mic', xy=(0, 0), xytext=(24,19))
    ax.annotate('mic2(North)', xy=(0, 0), xytext=(mic2, 115))
    ax.annotate('mic3', xy=(0, 0), xytext=(mic3, 125))
    ax.annotate('mic4', xy=(0, 0), xytext=(mic4, 150))
    ax.annotate(('vector to source:\n %f degrees' % math.degrees(theta)),xy = (0,0),xytext=(theta-25,300))
    ax.annotate('plot for node number: %d' % node_num, xy=(0, 0), xytext=(100,300))

def reformat(msgs):
    node_count = 0
    # re-format data
    for msg in msgs:
        word = []
        message_lst = []
        count = len(msg)
        for char in msg:
            if char != ',' and count > 0:
                word.append(char)
                count -= 1
                # print 'count: ', count
            elif char == ',' and count > 0:
                word = ''.join(word)
                message_lst.append(word[:])
                word = []
                count -= 1
        word = ''.join(word)
        message_lst.append(word[:])
        message_lst = [float(message_lst[0]), float(message_lst[1]), int(message_lst[2])]
        # print 'converted message_lst: ',message_lst
        node_num = message_lst[2]
        shot_time = message_lst[0]
        theta = message_lst[1]
        # show user the metrics received from a node (timestamp, node number, shot direction
        print "time of shot: ", shot_time
        print "node number: ", node_num
        node_count += 1
        print "direction of shot: %f degrees counterclockwise from north" % theta
        print 'node count: ', node_count
        # send data received from node
        plot_more_stuff(theta, node_num)

node_count = 0
#get ip addr and port #
ip_addr = '0.0.0.0'
port = int(raw_input("what port# would you like to listen to? "))
print "listening on IP address: ", ip_addr
print "listening on port: ", port
#build socket using above user input
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((ip_addr, port))
#serversocket.listen(5) # become a server socket, maximum 5 connections
shutdown = 0
timeout = None
quick_list = []
#wait for connection
while node_count < 3 and shutdown == 0:
    try:
        print "number of nodes that have reported in so far: ",node_count
        serversocket.settimeout(timeout)
        print 'waiting for data from node(s)'
        #connection, address = serversocket.accept()
        data = serversocket.recv(128)
        quick_list.append(data)
        node_count +=1
        print timeout
        if timeout == None:
                timeout = 5
    except socket.timeout:
        print "no other nodes reported gunshots in a logical amount of time"
        break
reformat(quick_list)
print "plotting data"
plt.show()
