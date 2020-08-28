import random
random_number = random.randint(1,10) # generate numbers 1-10

#handle user guesses
#	if they guess correctly tell them they won
# otherwise tell them they are too high or too low

#BONUS - let player play again if they want
random_number= int(random_number)
u_guess= input ("what is your number? ")
u_guess = int(u_guess)
while True:
	if u_guess == random_number:
		print (f"congratualations! the magic number was {random_number}")
		cont = (input("y to continue n to stop: "))
		if cont == "y":
			random_number = random.randint(1,10)
			u_guess = int(input("Please insert your new number: "))
		if cont == "n":
			print ("Thank you for playing!")
			break

	elif u_guess <= random_number:
		print ("That's too low")
		u_guess = int(input("Please try again: "))
	else:
		print ("That's too high")
		u_guess = int(input("Please try again: "))
	