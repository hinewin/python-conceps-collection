#Write a function called speak that accepts a single parameter, animal
def speak(animal="dog"):
    if animal == "pig":
        return("oink")
    if animal == "duck":
        return ("quack")
    if animal == "cat":
        return ("meow")
    if animal == ("dog"):
        return ("woof")
    else:
        return ("?")

print (speak(222))

####### Shorter Solution

#Use dictionary that maps animal names to noises###

def speak_better(animal= "dog"):
    noises ={"dog": "woof","pig": "oink", "duck": "quack", "cat": "meow"}
    # Create a dict of noises
    noise = noises.get(animal) # use.get() method to get value of key
    if noise: # if noise is true
        return noise #return value of when noises.get("key")
    return "?"

print(speak_better("duck"))