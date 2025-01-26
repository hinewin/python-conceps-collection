#Going to create a US to vietnamese Dong converter

#First you would want to ask the user for a user input
print ("How much would you like to convert your Dollar in Dong today?")

#Create a variable to hold the user input.
#Request for user input using function input()
user_input = input()
#Now the vairable user_input holds whatever the user inserts

#Use math to convert from dollar to dong 
dong = float(user_input)* 23174.50
#use Float so the number (in decimals) are more accurate

print (f"That will be {round(dong,1)} in dong")
#round to round the variable of dong into 1 decimals place
#You can also create another variable to round it to make the code cleaner
#rounded=round(dong,1)
