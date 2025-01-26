#CLEAR- clear all keys and values in a dictionary
d = dict(a=1,b=2,c=3)
print (d.clear()) #output: NONE

#COPY - makes a copy of a dictionary
dict1 = {"a": 1,
"b": 2,
"c": 3,
}
dict2 =dict1.copy()
print (dict2)

#FROMKEYS- creates key-value pairs from comma separated values:
#{}.fromkeys("key","value")
d1 = {}.fromkeys(["key"],"value")
d2 = {}.fromkeys(["email"],"unknown")
d3= {}.fromkeys(["list"],[1,2,3,4,5])
print (d1)
print (d2)
print (d3)

new_user = {}.fromkeys(["username","job","group"],"unknown")
print (new_user)

### GET- retrieves a KEY in an object and
# Return NONE instead of KeyError if key is not there
d= dict(a=1,b=4,cow=5)
print(d.get('cow'))
print (d.get('cat'))