# Use if (conditional logic)
numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num%2 == 0]
odds = [num for num in numbers if num%2 != 0]
print (f"this is even: {evens} and this is odd: {odds}")

## You can also use else
# for evens print out, for odds devide by 2
else_statement = [num if num%2 ==0 else num/2 for num in numbers]
print (else_statement)


### Join String Example
with_vowels = "This is so much fun!"
new = "".join(char for char in with_vowels if char not in "tsfthisisosmuch!")
print (new)
