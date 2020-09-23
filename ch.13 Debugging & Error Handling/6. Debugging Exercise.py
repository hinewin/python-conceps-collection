# Function "divide"- accepts 2 parameters (num1,num2)
# return result of num1/num2
# if do not pass same type of arguments
## return "Please provide two integers or floats"
# if num2 ==0, raise ZeroDevisionError
## return "Please do not divide by zero"

# def divide(num1,num2):
#     try:
#         return num1/num2
#     except TypeError:
#         return ("Please provide two integers or floats")
#     except ZeroDivisionError:
#         return ("Please do not divide by zero")
    
#print (divide(4,2))  #2
#print (divide([],"1")) #  "Please provide two integers or floats"
#print (divide(1,0)) #  "Please do not divide by zero"


### OR

def divide(num1,num2):
    try:
        result = num1/num2
    except TypeError:
        return ("Please provide two integers or floats")
    except ZeroDivisionError:
        return ("Please do not divide by zero")
    return result
    
print (divide(4,2))  #2
print (divide([],"1")) #  "Please provide two integers or floats"
print (divide(1,0)) #  "Please do not divide by zero"