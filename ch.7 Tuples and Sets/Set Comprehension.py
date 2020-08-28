#Set Comprehension
sc1= {x**2 for x in range (10)} # Since it is not a dict, it will not need key,value
#output will be random
print (sc1)

# Example using string
sc2 = {char.upper() for char in "hello"}
# capitalized the character in HELLO in each letter 
print (sc2)

# EX3
string1 = "sequoia"
len({char for char in string1 if char in "aeiou"}) == 5
# for each character in a given string
#if the character has a vowel "aeiou" 5 times
# checking if the length is = 5
