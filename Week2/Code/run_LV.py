#!/usr/bin/python

""" 
   Python script to run LV scripts
"""
import sys

from IPython import get_ipython
ipython = get_ipython()
ipython.magic("%%run -p LV1.py")
## All three same input to demonstrate differences between methods
ipython.magic("%%run -p LV2.py %f %f %f %f" % (1.1, 0.15, 1.45, 0.7))
ipython.magic("%%run -p LV3.py %f %f %f %f" % (1.1, 0.15, 1.45, 0.7))
ipython.magic("%%run -p LV4.py %f %f %f %f" % (1.1, 0.15, 1.45, 0.7))

#exit
