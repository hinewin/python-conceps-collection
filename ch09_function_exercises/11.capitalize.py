#function called capitalize
#accepts string and return same string with first letter capitalized

def capitalize(word):
    return word[:1:].upper() + word[1:]




print (capitalize("tim"))