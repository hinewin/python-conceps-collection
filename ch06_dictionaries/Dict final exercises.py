# given two lists
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
# Create a dict that looks like this
#{'CA:California",'NJ': 'New Jersey'}

answer = {list1[i]:list2[i] for i in range (0,len(list1))}
print(answer)

