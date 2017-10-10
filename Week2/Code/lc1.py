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
## Block of definitions to identify bird type
def is_a_sparrow(name):
	return name[0].lower().startswith('passerculus ')

def is_a_martin(name):
	return name[0].lower().startswith('delichon ')
	
def is_a_junco(name):
	return name[0].lower().startswith('junco ')
	
def is_a_swallow(name):
	return name[0].lower().startswith('tachycineata ')
	
## This block makes the 3 martins lists via comprehensions
martins_lc1 = set([species[0] for species in birds if is_a_martin(species)])
print martins_lc1 # after list comphension then outputs
martins_lc2 = set([species[1] for species in birds if is_a_martin(species)])
print martins_lc2
martins_lc3 = set([species[2] for species in birds if is_a_martin(species)])
print martins_lc3

## This block makes the 3 sparrows lists via comprehensions
sparrows_lc1 = set([species[0] for species in birds if is_a_sparrow(species)])
print sparrows_lc1
sparrows_lc2 = set([species[1] for species in birds if is_a_sparrow(species)])
print sparrows_lc2
sparrows_lc3 = set([species[2] for species in birds if is_a_sparrow(species)])
print sparrows_lc3

## This block makes the 3 juncos lists via comprehensions
juncos_lc1 = set([species[0] for species in birds if is_a_junco(species)])
print juncos_lc1
juncos_lc2 = set([species[1] for species in birds if is_a_junco(species)])
print juncos_lc2
juncos_lc3 = set([species[2] for species in birds if is_a_junco(species)])
print juncos_lc3

## This block makes the 3 swallows lists via comprehensions
swallows_lc1 = set([species[0] for species in birds if is_a_swallow(species)])
print swallows_lc1
swallows_lc2 = set([species[1] for species in birds if is_a_swallow(species)])
print swallows_lc2
swallows_lc3 = set([species[2] for species in birds if is_a_swallow(species)])
print swallows_lc3

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !).
## 3 lists for martins are now made using for loops
martins_loops1 = set()# creates empty sets
martins_loops2 = set()
martins_loops3 = set()
for species in birds:
	if is_a_martin(species):#checks if name matches
		martins_loops1.add(species[0])# adds to lists if it does
		martins_loops2.add(species[1])
		martins_loops3.add(species[2])
print martins_loops1# after loops prints lists
print martins_loops2
print martins_loops3

## 3 lists for sparrows
sparrows_loops1 = set()
sparrows_loops2 = set()
sparrows_loops3 = set()
for species in birds:
	if is_a_sparrow(species):
		sparrows_loops1.add(species[0])
		sparrows_loops2.add(species[1])
		sparrows_loops3.add(species[2])
print sparrows_loops1
print sparrows_loops2
print sparrows_loops3

## 3 lists for juncos
juncos_loops1 = set()
juncos_loops2 = set()
juncos_loops3 = set()
for species in birds:
	if is_a_junco(species):
		juncos_loops1.add(species[0])
		juncos_loops2.add(species[1])
		juncos_loops3.add(species[2])
print juncos_loops1
print juncos_loops2
print juncos_loops3

## 3 lists for swallows
swallows_loops1 = set()
swallows_loops2 = set()
swallows_loops3 = set()
for species in birds:
	if is_a_swallow(species):
		swallows_loops1.add(species[0])
		swallows_loops2.add(species[1])
		swallows_loops3.add(species[2])
print swallows_loops1
print swallows_loops2
print swallows_loops3

# ANNOTATE WHAT EVERY BLOCK OR, IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
