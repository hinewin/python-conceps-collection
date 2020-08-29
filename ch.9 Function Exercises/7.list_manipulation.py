#list_manipulation take 4 parameters (a list, command, location, and value)
# if command = "remove" and location = "end" 
## function removes last value in list and return the value removed
#if command = "add" and location is "beginning"
##function adds value (fourth parameter) to the beginning and return the list
#command ="add" and location = "end" 
## function should add value (fourth parameter) to end of list and return list

def list_manipulation(list,command,location,value = None):
    if command == "remove" and location == "end":
        return list.pop()
    elif command =="remove" and location == "beginning":
        return list.pop(0)
    elif command =="add" and location == "beginning":
        list.insert(0,value)
        return list
    elif command == "add" and location =="end":
        list.append(value)
        return list

print (list_manipulation([1,2,3],"remove","end"))
print (list_manipulation([1,2,3],"remove","beginning"))
print (list_manipulation([1,2,3],"add","beginning",20))
print (list_manipulation([1,2,3],"add","end","30"))