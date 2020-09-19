#abs return the absolute value
print (abs(-5))
# 5
#fabs (import with math)
#math.fabs(-4) - abs but treats everything as a float
import math
print (math.fabs(-4)) # 4.0 because fabs convert 

#sum- Takes an iterable and an optional START
#Returns the sum of start and the items of an
#iterable from left to right and returns total
# start defaults to 0
print (sum([1,2,3])) # 1+2+3= 6
# start at 10
print (sum([1,2,3],10)) # 10+(1+2+3)= 16

### Round- return number rounded to ndigits precision 
# if ndigits is omitted/ none, returns nearest integer
print (round(10.2)) # 10
print (round(1.215121,2)) #1.22