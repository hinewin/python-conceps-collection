# [variable name, FOR, 2nd variable, IN, LIST/RANGE]

nums = [1,2,3]

print ([x*10 for x in nums])
# [10,20,30]
##### List COmprehension Example

# numbers = [1,2,3,4,5]
# doubled_numbers = [ i*2 for i in numbers]#### multiply 2 in list
# ### [2,4,6,8,10]
# print (doubled_numbers)

# # String

# name = "Hai"
# cap = [char.upper() for char in name] ## uppercase each letter
# ### [H,A,I]
# print (cap)

friends = ['ashley','matt','michael']
cap2 = [char[0].upper()+ char[1:] for char in friends]
# first letter of each item capitalized + the rest char of item starting
#from index 1
#output is Ashley, Matt, Michael
print (cap2)

## Convert num to str

numbers = [1,2,3,4]
string = [str(num) for num in numbers]
print (string)