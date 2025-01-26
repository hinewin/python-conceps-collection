# is_palindrome - word/phrase reads the same backward or foward
# takes 1 parameter and return True or False depending
# if string is a palindrome
# Allow function to ignore whitespace & capitalize

def is_palindrome(word):
    stripped = word.lower().replace(" ","")
    return stripped == stripped[::-1]

print (is_palindrome("amanaplanacanalpanama"))