# Ask for age

# age = (input("How old are you: "))

# if age:
# 	age = int(age)
# # 18-21 wristband
# 	if (age) >= 18 and (age) < 21:
# 		print ("You can enter, but need a wristband!")
# #21+ drink, normal entry

# 	elif (age) >= 21:
# 		print ("You are good to enter and can drink")
# # too young, sorry

# 	else:
# 		print ("you are too young!")
# else:
# 	print ("PLease enter an age!")


age = input("How old are you?: ")
if age: # To avoid user from entering empty string. This means age must be true (!= 0 or none)
	age = int(age)
	if age >= 21: # for 21+ you can enter
		print ("You can enter and can drink")
	elif age >=18: #Between the age of 18 to 21, can enter but w wristband
		print ("you can enter, but you need a wristband")
	else: #The rest (younger than 18, is too young)
		print ("You are too young!")

else: #If there is no value (if age is FALSE)
	print ("Please enter an age")
