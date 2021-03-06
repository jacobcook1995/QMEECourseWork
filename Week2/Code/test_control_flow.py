#!/usr/bin/python

"""Some functions exemplifying the use of control statements"""
#docstrings are considered part of the running code (normal comments are
#stripped). Hence you can access your docstrings at run time
__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.0.1'

# imports
import sys # module to interface our program with the operating system
import doctest # Import the doctest module

#constants can go here

# functions can go here

def even_or_odd(x=0): # if not specified, x should take value 0.
	
	"""Find whether a number x is even or odd.
	
	>>> even_or_odd(10)
	'10 is Even!'
	
	>>> even_or_odd(5)
	'5 is Odd!'
	
	whenever a float is provided, then the closest integer is used:
	>>> even_or_odd(3.2)
	'3 is Odd!'
	
	in case of negative numbers the positive is taken:
	>>> even_or_odd(-2)
	'-2 is Even!'
	
	"""
	#Define function to be tested
	if x % 2 == 0:
		return "%d is Even!" % x
	return "%d is Odd!" % x
	
## I SUPPRESSED THIS BLOCK: WHY?
	
# def main(argv):
	# sys.exit("don't want to do this right now!")
	# print even_or_odd(22)
	# print even_or_odd(33)
	# return 0
		
# if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		# status = main(sys.argv)
doctest.testmod() # To run with embedded tests
