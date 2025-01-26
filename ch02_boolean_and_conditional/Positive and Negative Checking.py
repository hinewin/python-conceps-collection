input = input("What is the number you want to insert? ")

x_positive = input%2 ==0
if x_positive:
	x_positive = int(x_positive)
	if x_positive:
		print ("Even")
else:
	print ("Please insert a number")