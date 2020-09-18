#len - return the length of a number of items of an object
#argument may be a sequence (string,tuple,list,range) or
#collect (dictionary,set)

len('hi')
# in the background its actually calling
#    hi.__len__()