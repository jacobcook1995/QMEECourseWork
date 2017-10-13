#!/usr/bin/python

""" The discrete-time Lotka-Volterra Model simulated using scipy
    This script take user input to set model parameters
"""

__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

import sys 
import scipy as sc 
import scipy.integrate as integrate
import pylab as p #Contains matplotlib for plotting
import random

K = 50.

# import matplotlip.pylab as p 

## Function gives change in each step
def dR_dt(Pops):
    """ Returns the growth rate of predator and prey populations at any 
    given time step """
    
    R_t = Pops[0]
    C_t = Pops[1]
    E = random.gauss(0, 1)
    R_t1 = r*R_t + E*R_t - E*R_t*R_t/K - r*R_t*R_t/K - a*R_t*C_t 
    C_t1 = -z*C_t + e*a*R_t*C_t
    
    return sc.array([R_t1, C_t1])


def main(argv):
	## Sets iteration number
	N = 100000
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
	
	## Sets initial populations
	x0 = 10
	y0 = 5 
	z0 = sc.array([x0, y0]) # initials conditions: 10 prey and 5 predators per unit area
	
	# Now define time and max time -- integrate from 0 to 15, using N points:
	t_m = 150
	dt = float(t_m)/float(N)
	i = 0
	## Keep old time function so there's something to plot against
	t = sc.linspace(0, t_m,  N+1)
	# preallocate memory for pops
	pops = sc.zeros((N+1, 2))
	pops[0] = z0
	## For loop to succesively integrate the function
	## Just gonna use Euler as it's easiest
	while i < N:
		dRC = dR_dt(pops[i])# Get change from function
		pops[i+1, 0] = pops[i, 0] + dt*dRC[0] # apply it to each pop in term
		pops[i+1, 1] = pops[i, 1] + dt*dRC[1]
		i += 1

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
	f1.savefig('../Results/prey_and_predators_4.pdf') #Save figure
	## Now need to output the population sizes
	if (prey[N-1] - prey[N-2]) ** 2 < 0.0000000000001: 
		print 'Steady Resource population = {}'.format(prey[N-1])
	if (predators[N-1] - predators[N-2]) ** 2 < 0.0000000000001: 
		print 'SteadyConsumer population = {}'.format(predators[N-1])
	
	return 0



if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)
