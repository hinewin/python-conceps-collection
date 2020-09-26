#function contains_keyword
# accepts any # of string arguments
# Return True if arguments are Python keywords ("def","return","if",etc)
# * else return False

#use python module "keyword", method iskeyword.

from keyword import iskeyword as kw

def contains_keyword (*arg): # args to use as many arguments
    for x in arg: # for each item in arg
        if kw(x): #if keyword is in arg
            return True # loop will find if theres any keyword in arg
    else: # if x not in keyword, return FALSE
        return False

print (contains_keyword("return","waasfsfqw"))