## Using the Not logical operator

# Say you have 3 options for a movie theatre
# Kids (age 2-8) get $5 movie ticket
# Senior Citizens (65+) gets $5 movie ticket
# The rest will be $10

print ("Hello, how old are you?")

age = (input())

if not ((int(age) >= 2 and int(age) <=8) or int(age) >= 65):
	print ("You will pay $5")
else:
	print ("You will pay $10")