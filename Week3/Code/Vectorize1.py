#!/usr/bin/python

"""Vectorize.py: a script to demonstrate the relative speed of Python vs R
   Sums a matrix in order to demonstrate this
"""

__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

import sys
import numpy as np

M = np.random.random((1000, 1000))

def Sum_All_Elements(M):
	Tot = 0.
	i = 0
	j = 0
	Dim = M.shape
	while i < Dim[0]:
		while j < Dim[1]:
			Tot = Tot + M[i,j]
			j += 1
		i += 1
	return Tot

def main(argv):
	Sum = Sum_All_Elements(M)
	return 0

if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)
