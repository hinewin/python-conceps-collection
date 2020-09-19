#function sum_even_values -- accept variable number of arguments
#return sum of all arguments that are divisible by 2
# if no num div by 2, return 0
# accept all numbers as invidiual arguments

# def sum_even_values(*nums):
#     for n in nums:
#         if n%2 ==0:
#             return sum([n])

# print (sum_even_values(23,322,4,8))


def sum_even_values(*nums):
    return sum(n for n in nums if n%2 ==0)
print (sum_even_values(2,3,4,4,9,10))