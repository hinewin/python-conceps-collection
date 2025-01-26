#Function is_all_strings that accepts a single iterable
# return TRUE if it contains ONLY strings.
#Else return false

def is_all_strings(lst):
    return all(type(char)== str for char in lst)
# Check for type of char in list "lst" if char is a str
print (is_all_strings(['a',1,'b']))

#FALSE