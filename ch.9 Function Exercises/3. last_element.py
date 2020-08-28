#Write a function called *** last_element***
#Takes in one parameter ( a list)
#returns the last value in the list
# None of list is empty

def last_element(list):
    if list:
        return list[-1]
    return None

print (last_element([]))