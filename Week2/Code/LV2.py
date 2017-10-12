#!/usr/bin/python

""" The typical Lotka-Volterra Model simulated using scipy
    This script take user input to set model parameters
"""

__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

import sys 
import scipy as sc 
import scipy.integrate as integrate
import pylab as p #Contains matplotlib for plotting

K = 20.

# import matplotlip.pylab as p 


def dR_dt(pops, t=0):
    """ Returns the growth rate of predator and prey populations at any 
    given time step """
    
    R = pops[0]
    C = pops[1]
    dRdt = r*R - r*R*R/K - a*R*C 
    dydt = -z*C + e*a*R*C
    
    return sc.array([dRdt, dydt])


def main(argv):
	global r
	global a
	global z
	global e
	# Define parameters:
	if len(sys.argv) > 1:
		r = float(sys.argv[1])
	else:
		r = 1. # Resource growth rate
	if len(sys.argv) > 2:
		a = float(sys.argv[2])
	else:
		a = 0.1 # Consumer search rate (determines consumption rate) 
	if len(sys.argv) > 3:
		z = float(sys.argv[3])
	else:
		z = 1.5 # Consumer mortality rate
	if len(sys.argv) > 4:
		e = float(sys.argv[4])
	else:
		e = 0.75 # Consumer production efficiency
	
	# Now define time -- integrate from 0 to 15, using 1000 points:
	t = sc.linspace(0, 15,  1000)
	
	x0 = 10
	y0 = 5 
	z0 = sc.array([x0, y0]) # initials conditions: 10 prey and 5 predators per unit area

	pops, infodict = integrate.odeint(dR_dt, z0, t, full_output=True)

	infodict['message']     # >>> 'Integration successful.'

	prey, predators = pops.T # What's this for?
	f1 = p.figure() #Open empty figure object
	p.plot(t, prey, 'g-', label='Resource density') # Plot
	p.plot(t, predators  , 'b-', label='Consumer density')
	p.grid()
	p.legend(loc='best')
	p.xlabel('Time')
	p.ylabel('Population')
	p.title('Consumer-Resource population dynamics:\n with r = %f, a = %f, z = %f, e = %f' % (r, a, z, e))
	p.show()
	f1.savefig('../Results/prey_and_predators_2.pdf') #Save figure
	
	return 0



if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)
