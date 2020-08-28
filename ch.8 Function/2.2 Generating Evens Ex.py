# Write function generate_evens that
## returns a list of even numbers between (1-50)excluding 50
#inside function, construct the list using loop/list comprehension

def generate_evens():
    result =[] # create a variable to store the result
    for x in range (1,50): # for each num between (1,50)
        if x % 2 ==0: # if num devided by 2
            result.append(x) # put those num in result
    return(result)

### SHORTER way
print (generate_evens())

def generate_odds():
    return [x for x in range(1,50) if x%2 !=0]
    # return num for each of num between 1,50
    #only if theyre are not devided by 2
print (generate_odds())