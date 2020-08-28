## Print the first initial of each name
name = ["Elie","Tim","Matt"]
name2= [char[0] for char in name]
print (name2)

# Print even numbers in this list
number = [1,2,3,4,5,6]
evens = [num for num in number if num%2 ==0]
print(evens)

#given 2 lists [1,2,3,4] and [3,4,5,6]
#Create a variable "ANSWER" that stores
#The intersection of the 2 (3,4)
list_1 = [1,2,3,4]
list_2 = [3,4,5,6]
answer1 = [x for x in list_1 if x in list_2]
print (answer1)


### Given list of words create a variable that store
## a new list with each word reversed and in lowercase

words = ["Elie","Tim","Matt"]
answer2 = [char[::-1].lower() for char in words]
print (answer2)


## For all numbers between 1 and 100 (including 100)
## create a variable that storate a list
#with all numbers that are divisible by 12

number = range(1,101)
answer= [x for x in number if x%12 == 0]
print (answer)


### Given string "amazing" create a variable
# that stores a list of all letters from the string
# BUT not the vowels (a,e,i,o,u)
string = "amazing"
answer = [var for var in string if var not in"aeiou"]
print (answer)
