#This is interpolation
#Changing an int or float value to fit in a string

books = 8
say= (f"I have {books+3} books")
#inserting f in front of the string to interpolate, use {} to insert variable
print(say)


#Python 3.5 and below uses .format
#print("I had {} books".format)

###Converting Numbers###

#use the name of the builtin type to convert the data type

decimal = 3.14
interger = int(decimal) #prints out 3
print (f"I will convert:{decimal} from decimal to:{interger} integer")
