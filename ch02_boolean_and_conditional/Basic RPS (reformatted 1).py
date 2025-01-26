
#Original#
# print ("Rock...")
# print ("Paper...")
# print ("Scissors...")


# player1 = input("Player 1, Make your move: ")
# player2 = input("Player 2. Make your move: ")

# if player1 == "rock" and player2 == "scissors":
# 	print ("player1 wins!")
# elif player1 == "rock" and player2 =="paper":
# 	print("player2 wins!")
# elif player1 == "paper" and player2 =="rock":
# 	print ("player1 wins!")
# elif player1 =="paper" and player2 =="scissor":
# 	print ("player2 wins!")
# elif player1 =="scissors" and player2 == "rock":
# 	print ("player2 wins!")
# elif player1 =="scissors" and player2 == "paper":
# 	print ("player1 wins!")
# elif player1 == player2:
# 	print ("It's a tie!")

# else:
# 	print ("something went wrong")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################
##########
###1st SOLUTION


# print ("Rock...")
# print ("Paper...")
# print ("Scissors...")

# player1 = input("Player1, please make your move: ")
# player2 = input("Player2, please make your move: ")

# if player1==player2:
# 	print ("It's a tie")
# elif player1 == "rock":
# 	if player2 == "scissors":
# 		print ("Players1 wins!")
# 	elif player2 == "paper":
# 		print ("Player2 wins!")
# elif player1 == "scissors":
# 	if player2 == "paper":
# 		print("Player1 wins!")
# 	elif player2 == "rock":
# 		print ("Player2 wins!")
# elif player1 == "paper":
# 	if player2 == "rock":
# 		print ("player1 wins!")
# 	elif player2 =="scissors":
# 		print ("player2 wins!")
# else:
# 	print ("something went wrong")



#########Shorter Solution#########
#########Shorter Solution#########
#########Shorter Solution#########
#########Shorter Solution#########


p1 = input("Player 1: rock, paper, or scissors ")
p2 = input("Player 2: rock, paper, or scissors ")

if p1 == p2:
	print ("draw")
elif p1 =="rock" and p2 == "scissors":
	print ("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")

