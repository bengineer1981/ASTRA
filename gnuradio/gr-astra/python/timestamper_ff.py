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

import time
import numpy
from gnuradio import gr

class timestamper_ff(gr.basic_block):
    """
    docstring for block timestamper_ff
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="timestamper_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        j = 0
        print "len input_items: ",len(input_items[0])
        print "len output_items: ",len(output_items[0])
        print "input_items: ",input_items[0]
        while j < len(output_items[0]):
            val = input_items[0][j]
            print "val: ",val
            if val >= 1:
                print "************************************"
                print "triggering value is: ", val
                print "at index: ",j
                print "timestamp is: ", time.time()
                print "************************************"
                output_items[0][j] = input_items[0][j]
            else:
                print "nothing to see at index: ",j
                print "non-triggering value is: ", val
                output_items[0][j] = input_items[0][j]
            j = j+1

        #consume(0, len(input_items[0]))
        self.consume_each(len(output_items[0]))
        #print "the current time is now %d" % (time.time())
        #time.sleep(1)
        return len(output_items[0])
