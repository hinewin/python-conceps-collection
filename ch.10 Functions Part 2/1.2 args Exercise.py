#Define a function called contains_purple that
#accepts any number of arguments
# return True if any of arguments are "purple" all lowercase
# else return False

def contain_purple(*colors):
    if "purple" in colors: # if "purple is in the colors parameter"
        return True # return true
#if its not return false
    return False