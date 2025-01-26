## Accessing Dictionary: keys,values,items()

# Accessing All Values in a Dictionary
# Use .values()

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

for value in instructor.values(): # Using the.values() function
    #for each value in dict instrudtor, print them
    print(value)
    #output: Colt, True, 4, Python, False, fav number

#Same way for KEYS -- use .keys()

for keys in instructor.keys():
    print (keys)
#output: "name,","owns_dog"

### Accessing both keys and values using .items()
# first is key, 2nd is value
for keys,values in instructor.items():
    print(f"keys: {keys} - values: {values}")

