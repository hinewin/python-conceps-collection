
# while True: ### Infinite loop while TRUE
# 	pw = input("What is the password ") ## ask for password
# 	### if pw wrong, keep going, if = cow break the loop
# 	if pw == "cow":
# 		break
# 	else:
# 		print("Please try again ")

times = int(input("How many times do I have to tell you? "))

for times in range (times):
	print ("Clean up your room")
	if times >= 4:
		print ("do you even listen anymore")
		break