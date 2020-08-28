#Add
# Adds an element to a set
s = set([1,2,4,6])
s.add(4) # set already has 4 in the list
print (s) #output will be 1,2,4,6

#REMOVE
# Removes a value from set
set1 = {1,2,3,4,5,6,7}
set1.remove(3)
print (set1) # It will remove 3, 1,2,4,5,6,7

#If trying to remove a value not in there it will prints error
#to prevent error use method    DISCARD

# # # # # COPY ######
#- Creates a copy of the set
s = set([1,2,3])
another_s = s.copy()
print (another_s) # same value as s, 1,2,3
print (another_s is s) #False

#### CLEAR
#- Removes all the contents of the set
s = ([1,2,3])
s.clear()
print (s) # nothing will be there

### Set Math ###
# sets have math methods ( intersection, symetric_differencem, union)
math_students = {"Matthew","Helen","Prashant","James","Aparna"}
biology_students = {"Jane","Matthew","Charlotte","Mesut","Oliver","James"}
#UNION- allow you to join 2 lists together and avoid duplication items
#Union uses pipe (|)
print (math_students | biology_students)
# Intersection - select items that both set have in common
print (math_students & biology_students)
# James and #Matthew- 2 items in both sets