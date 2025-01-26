#function triple_and_filter
#accepts list of numbers
#filers out every # that's not divisible by 4
#return a new list where every remaning # is tripled

def triple_and_filter(lst):
    return list(map(lambda n: n*3,filter(lambda n: n%4==0, lst)))
# Use map to iterate through n, for each n, multiple 3
# filter out n that are divisble by 4

print (triple_and_filter([1,2,4,4,48,16,20]))       