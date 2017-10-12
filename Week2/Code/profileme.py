#!/usr/bin/python

"""Very useless program to test running the profileing"""
   
__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

# imports
import sys


def a_useless_function(x):
	y = 0
	# eight zeros!
	for i in xrange(100000000):
		y = y + i
	return 0
	
def a_less_useless_function(x):
	y = 0
	# five zeros!
	for i in xrange(100000):
		y = y + i
	return 0
	
def some_function(x):
	print x
	a_useless_function(x)
	a_less_useless_function(x)
	return 0
	
def main(argv):
	some_function(1000)
	return 0

if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)

