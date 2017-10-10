"""Author: Jacob Cook.
   tuple.py script that prints a tuple of tuples as indvidual lines for 
   each species through use of list comprehensions
"""

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line for each species
# Hints: use the "print" command! You can use list comprehensions!

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
## Setup definitions for the bird species
def is_a_sparrow(name):
	return name[0].lower().startswith('passerculus ')

def is_a_martin(name):
	return name[0].lower().startswith('delichon ')
	
def is_a_junco(name):
	return name[0].lower().startswith('junco ')
	
def is_a_swallow(name):
	return name[0].lower().startswith('tachycineata ')

## List definitions then used to print data for same species on same line
print [species for species in birds if is_a_martin(species)]
print [species for species in birds if is_a_sparrow(species)]
print [species for species in birds if is_a_junco(species)]
print [species for species in birds if is_a_swallow(species)]
