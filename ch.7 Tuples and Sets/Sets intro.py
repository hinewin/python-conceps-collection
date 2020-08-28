# SETS
# formal mathematical sets
#- Do not have duplicate values and have no orders
#- Cannot access items by index (because everything is random)
#- Useful when need to keep track of collection of element
#without caring ordering,keys or values or duplicates

#Create/Access Sets
s= set({1,4,4,4,4,6}) #output: (1,4,6)
# function
s2 = set({1,2,3})
#or
s3= {1,2,3}
# Since we cannot find index use "in" to check
print (4 in s3)
print (3 in s3)

# ACCESS all values in a set using FOR LOOP

numbers = {1,2,3,"a"}
for num in numbers:
    print (num)

## Common use cases
cities = ["Los Angeles", "Boulder","Kyoyo","San Francisco","San Francisco", "Boulder","Florence","Santiago","Los Angels","Shanghai"]
print (len(cities)) # There are 10 cities but some are duplicate
print (len(set(cities))) #using set on the list will only print non duplicate
#output:8


