# No default parameters allowed
#Function combine_words accepts a single string called word
# and any number of additional key word arguments
# if prefix is provided, return prefix followed by the word
#if suffix provided, return word followed by suffix
#else return word

def combine_words(word,**words):
    if "prefix" in words:
        return (f"{words['prefix']}{word}")
    elif "suffix" in words:
        return (f"{word}{words['suffix']}")
    else:
        return word

print (combine_words("child"))
print (combine_words("child",prefix ="man"))
print (combine_words("child",suffix='ish'))
print (combine_words("work",suffix ='er'))
print (combine_words("work",prefix= "home"))