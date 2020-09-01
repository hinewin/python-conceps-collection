# **kwargs- special operator to pass to functions
# - Gathers remaning keyword arguments as a dictionary

#def fav_colors(colt ="purple",ruby ="red",ethel="teal"}
## instead use
def fav_colors2(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


print (fav_colors2(colt ="purple",ruby ="red",ethel="teal"))

### Looping through key and values
def special_greeting (**greetings):
    if "David" in greetings and greetings["David"] == "Special":
        return "Key in David contains 'Special'"
    elif "David" in greetings and greetings["David"] == "Hello":
        return (f"key is: {greetings['David']} in the dict David")
    else:
        return "not recorded"

print (special_greeting(David = "Hello"))
print (special_greeting(David = "Special"))
print (special_greeting(Tanner = "Hi"))