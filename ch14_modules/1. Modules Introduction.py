# Why use Modules?
# keep Python files small
# Reuse code across multiple files by importing 

# Built-in Modules
# - comes with Python, need to import to use

#import random
#import random as r             * alias
#from random import *          * all functions
#from randim import choice, shuffle        *selected functions
#from random import choice as c, randidnt as rannum       * alias for functions

import random # import the modules to use
print (random.choice (["apple","banana","cherry","durian"])) 
#.choice will pick an item from a list
print (random.randint(1,100))
# randint will choose a random number

# Use an alias if the module is LONG
import random as rd
print (rd.choice (["apple","banana","cherry","durian"])) 

#Importing parts of a module
 #* use the from keyword lets you import parts of a module
 # import only what you need~!!!
# from "MODULE" import * pattern
from random import choice, randint,shuffle
# when use FROM, can no longer the name of the MODULE
# use the name of the CHOICE
mylist = (["apple","banana","cherry","durian"])
shuffle(mylist) # call using shuffle instead of random.shuffle
print (mylist)