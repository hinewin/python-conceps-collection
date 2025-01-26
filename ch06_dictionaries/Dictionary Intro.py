# A Dictionary is a 
# Data structure that consists of key value pairs
# pair of information
# Keys= describe data, values = represent data

## kEYS and VALUES are seperated by a colon (:)
student ={
    "name": "Hai",
    "owns_dog": False,
    "fav_lang": "Python",
    9: "Favorite Number",
}
print (student)

### ANOTHER APPROACH- DICT function
# Pass keys and values separted by =
cat2 = dict(name="kitty",age = 0.5)
print (cat2)

## How to access individual values
# pass the key in []
# if key does not exist, there will be error
print(student["name"])

###Acess Data Exercise
#given list, print out first and last name with space between
artist = dict(first = "Neil", last = "Young")
full_name = artist["first"] + " " + artist["last"]
print (full_name)

#Solution #2 using f-string
full_name2 = f"{artist['first']} {artist['last']}"
print (full_name2)
