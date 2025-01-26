## KEYWORD arguments
# If we know the parameter keyword, the order would NOT matter
# for the argument

def full_name (first, last):
    return (f"firstname: {first} and lastname: {last}")

print (full_name(last = "Nguyen", first ="Hai"))
# By knowing the keyword, the parameter order will not matter

## Why use Keyword Arguments?

# It is more flexible 