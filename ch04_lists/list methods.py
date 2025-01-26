### APPEND - to add an item to the end of the list

list_append = [1,2,3,4] ### Append will only add *1* item to the list
list_append.append(5)
print (list_append)
#output: [1,2,3,4,5]

###to add multiple items in the END of the list use ##EXTEND##


list_extend = [1,2,3,4]
list_extend.extend([5,6])
print (list_extend)
#output: [1,2,3,4,5,6]

### Use INSERT to add an item at a GIVEN position

list_insert = [1,2,4,5]

#list3.insert(#position#, #what to insert#)

list_insert.insert(2,3)
print (list_insert)

#output: [1,2,3,4,5]

##############################################################
#CLEAR method- Remove all items from a list
list_clear = [1,2,3,4]
list_clear.clear()
print(list_clear)
#output: []

##### POP#### 
# - Removes item at a certain position, also return
# - If position was not assigned, it will remove the last item

list_pop= [1,2,3,3,4]
## you can use the removed value by assigning to a variable
popped= list_pop.pop(2)
print (list_pop) #output: [1,2,3,4]
print (popped)# output: 3

######REMOVE#######
## Remove the first found *ASSIGNED* value
## Will not return value

list_remove = [1,2,2,2,3,4]
list_remove.remove(2)
print (list_remove)