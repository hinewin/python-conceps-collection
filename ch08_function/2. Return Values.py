# def print_square_of_7():
#     print(7**2)
# print_square_of_7()

def print_square_of_7():
    print ("this is before the return") # this will be returned 
    return 7**2  #### the output will be returned and captured
   # print ("I AM AFTER THE RETURN!") # this will not be an output (behind return)
# BUT it will EXIT the function



#Return will POPS the function off the call stack****
result = print_square_of_7()
print (result)