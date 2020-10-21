#Lets add some attributes in the class of User
#Use __init__ method to create an instance of the class (instantiate)

class User:
    def __init__(self, first, last, age):
#initialize the DATA the user will have
# self will always be the first parameter
# self refers to the instance were working on
        self.first = first # first name attribute of user
        self.last = last # last name attribute of user
        self.age = age # age attribute of user

user1 = User("Joe","Bui",27) # Joe will be assigned to the first parameter
user2 = User("Blanca","Parez",42) #After first user is created, self will refers to this

print (user1.first, user1.last) #the attribute of user1
#BOTH have the same pattern, just holds different information
print (user2.first, user2.last) #the attribute of user1


#To instantiating a class,
#v = Vehicle (name of class) (Pass in data/arguments)
#v = Vehicle ("Honda","Civic",2017)
#now V will be come the INSTANCE of the Vehicle Class

#Self must always be the first parameter to __init__ and any
#methods and properties on class instances