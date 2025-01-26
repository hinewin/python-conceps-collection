#LOOPING
#We can use a FOR loop to iterate a tuple just like a list
names = ('Colt','Blue','Rusty','Lassie')
for name in names:
    print (name)
#output: Colt, Blue, Rusty, Lassie
## While loop
i = len(names) - 1  # Have the list go from backward (3)
print (i)
while i >= 0: # When it is above 0 (3,2,1,0) run the loop
    print (names[i]) # print out the item in the tuple names
    i -= 1  # i will -1 each time it loops


# Tuples methods
#COUNT- return # of times a value appears in a tuple
x=(1,2,3,3,3,6)
print (x.count(3))
#output: 2

#INDEX- return the index in the tuple
t= (1,2,3,3,3,)
print (t.index(1)) # What is the position of 1 in the tuple t
#output: 0
#if item in tuple repeats, it will return the postion of the 1st item