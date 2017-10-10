# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets

"""Author: Jacob Cook.
   lc2.py script that breaks down a list of rainfall into smaller lists
   based on amount of rain
   does this via both list comprehension and convential loops
"""

rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )
           
# Block of definitions to  identify rain depth
def is_above_100(name):
	return name[1] >= 100.0

def is_below_50(name):
	return name[1] <= 50.0

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
mm100_lc = set([data[0] for data in rainfall if is_above_100(data)])
print mm100_lc

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm.
mm50_lc = set([data[0] for data in rainfall if is_below_50(data)])
print mm50_lc

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !).
# List for rainfall above 100mm
highrain_loops = set()
for data in rainfall:
	if is_above_100(data):#checks if rainfall greater 100mm
		highrain_loops.add(data[0])# adds to list if it does
print highrain_loops# after loops prints lists

# List for rainfall below 50mm
lowrain_loops = set()
for data in rainfall:
	if is_below_50(data):
		lowrain_loops.add(data[0])
print lowrain_loops

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
