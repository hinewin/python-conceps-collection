#Write a function called **multiple_letter_count
#Takes in one paramter (a string) and return
# a dictionary with the keys being the letters
#and the values being the COUNT of the letter

def multiple_letter_count(words):
    return {word:words.count(word) for word in words}

print (multiple_letter_count("awesome"))