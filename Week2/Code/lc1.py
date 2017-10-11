"""Author: Jacob Cook.
   lc1.py script that breaks down a list of birds into smaller sub-lists
   does this via both list comprehension and convential loops
"""

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively.
## Block of definitions to check data is valid
def is_a_name(name):
	return isinstance(name[0], str)

def is_a_name2(name):
	return isinstance(name[1], str)
	
def is_a_mass(name):
	return isinstance(name[2], (float,int))

	
## This block makes the list of latin names via comprehensions
lnames_lc = set([species[0] for species in birds if is_a_name(species)])
print lnames_lc # after list comphension then outputs

## This block makes the list of proper names via comprehensions
pnames_lc = set([species[1] for species in birds if is_a_name2(species)])
print pnames_lc # after list comphension then outputs

## This block makes the list of weights via comprehensions
weights_lc = set([species[2] for species in birds if is_a_mass(species)])
print weights_lc # after list comphension then outputs



# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !).
## list for latin names are now made using for loops
lname_loops = set()# creates empty set
for species in birds:
	if is_a_name(species):#checks if name is valid
		lname_loops.add(species[0])# adds to lists if it does
print lname_loops# after loops prints list

## list for proper names are now made using for loops
pname_loops = set()# creates empty set
for species in birds:
	if is_a_name(species):#checks if name is valid
		pname_loops.add(species[1])# adds to lists if it does
print pname_loops# after loops prints list

## list for weightss are now made using for loops
weight_loops = set()# creates empty set
for species in birds:
	if is_a_name(species):#checks if name is valid
		weight_loops.add(species[2])# adds to lists if it does
print weight_loops# after loops prints list



# ANNOTATE WHAT EVERY BLOCK OR, IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
