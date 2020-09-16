#ALL- return TRUE if all ELEMENTS of iterable are truthy or iterable is empty
#ex1
ex1= all([0,1,2,3])
# since 0 is false output is #FALSE
print (ex1)

ex2= all([char for char in "eio" if char in "aeiou"])
print (ex2) # all char in eio is in "aeiou"

ex3= all(num for num in [4,2,10,6,8] if num%2 ==0)
#if num in list is even, hence it is true
print (ex3)

#ANY- return TRUE if ANY element of iterable is Truthy. If iterable empty, returns FALSE

ex4= any([num for num in [2,3,4,6,8] if num %2==0])
print (ex4)
# Tru because most are evens