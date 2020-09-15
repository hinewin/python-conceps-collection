# MAP = a function that accepts 2 arguments, 1 function, and 1 "iterable"
# iterable = something that can be iterated (lists, strings,dicts,sets,tuples)
# Map will runs lambda for each value in the iterable
# and returns a map object that can be converted into another data structure

#Map can be used on functions as well, must define function
# def double(x): return x*2
# doubles =map(double,num)
#list (doubles)


#MAP on LAMBDA

nums = [2,4,6,8,10]

doubles = map(lambda x :x*2,nums)
print (doubles)
#map object at 0x102583f98
# Map can only be iterated once
# to see map use list or for loop
doubles_clean = list(map(lambda x:x*2,nums))
print (doubles_clean)

#2nd Example
people = ["Darcy","Christina","Dana","Annabel"]
peeps = map (lambda name:name.upper(),people)
print (list(peeps))

#3rd Example

names = [{'first':'Rusty','last':'Steele'},
{'first':'Colt', 'last': 'Steele',},
{'first':'Blue', 'last': 'Steele',}]

first_name = list (map(lambda x:x['first'],names))
# list to show map
#map (lambda) for x, shows key 'first' in list names
# RUSTY, COLT, BLUE
print (first_name)

