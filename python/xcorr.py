#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import math
import time
import numpy
import sys
import os
import matplotlib.pyplot as plt

def get_streams_from_files(test_number):
#for gnuradio output file
    with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in1file%s.csv' % test_number, 'rb') as f1:
#for matlab output file
    #with open("/home/ben/Desktop/senior_design/gnuradio/data_files/stream1.csv",'rb') as f1:
        reader = csv.reader(f1)
        in1 = []
        for row in reader:
            print len(row)
            for num in row:
                num = float(num)
                in1.append(num)
        print len(in1)

# for gnuradio output file
    with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in2file%s.csv' % test_number, 'rb') as f2:
# for matlab output file
    #with open("/home/ben/Desktop/senior_design/gnuradio/data_files/stream2.csv", 'rb') as f2:
        reader = csv.reader(f2)
        in2 = []
        for row in reader:
            print len(row)
            for num in row:
                num = float(num)
                in2.append(num)
        print len(in2)

# for gnuradio output file
    with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in3file%s.csv' % test_number, 'rb') as f3:
#  for matlab output file
    #with open("/home/ben/Desktop/senior_design/gnuradio/data_files/stream3.csv", 'rb') as f3:
        reader = csv.reader(f3)
        in3 = []
        for row in reader:
            print len(row)
            for num in row:
                num = float(num)
                in3.append(num)
        print len(in3)

# for gnuradio output file
    with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in4file%s.csv' % test_number, 'rb') as f4:
# for matlab output file
    #with open("/home/ben/Desktop/senior_design/gnuradio/data_files/stream4.csv", 'rb') as f4:
        reader = csv.reader(f4)
        in4 = []
        for row in reader:
            print len(row)
            for num in row:
                num = float(num)
                in4.append(num)
        print len(in4)
    ins = [in1, in2, in3, in4]
    return ins

def xcorr(mic1_detector, mic2_locator, mic3_locator, mic4_locator):
    # cross correlate detector with element 2
    autocorr = numpy.correlate(mic1_detector, mic1_detector, "same")
    mxind0 = numpy.where(autocorr == max(autocorr))
    mxind0 = mxind0[0][0]
    middle = mxind0
    print 'location of initial detection is: ', middle
    print "len autocorr: ", len(autocorr)
    plt.figure(5)
    plt.plot(autocorr)
    #plt.show()
    xcorr1 = numpy.correlate(mic1_detector, mic2_locator, "same")
    mxind1 = numpy.where(xcorr1 == max(xcorr1))
    mxind1 = mxind1[0][0]
    print 'mxind1 is: ',mxind1
    print 'middle', middle
    lag1 = middle - mxind1
    print "len xcorr1: ", len(xcorr1)
    print "lag1: ", lag1

    # cross correlate detector with element 3
    xcorr2 = numpy.correlate(mic1_detector, mic3_locator, "same")
    mxind2 = numpy.where(xcorr2 == max(xcorr2))
    mxind2 = mxind2[0][0]
    print 'mxind2 is: ', mxind2
    lag2 = middle - mxind2
    print "len xcorr2: ", len(xcorr2)
    print "lag2: ", lag2

    # cross correlate detector with element 4
    xcorr3 = numpy.correlate(mic1_detector, mic4_locator, "same")
    mxind3 = numpy.where(xcorr3 == max(xcorr3))
    mxind3 = mxind3[0][0]
    print 'mxind3 is: ', mxind3
    lag3 = middle - mxind3
    print "len xcorr3: ", len(xcorr3)
    print "lag3: ", lag3

    plt.figure(2)
    plt.subplot(411)
    plt.plot(autocorr)
    plt.plot(numpy.argmax(autocorr), max(autocorr), '-rD')
    plt.ylabel('autocorr')

    plt.subplot(412)
    plt.plot(xcorr1)
    plt.plot(numpy.argmax(xcorr1), max(xcorr1), '-bD')
    plt.ylabel('xcorr1')

    plt.subplot(413)
    plt.plot(xcorr2)
    plt.plot(numpy.argmax(xcorr2), max(xcorr2), '-gD')
    plt.ylabel('xcorr2')

    plt.subplot(414)
    plt.plot(xcorr3)
    plt.plot(numpy.argmax(xcorr3), max(xcorr3), '-yD')
    plt.ylabel('xcorr3')
    # if (lag1 or lag2 or lag3) > 100:
    center_mic_offset = 0
    lag1 = lag1-center_mic_offset
    lag2 = lag2-center_mic_offset
    lag3 = lag3-center_mic_offset
    lags = [lag1,lag2,lag3]
    return lags

def angler(lags,mic_dist):
    print 'lags in angler', lags
    #speed of sound
    c = 343 #m/s
    elem_dist = mic_dist #meters
    #sampling rate
    fs = 44100.0 #samps/sec
    third_mic = lags.index([max(lags)]), int(max(lags))
    print "third mic w/o abs val: ", third_mic
    lags[third_mic[0]] = -99999
    second_mic = lags.index([max(lags)]), int(max(lags))
    print "second mic w/o abs val: ", second_mic
    lags[second_mic[0]] = -99999
    first_mic = lags.index([max(lags)]), int(max(lags))
    print "first mic w/o abs val: ", first_mic
    lags[first_mic[0]] = -99999
    print 'first mic to receive hit is: ',first_mic[0]+2
    print 'second mic to receive hit is: ',second_mic[0]+2
    print 'third mic to receive hit is: ',third_mic[0]+2
    print "first_mic[1]: ",first_mic[1]
    print "taking abs val of first mic for calculation purposes"
    print 'first mic abs val: ',math.fabs(first_mic[1])
    t_delay = math.fabs(first_mic[1])/fs
    print "t_delay is: ",t_delay
    print "distance (x = c*t_delay) is: ",c*t_delay
    theta = math.degrees(math.acos((c*t_delay)/elem_dist))
    print 'angle between detector and first mic (theta = invcos(c*t_delay)/elem_dist): ',theta
    print "determining which side its on using which mics came after"
    if first_mic[0]+2 == 2 and second_mic[0]+2 == 4:
        theta = theta
    elif first_mic[0]+2 == 2 and second_mic[0]+2 == 3:
        theta = -theta
    elif first_mic[0]+2 == 3 and second_mic[0]+2 == 2:
        theta = theta+240
    elif first_mic[0]+2 == 3 and second_mic[0]+2 == 4:
        theta = 240-theta
    elif first_mic[0]+2 == 4 and second_mic[0]+2 == 3:
        theta = 120+theta
    elif first_mic[0]+2 == 4 and second_mic[0]+2 == 2:
        theta = 120-theta
    else:
        print "missed a case here"
    print "theta after looking at other mics: ",theta
    first_mic_and_angle = [first_mic[0]+2,theta]
    return first_mic_and_angle

def plot_stuff(in1,in2,in3,in4):
    x1 = in1.index(max(in1))
    y1 = max(in1)
    x2 = in2.index(max(in2))
    y2 = max(in2)
    x3 = in3.index(max(in3))
    y3 = max(in3)
    x4 = in4.index(max(in4))
    y4 = max(in4)
    plt.figure(1)
    plt.subplot(411)
    plt.plot(in1)
    plt.plot(in1.index(max(in1)), max(in1),'-rD')
    #plt.annotate(str(x1), xy=(x1,y1), xytext=(x1,y1))
    plt.ylabel('in1')

    plt.subplot(412)
    plt.plot(in2)
    plt.plot(in2.index(max(in2)), max(in2),'-bD')
    plt.ylabel('in2')

    plt.subplot(413)
    plt.plot(in3)
    plt.plot(in3.index(max(in3)), max(in3),'-gD')
    plt.ylabel('in3')

    plt.subplot(414)
    plt.plot(in4)
    plt.plot(in4.index(max(in4)), max(in4),'-yD')
    plt.ylabel('in4')

    plt.figure(4)
    plt.plot(in1,'r',in2,'b',in3,'g',in4,'y')

def plot_more_stuff(theta):
    theta = math.radians(theta)
    first_mic = elem_num_and_theta[0]
    # # Polar plotting
    fig = plt.figure(5)  # Size
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


##################################################
#--------------------MAIN------------------------#
##################################################

print ('test number example is: AR15.50m.120deg.shot1')
test_number = raw_input('enter test number to analyze: ')
mic_dist = float(raw_input('enter mic_dist: '))
ins = get_streams_from_files(test_number)
#cross_correlate all inputs with in1 and get back lags
result = xcorr(ins[0],ins[1],ins[2],ins[3])
#calculate angle of arrival and first_element to receive signal
elem_num_and_theta = angler(result,mic_dist) #result = lags
plot_stuff(ins[0],ins[1],ins[2],ins[3])
theta = elem_num_and_theta[1]
plot_more_stuff(theta)
plt.show()



