# Write function max_magnitude - accepts single list full of #
# return magnitute of the number with largest magnitutde
# (number that is furthest away from zero)

def max_magnitude(lst):
    return(max(abs(l) for l in lst))
# absolute value for EACCH number in list
#abs cannot be applied to entire list has to use list comp
print (max_magnitude([3,4,3]))