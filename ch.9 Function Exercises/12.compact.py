#compact accepts a list and returns
# a list of values that are truthy values
#without any of falsey values

def compact(list):
    return [i for i in list if i]
        
print (compact([0,1,2,"",[], False, {}, None, "All done"]))