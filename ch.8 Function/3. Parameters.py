# Parameters
def square(num): ### Add in a parameter within ()
    return num**2 #use that parameter

print (square (32))
print (square(8))

def sing_happy_birthday(name):
    print ("Happy Birthday to You")
    print ("Happy Birthday to You")
    print (f"Happy Birthday dear {name}")
    print ("Happy Birthday to You")

print(sing_happy_birthday("Hai"))

### ANOTHER FUNCTION 

def add(a,b): 
    return a+b

print (add(2,1)) ### 2+1 = 3

### Variables that are passed to a function
# Theyre placeholders that get assigned
# When you call the function

def multiply (first,second): # these are just placeholders
    return first*second

print (multiply(1,0)) ### 1*0 = 0


#########  NAMING PARAMETERS  ###########
# specify your parameters so we can understand
def print_full_name (first_name, last_name):
    return (f" your first name is: {first_name} and lastname is: {last_name}")

print (print_full_name("Hai","Nguyen"))


### Parameters vs Arguments

# Parameter is a variable in a METHOD DEFINITION

# When a method is called, ARGUMENTS are the data you pass
#into the method's parameters

#Parameter is a variable (first_name) in the Declaration of a function

#Argumment is the ACTUAL value (Hai) that get passed