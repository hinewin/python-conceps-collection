# Python strongly encouraged to use try/except blocks
# use to catch exceptions when we can do something about them

try:
    foobar
except:# this would run in every error
    print ("PROBLEM!") # we dont to watch catch every error
    # we wont be able to correctly idefinty what went wrong

# We want to except SPECIFIC ERROR
try:
    colt
except NameError:
    print ("You tried to use a variable that was never declared!")
    #if theres any other error this wouldnt run



d ={"name": "Ricky"}
# d['city'] # would return a key error

# get (d, 'city') return the value from key 'city' in dict d

 # write a function call "get" that get the value from a key in a dict
def get (d,key): 
    try: #use try to run that code 
        d[key]
    except KeyError: #specify the error we might run into
        return "Key not in dict" # return text if key isnt in dict

print (get(d,'city'))