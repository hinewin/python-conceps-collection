#function remove_negative that accepts a list of #
# and return a copy of lists with all negative # removed
def remove_negatives(lst):
    return list(filter(lambda num: num >=0,lst))
#return list of filter where
# for number in list, if number >= 0, return number
print(remove_negatives([-1,3,4,-99]))