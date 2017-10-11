#!/usr/bin/python

"""Author: Samraat Pawar. (section reading in data added by Jacob Cook)
   align_seqs.py script that reads in DNA sequences from a file and then
   finds the length of the longest overlap and then prints said overlap 
   and its length. Can read two sequences written in seperate fasta files
   if no fasta files are specified it automatically uses two specified in
   Data
"""

__author__ = 'Jacob Cook (jc2017@imperial.ac.uk)'
__version__ = '0.01'

import sys # module to interface our program with the operating system

# functions can go here
# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
	# startpoint is the point at which we want to start
	matched = "" # contains string for alignement
	score = 0
	for i in range(l2):
		if (i + startpoint) < l1:
			# if its matching the character
			if s1[i + startpoint] == s2[i]:
				matched = matched + "*"
				score = score + 1
			else:
				matched = matched + "-"

	# build some formatted output
	print "." * startpoint + matched           
	print "." * startpoint + s2
	print s1
	print score 
	print ""

	return score

def main(argv):
	# First need to determine if default fasta files should be opened or if
	# the user has provided their own
	if len(sys.argv) > 1:
		file1 = sys.argv[1]
	else:
		file1 = "../Data/407228326.fasta"

	if len(sys.argv) > 2:
		file2 = sys.argv[2]
	else:
		file2 = "../Data/407228412.fasta"
		
	# Now that file names have been obtained should open the fasta files
	f = open(file1, 'r')
	g = open(file2, 'r')
	#reads lines skipping the first line
	lines1 = f.readlines()[1:]
	lines2 = g.readlines()[1:]
	# Now need to remove newlines
	seq1 = ''.join([line.strip() for line in lines1])
	seq2 = ''.join([line.strip() for line in lines2])
	f.close()
	g.close()
	
	# assign the longest sequence s1, and the shortest to s2
	# l1 is the length of the longest, l2 that of the shortest
	
	l1 = len(seq1)
	l2 = len(seq2)
	if l1 >= l2:
		s1 = seq1
		s2 = seq2
	else:
		s1 = seq2
		s2 = seq1
		l1, l2 = l2, l1 # swap the two lengths

	
	calculate_score(s1, s2, l1, l2, 0)
	calculate_score(s1, s2, l1, l2, 1)
	calculate_score(s1, s2, l1, l2, 5)

	# now try to find the best match (highest score)
	my_best_align = None
	my_best_score = -1

	for i in range(l1):
		z = calculate_score(s1, s2, l1, l2, i)
		if z > my_best_score:
			my_best_align = "." * i + s2
			my_best_score = z

	print my_best_align
	print s1
	print "Best score:", my_best_score
	
	
	return 0
		
if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
		status = main(sys.argv)
		sys.exit(status)
