#sum_floats - accept a variable number of arguments
# return sum of all parameters that are FLOAT
# if no float return 0 

def sum_floats(*nums):
    return sum(n for n in nums if type(n) == float)
print (sum_floats(1.5,5.6,'sdqwe'))