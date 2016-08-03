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
    def __init__(self, thresh):
        self.thresh = thresh
        self.limiter = 1
        gr.sync_block.__init__(self,
            name="peak_detect_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        h = 0
        for val in in0:
            if val > self.thresh:# and self.limiter ==1:
                print "thresh exceeded, val is: ",val
                output_items[0][h] = 1
                #self.limiter = 0
            else:
                output_items[0][h] = 0
            h +=1
        #out[:] = in0
        #print output_items
        return len(output_items[0])

