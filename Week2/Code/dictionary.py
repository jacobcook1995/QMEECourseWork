"""Author: Jacob Cook.
   dictionary.py script creates a dictionary from hard coded data using
   list comprehensions
"""

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here:
## First definitions to determine order
def is_Carnivora(name):
	return name[1].lower() == 'carnivora'
	
def is_Afrosoricida(name):
	return name[1].lower() == 'afrosoricida'
	
def is_Rodentia(name):
	return name[1].lower() == 'rodentia'
	
def is_Chiroptera(name):
	return name[1].lower() == 'chiroptera'
	
## Then make the sets for each order name
Carnivora_lc = set([species[0] for species in taxa if is_Carnivora(species)])
Afrosoricida_lc = set([species[0] for species in taxa if is_Afrosoricida(species)])
Rodentia_lc = set([species[0] for species in taxa if is_Rodentia(species)])
Chiroptera_lc = set([species[0] for species in taxa if is_Chiroptera(species)])

## Then add all things to the dictionary
Taxa = {'Afrosoricida': Afrosoricida_lc, 'Carnivora': Carnivora_lc, 
'Chiroptera': Chiroptera_lc, 'Rodentia': Rodentia_lc}

## Then print dictionary
print Taxa
