#Multiply_even_numbers
#accepts list of numbers
#returns the product of all even numbers in the list


def Multiply_even_numbers(numbers):
    x = 1
    for num in numbers:
        if num%2==0:
            x = x*num
    return x        




print (Multiply_even_numbers([1,2,3,4,5,6]))