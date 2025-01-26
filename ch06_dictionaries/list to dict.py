#given person variable:
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#Create a dict called answer that make first item in the list
#a KEY and 2nd item a VALUE.
answer = {k:v for k,v in person}
# {set key:value as k,v from items in person
print (answer)

#Easy way to convert a list to dict is
dict(person)
print (person)
