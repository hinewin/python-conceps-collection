#INDEX#
#- Return the index(position) by specifying the item 

list_index = [1,2,3,4,5]
print (list_index.index(3))### Output: 2 (is the index position of #3)
#Can also specify the start and end of where to look
#list_index(#what item, #starting from position)
#list_index(#what item,#starting from, #end from)

#####COUNT#######
#- Count how many time an item occurs

list_count = [1,1,1,2,2,3,4,5]
print(list_count.count(1)) ### output: "1" occurs 3 times


##########REVERSE########
#- REVERSE the items of the list ## Update

list_reverse = [1,2,3,4]
list_reverse.reverse()
print (list_reverse) ##Output: [4,3,2,1]


########SORT###########
#-sort the items of the list

list_sort=[3,5,2,1,4]
list_sort.sort()
print (list_sort)### Output: [1,2,3,4]

############JOIN##############
#- JOIN is a str method
#- Convert a LIST into a STRING
##- Concatenates (combine) 	a **BASE** string between each item in a list
#### base string is provided by you

words = ["Hello","world","!"]
print (" ".join(words))
