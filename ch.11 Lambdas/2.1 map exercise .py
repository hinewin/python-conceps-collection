#function decrement_list accepts single list of numbers as a parameter.
#Return a copy of list with each item decremented by 1

def decrement_list(lst): #function has parameter that takes a list
    return list(map(lambda x:x-1,lst))
# return list to pass MAP
# for x, x-1 in list
print (decrement_list([1,2,3,4,5,6]))