#Use if, elif, else to check if a number is ODD or EVEN
#To check if a number use modulus (%)

#Start out by asking the user input

print ("Hello, please put in your number")
#Define variable to take user input
number = input()
# use modulus (%), if remainder is not 0 when divided by 2,
# that means it is an odd number
if int(number) % 2 != 0:
	# use int() to clarify ure using a modulus
	print("This is an ODD number")
else:
	print ("This is an EVEN number")