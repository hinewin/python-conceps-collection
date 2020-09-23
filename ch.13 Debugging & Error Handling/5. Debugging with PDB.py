# pdb is a python module "python debugger"

#import pdb
# Put pdb.set_trace() wherever, but suggest to put right before
#a couple lines that cause the code to break
# allow us to see a preview to see what happened before, then 
#step trhough and after it
#import pdb

#FIRST EXAMPLE:
first = "First"
second = "Second"
#pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# go through each line to check the value for each variable
#Common PDB commands:
# l (list)
#n (next line)
#p(print)
# c (continue - finishes debugging)

def add_numbers (a,b,c,d):
	import pdb; pdb.set_trace()
	return a+b+c+d
add_numbers(1,2,3,4)
# for this case if we were to press c to check the value of c
# or a to check value of a
# it would use pdb function, so use p(print) the variable
# p a      #(1)


# Also function must be CALLED/ EXECUTED for pdb to run



