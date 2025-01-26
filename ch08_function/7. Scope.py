# When variables are created in functions
# They are SCOPED in that function
### Meaning it will only be available INSIDE that function

#ex:
def say_hello():
    instructor = "Colt" ## Instructor is WITHIN the function
    return (f"Hello{instructor}")
print (say_hello()) # return Hello Colt

# When trying to print a variable that is SCOPED
#it will not be able to print instructor
#print (instructor) #output: insturctor is not defined

# A way to access a scope variable is to return the result of that variable



######## GLOBAL SCOPE #########

#- A variable OUTSIDE of functions
#- Cannot change a global variable/scope
#ex:
total =0
def increment():
    #total +=1 # add the global variable by 1
    return total # get the value of it being added
print (increment()) # ERROR
# Python will assume there is a LOCAL variable within the function
# ** to reference a global variacle use "global"
total = 0
def increment_global():
    global total # now you can manipulate the variable total
    #outside of the function
    total +=1
    return total
print (increment_global()) 
print (total)


### Nonlocal
## Lets us modify a parent's variable in a child (nested) function
def out():
    count = 0
    def inner():
        nonlocal count ## indicates its not a global variable, nor
        #within the inner function. It is within the parent or
        # some other function that it is nested in
        count +=1
        return count
    return inner()