#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
import csv
import numpy
from gnuradio import gr
import time
import math
import socket
import serial
import sys
import matplotlib.pyplot as plt

class xcorr_ts_ff(gr.sync_block):
    """
    docstring for block xcorr_ts_ff
    """
    def __init__(self,samp_window,samp_rate,node_number,ip_addr,port_num,center_mic_offset,mic_distance,test_number):
        gr.sync_block.__init__(self,
            name="xcorr_ts_ff",
            in_sig=[numpy.float32,numpy.float32,numpy.float32,numpy.float32,numpy.float32],
            out_sig=[numpy.float32])
        self.samp_window = samp_window
        self.samp_rate = samp_rate
        self.trig_in_tracker = []
        self.in1_tracker = []
        self.in2_tracker = []
        self.in3_tracker = []
        self.in4_tracker = []
        self.fixed_dly = 10
        self.limiter = 1
        self.total_capture_len = samp_window
        self.captured_samp_count = 0
        self.captured_samps1 = []
        self.captured_samps2 = []
        self.captured_samps3 = []
        self.captured_samps4 = []
        self.capturing = 0
        self.out_msg = [0,0,node_number,test_number] # [timestamp,angle]
        self.ip_address = ip_addr
        self.port_num = port_num
        self.center_mic_offset = center_mic_offset
        self.mic_distance = mic_distance
        self.test_number = test_number

    # def tracker(self, trig_in,in1,in2,in3,in4):
    #     if len(self.trig_in_tracker) == 0:
    #         self.trig_in_tracker[:] = trig_in
    #     else:
    #         self.trig_in_tracker[len(self.trig_in_tracker):] = trig_in
    #     print "trig_in_tracker: ", self.trig_in_tracker
    #     print "length of trig_in_tracker: ",len(self.trig_in_tracker)
    #     if len(self.in1_tracker) == 0:
    #         self.in1_tracker[:] = in1
    #     else:
    #         self.in1_tracker[len(self.in1_tracker):] = in1
    #     print "in1_tracker: ", self.in1_tracker
    #     print "length of in1_tracker: ", len(self.in1_tracker)
    #     if len(self.in2_tracker) == 0:
    #         self.in2_tracker[:] = in2
    #     else:
    #         self.in2_tracker[len(self.in2_tracker):] = in2
    #     print "in2_tracker: ", self.in2_tracker
    #     print "length of in2_tracker: ", len(self.in2_tracker)
    #     if len(self.in3_tracker) == 0:
    #         self.in3_tracker[:] = in3
    #     else:
    #         self.in3_tracker[len(self.in3_tracker):] = in3
    #     print "in3_tracker: ", self.in3_tracker
    #     print "length of in3_tracker: ", len(self.in3_tracker)
    #     if len(self.in4_tracker) == 0:
    #         self.in4_tracker[:] = in4
    #     else:
    #         self.in4_tracker[len(self.in4_tracker):] = in4
    #     print "in4_tracker: ", self.in4_tracker
    #     print "length of in4_tracker: ", len(self.in4_tracker)

    def angler(self,lags):
        print 'lags in angler', lags
        # speed of sound
        c = 343  # m/s
        elem_dist = self.mic_distance  # meters
        # sampling rate
        fs = 44100.0  # samps/sec
        third_mic = lags.index([max(lags)]), int(max(lags))
        print "third mic w/o abs val: ",third_mic
        lags[third_mic[0]] = -99999
        second_mic = lags.index([max(lags)]), int(max(lags))
        print "second mic w/o abs val: ",second_mic
        lags[second_mic[0]] = -99999
        first_mic = lags.index([max(lags)]), int(max(lags))
        print "first mic w/o abs val: ",first_mic
        lags[first_mic[0]] = -99999
        print 'first mic to receive hit is: ', first_mic[0] + 2
        print 'second mic to receive hit is: ', second_mic[0] + 2
        print 'third mic to receive hit is: ', third_mic[0] + 2
        t_delay = math.fabs(first_mic[1]) / fs
        print "t_delay is: ", t_delay
        print "distance (x = c*t_delay) is: ", c * t_delay
        theta = math.degrees(math.acos((c * t_delay) / elem_dist))
        print 'angle between detector and first mic (theta = invcos(c*t_delay)/elem_dist): ', theta
        print "determining which side its on using which mics came after"
        if first_mic[0] + 2 == 2 and second_mic[0] + 2 == 4:
            theta = theta
        elif first_mic[0] + 2 == 2 and second_mic[0] + 2 == 3:
            theta = -theta
        elif first_mic[0] + 2 == 3 and second_mic[0] + 2 == 2:
            theta = theta + 240
        elif first_mic[0] + 2 == 3 and second_mic[0] + 2 == 4:
            theta = 240 - theta
        elif first_mic[0] + 2 == 4 and second_mic[0] + 2 == 3:
            theta = 120 + theta
        elif first_mic[0] + 2 == 4 and second_mic[0] + 2 == 2:
            theta = 120 - theta
        else:
            print "missed a case here"
        print "theta after looking at other mics: ", theta
        first_mic_and_angle = [first_mic[0] + 2, theta]
        self.out_msg[1] = theta
        print "final message: 'node number %d, saw a shot at time: %f, at angle: %f" % (self.out_msg[2],self.out_msg[0],self.out_msg[1])
        return first_mic_and_angle

    def xcorr(self, mic1_detector, mic2_locator, mic3_locator, mic4_locator):
        autocorr = numpy.correlate(mic1_detector, mic1_detector, "same")
        mxind0 = numpy.where(autocorr == max(autocorr))
        mxind0 = mxind0[0][0]
        middle = mxind0
        print "ch-ch-ch-ch-ch-changes"
        print 'location of initial detection is: ', mxind0
        print "len autocorr: ", len(autocorr)

        #cross correlate detector with element 2
        xcorr1 = numpy.correlate(mic1_detector, mic2_locator, "same")
        mxind1 = numpy.where(xcorr1 == max(xcorr1))
        mxind1 = mxind1[0][0]
        print 'mxind1 is: ', mxind1
        print 'middle', middle
        lag1 = middle - mxind1
        print "len xcorr1: ", len(xcorr1)
        print "lag1: ",lag1
        #lag1 = self.center_mic_offset - lag1
        print 'lag1 after delay compensation: ',lag1

        # cross correlate detector with element 3
        xcorr2 = numpy.correlate(mic1_detector, mic3_locator, "same")
        mxind2 = numpy.where(xcorr2 == max(xcorr2))
        mxind2 = mxind2[0][0]
        print 'mxind2 is: ', mxind2
        lag2 = middle - mxind2
        print "len xcorr2: ", len(xcorr2)
        print "lag2: ", lag2
        #lag2 = self.center_mic_offset - lag2
        print 'lag1 after delay compensation: ',lag2

        # cross correlate detector with element 4
        xcorr3 = numpy.correlate(mic1_detector, mic4_locator, "same")
        mxind3 = numpy.where(xcorr3 == max(xcorr3))
        mxind3 = mxind3[0][0]
        print 'mxind3 is: ', mxind3
        lag3 = middle - mxind3
        print "len xcorr3: ", len(xcorr3)
        print "lag3: ", lag3
        #lag3 = self.center_mic_offset - lag3
        print 'lag1 after delay compensation: ',lag3
        lags = [lag1,lag2,lag3]
        self.angler(lags)

    def capture(self, in1, in2, in3, in4):
        in1 = in1.tolist()
        in2 = in2.tolist()
        in3 = in3.tolist()
        in4 = in4.tolist()
        if self.total_capture_len > 0 and len(self.captured_samps1) == 0:
            print "lengths of in1-4 in 1st stage of capture: ", len(in1), len(in2), len(in3), len(in4)
            print "first if statement satisfied, total_captured_len = ", self.total_capture_len
            self.captured_samps1 = in1
            self.captured_samps2 = in2
            self.captured_samps3 = in3
            self.captured_samps4 = in4
            self.total_capture_len = self.total_capture_len - len(in1)
            print 'len of captured samps1: ', len(self.captured_samps1)
        elif self.total_capture_len > 0 and len(in1) <= self.total_capture_len:
            print "second if statement satisfied, total_captured_len = ", self.total_capture_len
            self.captured_samps1[len(self.captured_samps1):] = in1
            self.captured_samps2[len(self.captured_samps2):] = in2
            self.captured_samps3[len(self.captured_samps3):] = in3
            self.captured_samps4[len(self.captured_samps4):] = in4
            self.total_capture_len = self.total_capture_len - len(in1)
            print 'len of captured samps1: ',len(self.captured_samps1)
        elif self.total_capture_len > 0 and len(in1) > self.total_capture_len:
            print "third if statement satisfied, total_captured_len = ", self.total_capture_len
            self.captured_samps1[len(self.captured_samps1):] = in1[:self.total_capture_len]
            self.captured_samps2[len(self.captured_samps2):] = in2[:self.total_capture_len]
            self.captured_samps3[len(self.captured_samps3):] = in3[:self.total_capture_len]
            self.captured_samps4[len(self.captured_samps4):] = in4[:self.total_capture_len]
            self.total_capture_len = self.total_capture_len - len(in1[:self.total_capture_len])
            print 'len of captured samps1: ', len(self.captured_samps1)
        elif self.total_capture_len == 0:
            print "************************************"
            print "fourth if statement satisfied, total_captured_len = ", self.total_capture_len
            print 'start writing data'
            data1 = self.captured_samps1
            data2 = self.captured_samps2
            data3 = self.captured_samps3
            data4 = self.captured_samps4
            with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in1file%s.csv' % self.test_number,'wb') as f1:
                writer = csv.writer(f1)
                writer.writerow(data1)
            with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in2file%s.csv' % self.test_number,'wb') as f2:
                writer = csv.writer(f2)
                writer.writerow(data2)
            with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in3file%s.csv' % self.test_number,'wb') as f3:
                writer = csv.writer(f3)
                writer.writerow(data3)
            with open('/home/ben/Desktop/senior_design/gnuradio/data_files/in4file%s.csv' % self.test_number,'wb') as f4:
                writer = csv.writer(f4)
                writer.writerow(data4)
            self.capturing = 0
            print "data written"
            print "len of captured samps1: ", len(self.captured_samps1)
            print "calling xcorr on captured samples"
            print "************************************"
            self.xcorr(self.captured_samps1,self.captured_samps2,self.captured_samps3,self.captured_samps4)
        else:
            "something i didn't think of in capture function"

    def message_write(self,msg):
        filename = "/home/ben/Desktop/senior_design/python/gps.txt"
        f = open(filename, 'r')
        gps = f.read()
        f.close()
        msg.append(gps)
        msg = str(msg[0]),str(msg[1]),str(msg[2]),str(msg[3]),str(msg[4])
        msg = ','.join(msg)
        detection_file = '/home/ben/Desktop/senior_design/python/detection.txt'
        d = open(detection_file,'w')
        d.write(msg)
        print 'this message was just written to a file', msg
        d.close()
        # clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # clientsocket.connect((self.ip_address, self.port_num))
        # clientsocket.send(msg+'n')
        #clientsocket.close()


    def work(self, input_items, output_items):
        trig_in = input_items[0]
        in1 = input_items[1] #in1 is the whole list, in1[h] is the single element of the list
        in2 = input_items[2]
        in3 = input_items[3]
        in4 = input_items[4]
        out = output_items[0]
        h = 0
        trig_index = 0

        # print "len in1: ",len(in1)
        # print "len in2: ",len(in2)
        # print "len in3: ",len(in3)
        # print "len in4: ",len(in4)
        while h < len(output_items[0]):
            val = trig_in[h]
            if val == 1 and self.limiter ==1:
                print "************************************"
                print "triggering value is: ", val
                print "at index: ",h
                self.out_msg[0] = time.time()
                print "timestamp is: ", self.out_msg[0]
                print "setting enable to 'on'"
                print "capturing %d samples (%0.3f sec) of signal in scheduler dependent chunks." % (self.samp_window,float(self.samp_window)/self.samp_rate)
                print "************************************"
                self.limiter = 0
                self.capturing = 1
                trig_index = h
                output_items[0][h] = input_items[0][h]
                h = len(output_items[0])
            else:
                output_items[0][h] = input_items[0][h]
            h = h+1
        if self.capturing ==1 and len(self.captured_samps1) == 0:
            print "************************************"
            print "starting sample capture, because capture flag is high and captured samps == 0"
            print "will only grab samples from trigger index on"
            print "capturing %d samples now" % len(in1[trig_index:])
            print "************************************"
            self.capture(in1[trig_index:], in2[trig_index:], in3[trig_index:], in4[trig_index:])
        elif self.capturing == 1 and self.total_capture_len > 0:
            print "************************************"
            print "continuing to capture samples"
            print "capturing %d samples now" % len(in1)
            print "************************************"
            self.capture(in1,in2,in3,in4)
        elif self.capturing == 1 and self.total_capture_len == 0:
            print 'capturing flag still high, but total capture length == 0'
            self.capture(in1,in2,in3,in4)
            print 'writing message to file'
            self.message_write(self.out_msg)
            h = 0
            trig_index = 0
        out[:] = trig_in

        return len(output_items[0])

