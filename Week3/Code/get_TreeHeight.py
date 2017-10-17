#!/usr/bin/python

"""get_TreeHeight.py: a script that reads in a csv file and then calculates
   heights and reoutputs with addoitional data
"""
   
__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

# imports
import sys # module to interface our program with the operating system
import scipy
import csv
import math
import os
import numpy as np

#constants can go here


# functions can go here
def Height(degrees, distance):
	radians = degrees * math.pi/180
	height = distance * math.tan(radians)
	return height


def main(argv):
	filename = sys.argv[1]
	filepath = "../Data/" + filename
	f = open(filepath, 'r')
	lines = len(f.readlines()) - 1
	## initialise vector and i
	heights = [0] * (lines+1)
	names = [None] * (lines+1)
	angles = [0] * (lines+1)
	distances = [0] * (lines+1)
	heights[0] = "Height.m"
	names[0] = "Species"
	angles[0] = "Angle.degrees"
	distances[0] = "Distance.m"
	i = 0
	
	with open(filepath, 'r') as csvfile:
		csvfile.readline() # skip header
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in spamreader:
			heights[i+1] = Height(float(row[2]),float(row[1]))
			names[i+1] = row[0]
			angles[i+1] = row[2]
			distances[i+1] = row[1]
			i += 1

	
	Data = (names, distances, angles, heights)
	data = np.asarray(Data).T.tolist() #transpose
	
	## Strip file name
	filenamestrip = filename.replace('.csv', '')
	## create file path name
	outfilepath = "../Results/" + filenamestrip + "_treeheights.csv"
	## output data as a csv
	with open(outfilepath, "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for line in data:
			writer.writerow(line)

	
	return 0

		
if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)
