# *args - a special operator we can pass to functions as a parameter
# gather arguments as a tuple 
# JUST a parameter, can call whatever you want(has to start with *)

def sum_all_nums(num1,num2,num3): # INSTEAD of adding more parameters
    #to hold num4, num5, we can use *args
    return num1+num2+num3

print (sum_all_nums(4,6,9))

def sum_nums(*args):
    print(args)

print (sum_nums(4,7,8,9,6)) 
# output: (4,7,8,9,6) its a tuple (cant be changed)


def iterate(num1,*args):
    total = 0
    print (num1) # print first variable, then the rest
    for num in args:
        total += num
    return total

print (iterate(1,1,5))


def ensure_correct_info(*args):
    print(f"input: {args}")
    if "Hai".lower() in args and "Nguyen".lower() in args:
        return "Welcome back Hai"
    else:
        return "Not sure who you are..."

print (ensure_correct_info("he",1,3,"nguye"))
print (ensure_correct_info("hai",1,3,"nguyen"))