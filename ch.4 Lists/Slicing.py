## Slicing
## Make new lists using slices of OLD list

### list[start:end:step]

first_list=[1,2,3,4]

#START
print (first_list[1:])	#output would be [2,3,4] exclusive 
#Slice from the end (negative#) it will be inclusive
second_list = [1,2,3,4]
print (second_list[-3:]) ##output would be [3,4]


##END

end_list =[0,1,2,3,4]
print (end_list[:2]) ## It is EXCLUSIVE, includes item before the stop
## Output: [0,1]
print (end_list[:-2]) # using negative will EXCLUSE how many # from that position
#output : [0,1,2]


### STEP
##- Number to count at a time (same as range)

step_list = [1,2,3,4,5,6]
print (step_list[1::2]) # start at 1, end at the end, in interval of 2
#output: [2,4,6]

#WITH NEGATIVE NUMBERS, REVERSE ORDER
print (step_list[1::-1]) # start at 1, start going back from 1
#output: [2,1]
print(step_list[:1:-1]) # Start from 0, end by 1, go reverse from 1
#output: [6,5,4,3]
print(step_list[2::-1]) # Start from 2, end from 0, go reverse from then
#output: [3,2,1]

#Reverse a string
string = "reverse this string"
print(string[::-1]) # start from 0, end from 0, go reverse
string_list = ["orange","blue","purple"]
print (string_list[1][::-1]) #select the string, and go reverse
#reverse of blue
#Modify a list
number = [1,2,3,4,5]
number[1:3] = ['a','b','c'] ## I want to insert abc from index 1-3 (excluding 3)

#output: [1,a,b,c,4,5]

## SWAPPING VALUES####
names = ["Hai","Nguyen"]
names[0],names[1] = names[1],names[0] ### swap values
print(names)
# output: ["Nguyen", "Hai"]

