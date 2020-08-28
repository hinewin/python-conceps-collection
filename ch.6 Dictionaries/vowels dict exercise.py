#Create a dict with key as a vowel in the alphabet
#Values as 0
answer = {char:0 for char in 'aeiou'}
#or
answer2 = dict.fromkeys("aeiou",0)

#ASCII Codes Dictionary Exercises
#chr() returns a string if you provide a corresponding ASCII code
#ex: chr(65) = 'A'. chr(66) 'B' all the way to (99) = Z
#Create a dict that maps ASCII keys to their letter

answer = {key:chr(key) for key in range (65,91)}
# dictionary {key:value}
#key, chr(key)= value for key between 65-91
print (answer)

