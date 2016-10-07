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

import numpy
from gnuradio import gr

class peak_detect_ff(gr.sync_block):
    """
    docstring for block peak_detect_ff
    """
    def __init__(self, percent,window_size):
        self.percent = .01*percent
        self.window_size = window_size
        self.window = []
        self.limiter = 1
        self.init_avg = 1
        self.avg_compare = []
        self.potential_max = 0
        gr.sync_block.__init__(self,
            name="peak_detect_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
    def averager(self, window):
        avg_val = (sum(window)/len(window))
        if avg_val > 0:
            avg_val +=1
        else:
            avg_val = avg_val
        return avg_val
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        h = 0
        for val in in0:
            if len(self.window) < self.window_size-1:
                self.window.append(val)
            else:
                self.window.append(val)
                avg = self.averager(self.window)
                #print 'average', avg
                if len(self.avg_compare) < 2:
                    self.avg_compare.insert(0,avg)
                else:
                    self.avg_compare.pop(1)
                    self.avg_compare.insert(0,avg)
                    print self.avg_compare
                    delta = abs(self.avg_compare[0]-self.avg_compare[1])
                    #print "avg_compare delta: ",delta
            #if self.init_avg == 0:
                    if self.avg_compare[0] > self.avg_compare[1]*self.percent:# and self.limiter ==1:
                        self.potential_max = self.avg_compare[0]
                        print "thresh potentially exceeded with potential max: ",self.potential_max
                        print "thresh is avg_compare[1] * self.percent = ",(self.avg_compare[1]*self.percent)
                        output_items[0][h] = 1

                self.window = []
                self.init_avg = 0
                    #self.limiter = 0
            #else:
            #    output_items[0][h] = 0
            h +=1
        #out[:] = in0
        #print output_items
        return len(output_items[0])

