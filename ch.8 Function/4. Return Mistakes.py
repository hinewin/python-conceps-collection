# Mistake 1 (indentation)

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num%2 !=0:
            total += num
            #return total       
            # if return is placed here, the loop will
            #stops after going thru (1)
    return total # placing here the loop will keep going
    # since it will go for number in the list of numbers

print (sum_odd_numbers([1,2,4,7,8,9,10]))

########### UNCESSARY "ELSE"##############


def is_odd_number(num):
    if num%2 !=0:
        return True
    else:
        return False
## this can be shortened by 
def better_is_odd_number(x):
    if x %2 !=0:
        return True ## if it is odd return true
    return False # since its indented under IF # is odd, if its not
    # it will return FALSE


    