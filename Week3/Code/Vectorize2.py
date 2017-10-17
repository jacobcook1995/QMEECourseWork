#!/usr/bin/python

"""Vectorize.py: a script to demonstrate the relative speed of Python vs R
   Implements the stochastic Ricker method to do this
"""

__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

import sys
import numpy as np
import scipy as sc
import random


# Runs the stochastic (with gaussian fluctuations) Ricker Eqn .

def stochrick(p0=np.random.random(1000),r=1.2,K=1,sigma=0.2,numyears=100):
	#initialize
	number_populations = len(p0)
	N = sc.zeros((numyears+1,number_populations))
	N[0,]=p0
	pop = 0
	while pop < number_populations: #loop through the populations
		yr = 1
		while yr < numyears: #for each pop, loop through the years
			N[yr,pop]<-N[yr-1,pop]*np.exp(r*(1-N[yr-1,pop]/K)+random.uniform(0., 1.))
			yr += 1
		pop += 1
	
	return N

 

# Now write another code called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 
def stochrickvect(p0=np.random.random(1000),r=1.2,K=1,sigma=0.2,numyears=100):
	# initialize as a vector
	number_populations = len(p0)
	N = sc.zeros((numyears+1,number_populations))
	N[0,:]=p0
	yr = 0
	while yr < numyears: #for each pop, loop through the years
		rannums = np.random.rand(number_populations,1)
		Ranums = rannums.T
		N[yr+1,:] = N[yr,:]*np.exp(r*(1-N[yr,:]/K)+Ranums)
		yr += 1
      
	return (N)

def main(argv):
	stochrick()
	stochrickvect()
	return 0

if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)
