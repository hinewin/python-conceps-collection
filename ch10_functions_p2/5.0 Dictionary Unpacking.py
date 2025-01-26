# use ** as an argument for dictionary unpacking
def display_names (first,second):
    print (f"{first} says hello to {second}")
names = {"first": "Colt","second":"Rusty"}

display_names(first = "Charlie",second = "Sue") # not using dict

#if we want to use the names dict in this function nicely
# we will need to use **
display_names(**names)
# It will unpack the names dict into seperate keyword arguments

def add_and_multiply_numbers(a,b,c, **kwargs):
    print (a+b*c)
    print ("Other Stuff...")
    print (kwargs)
data = dict (a=1,b=2,c=3,d=55,name ="Tony")
add_and_multiply_numbers(**data) 
# it will use the dict data and unpack it