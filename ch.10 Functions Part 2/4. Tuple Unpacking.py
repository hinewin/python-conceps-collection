# Using * as an Argument:
# Argument Unpacking: use * as an argument to a function to unpack values

def sum_all_values(*args):
    print (args)
    total = 0       
    for num in args:
        total += num
    print (total)

nums = (1,2,3,4,5,7)
#Right now num will just be a 1 single parameter tuple
# [1,2,3,4,5,7,] is just one parameter
# using *, we will be able to go through each num of nums
sum_all_values(*nums) #now it will go through each value
# (1,2,3,4,5,6)

# Taking a collection and unpack them as individual
#element this is Unpacking