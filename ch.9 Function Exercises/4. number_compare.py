# Function number_compare takes two parameters (both numbers)
# if first is greater than second:
#   return "First is greater" likewise
#Otherwise Numbers are equal

def number_compare(a,b):
    if a>b:
        return"First is greater"
    elif b>a:
        return "Second is greater"
    return "Numbers are equal"

print (number_compare(4,2))