import csv
import sys
import pdb
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus '
        >>> is_an_oak('quercus ')
        True
        
        Returns True if name is started with 'Quercus '
        >>> is_an_oak('Quercus ')
        True
        
        Returns False if name is started with 'Quercuss '
        >>> is_an_oak('Quercuss ')
        False
        
        Returns False if name is started with 'Fagus '
        >>> is_an_oak('Fagus ')
        False
        
    """
    return name.lower().startswith('quercus ')
    
print(is_an_oak.__doc__)

# Starts the dubugging session here
def main(argv):
    f = open('../Data/TestOaksData.csv','rb')
    g = open('../Data/JustOaksData.csv','wb')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        print row
        print "The genus is", row[0]
        if is_an_oak(row[0]):
            print row[0]
            print 'FOUND AN OAK!'
            print " "
            csvwrite.writerow([row[0], row[1]])    
    
    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()
