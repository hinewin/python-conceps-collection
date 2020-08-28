nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for lst in nested_list: ## for each list in nested list
    for i in lst:   ## for each item in this list
        print (i)   #print the item

### Ex. 2
coords = [[10.323,423,9.132],[37.212,-14.092],[21.367,32.572]]
for loc in coords:
    for coord in loc:
        print (coord)

### Nested List Comprehension
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
[[print(num) for num in lst] for lst in nested_list]
## print item for item in list, for lists in the NESTED list


#### Nested list comprehension ex(2)

board = [[num for num in range(1,4)] for i in range(1,7)]
#[for each number in range 1,4 print out the num.]
#[do this loop in 6 times ( for each list in 6 lists)]
print (board)

### Print even or odd in loop of 3
ex5=[["X" if x%2 !=0 else "O" for x in range(1,4)] for x in range(1,3)]
# print "X" if # in range (1,4) is odd
# else print "O"
# do loop in range (1,3), 2x
print (ex5)

#### Lets say you want muliple * in a list
star = [[("*") for i in range (1,4)] for i in range(1,9)]
## print * 3 times (1,2,3)
## each list print list (1,2,3,4,5,6,7,8)
print (star)

#### List Exercises 5
#Use list comprehension to print [0,1,2],[0,1,2],[0,1,2]

answer=[[x for x in range(1,4)] for i in range (1,4)]
print(answer)

### Exercise #6
# Create a 10x10, each row contains numbers (0,9)

num = [[x for x in range(0,10)] for i in range(1,11)]
print (num)