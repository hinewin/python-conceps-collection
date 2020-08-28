### All conditional checks resolve to TRUE or FALSE

### False are ##EMPTY STRINGS## and Zero (0)

#EX:
# print ("What is your favorite animal?")

# animal = input()

# print (f"wow {animal} is my favorite too!")

## Now if enter nothing, it will still return  is my favorite too!

#By using a conditional, if the string is empthy you can return something else

print ("what is your favorite animal?")
animal = input()
if animal:
	### Check off for empthy string
	print (f"wow {animal} is my favorite too!")
else:
	### if empty it will return this
	print ("Please insert your favorite animal")