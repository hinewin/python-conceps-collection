def exponent (num, power):
    return num ** power

print (exponent(2,3)) ### 2**3 = 8
print (exponent(3,2)) ## 3*2 = 9

### to DEFAULT a parameter

def exponent_default (num,power=2):#default to 2 if not specified)
    ## you can default both , num =2, power =2
    return num ** power

print (exponent_default(2)) #2**2


### Default Parameters Example

def show_information(first_name ="Hai", is_student = False):
    if first_name =="Hai" and is_student:
        return (f"Welcome back student {first_name}")
    elif first_name =="Hai":
        return (f"Hey {first_name}, you are not a student")
    return (f"hello {first_name}")

print (show_information()) # output: Hey Hai, you are not a student
print (show_information(is_student = True)) # Welcome back student Hai
print (show_information(first_name ="Kathy")) # Hello Kathy

# Parameters allows more defensive
# Avoids errors with incorrect paramters

#Default parameters can be ANYTHING (list,boolean,dictionaries,FUNCTIONS)
def add (a,b):
    return (a+b)
def subtract (a,b):
    return (a-b)
def math (a,b, fn=add): # if fn is not listed, it will default to add function
    return fn(a,b)

print(math(2,2,subtract)) #output 2-2 = 0
print(math(2,2)) # output: FN is default to add 2+2=4

###########****** Make sure that default parameter goes to the end
## OR every paramter has a default