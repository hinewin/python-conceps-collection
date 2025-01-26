#name classes are SINGULAR and Uppercase
class User:
    pass #nothing else is in there, move on
user1 = User() #just like an empty list, they might look the same
# but they are all stored at different memories
user2 = User()
user3 = User() # they're all different users

print (user1) # __main__.User. It is now in the User class