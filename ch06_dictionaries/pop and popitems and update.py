#POP takes a single argument(key) to remove key-value pair from a dict
#Return the value that was removed
student = dict(name = "hai", funny = False, favorite_language = "Python", favorite_number = 9)

student.pop("name")
print (student)

#POPITEM
# Removes a random key in a dictionary
student.popitem()
print (student) 

#Update
#Update keys and values in a dictionary with another set of key value
student_update={}
student_update.update(student)
print (student_update)