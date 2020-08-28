#count_dollar_signs function is broken
# its supposed to return the number of $ characters
## in a given string
#ex: count_dollar_signs ("$super $size") # return 2

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        #return count ## return is within if char == $
    return count
# if added return under for char, the loop will continues
