#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ben/Desktop/senior_design/gnuradio/gr-astra/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/ben/Desktop/senior_design/gnuradio/gr-astra/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/ben/Desktop/senior_design/gnuradio/gr-astra/build/swig:$PYTHONPATH
/usr/bin/python2 /home/ben/Desktop/senior_design/gnuradio/gr-astra/python/qa_peak_detect_ff.py 
