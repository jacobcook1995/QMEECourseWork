"""Author: Samraat Pawar. (section reading in data added by Jacob Cook)
   align_seqs.py script that reads in DNA sequences from a file and then
   finds the length of the longest overlap and then prints said overlap 
   and its length. Can read two sequences written in csv format
"""
# import csv so I can use csv reader
import csv
import doctest

# Need to open csv file to be read from
f = open('../Data/Sequence.csv','r')

# Now use csv.reader
csvread = csv.reader(f)

# Assign the sequences from the readcsv tuple
for row in csvread:
	seq1 = row[0]
	seq2 = row[1] # Obviously this only really reads final row, crude but works for purpose
f.close()
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

# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
	"""Checks that not matching and matching works for short strings
	>>> calculate_score("A", "T", 1, 1, 0)
	-
	T
	A
	0
	<BLANKLINE>
	0
	>>> calculate_score("A", "A", 1, 1, 0)
	*
	A
	A
	1
	<BLANKLINE>
	1
	"""
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

doctest.testmod()
