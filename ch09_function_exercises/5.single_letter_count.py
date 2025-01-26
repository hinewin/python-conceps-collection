# single_letter_count function takes two parameters(2 strings)
#1st parameter = word, second parameter = letter
#returns the number of times that letter appears in the word
#Case Insensitive
# if letter not in word, return 0

def single_letter_count(words,char):
    if char.lower() in words.lower():
        return words.lower().count(char.lower())
    return 0
print (single_letter_count("Hello World","h"))
print (single_letter_count("Hello World","z"))
print (single_letter_count("Hello World","l"))

def single2_letter_count(words,char):
    word= words.lower()
    char= char.lower()
    if char in word:
        return word.count(char)
    return 0

    
print (single2_letter_count("Hello World","h"))
print (single2_letter_count("Hello World","z"))
print (single2_letter_count("Hello World","l"))