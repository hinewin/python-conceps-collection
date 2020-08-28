#What is a tuple?
#- Ordered collection/ grouping of items
numbers = (1,2,3,4)
# it is IMMUTABLE
# IT cannot be changed like a list
x = (1,2,3)
print (3 in x) #output: TRUE
#print (x[0] =2) #output: ERROR because it is IMMUTABLE
# WHY USE IMMUTABLE?
# - Faster, safer(from bugs), Valid keys in a dictionary
# some methods return a tuple. ex) .items()
month = ('January','February','March','April','May','June') # good ex of tuple
# ACCESSING TUPLE
# use [], month[1] == February 

locations = { ## Using tuple as a key
    (35,6895,39.6817): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749,122.4194): "San Francisco Office"   

}
print (locations[35,6895,39.6817])
# Cannot use LIST as a key but can use TUPLE if data needs to be a key in a dict
# Anything.() will return a tuple
#When run .() it will not be changed so they are tuples 