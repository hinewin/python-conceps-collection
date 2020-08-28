
import random ## Import random module

#If only using randint from random
#You can say
#From random import randidnt
#Then you will not need to reference random.randidnt

rand_num = random.randint(0,2) # Use function in module to generate 3 ranndon #s
#you can say rand_num = randint(0,2)
p1 = input("Player1, please make your move: ").lower()## all inputs will be the same using lower()

if rand_num == 0:
	ai = "rock"
elif rand_num == 1:
	ai = "paper"
else:
	ai = "scissors"
print (f"computer plays {ai}")

if p1 == ai:
	print ("draw")
elif p1 =="rock" and ai == "scissors":
	print ("p1 wins")
elif p1 == "paper" and ai == "rock":
    print("p1 wins")
elif p1 == "scissors" and ai == "paper":
    print("p1 wins")
else:
    print("Please enter a valid move")

