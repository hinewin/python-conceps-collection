#ex) 1
numbers = dict(first=1, second=2,third=3)
squared_numbers = {
    key:value**2 for key,value in numbers.items()
#Since using value we nust include .items()
#for each key, value ^2 
}
print (squared_numbers)
#output: first:1, second =4, third = 9
#ex) 2
ex_2 = {num: num**2 for num in [1,2,3,4,5]}
# for each value, value = key^2 in key (1-5)
print (ex_2)
#output:
#1:1, 2:4, 3:9, 4:16, 5:25

#ex) 3

str1 = "ABC"
str2 = str(123)
combo = {str1[i]:str2[i] for i in range (0,len(str1))}
#for each item in str1 is key, each item in str2 is value
#for each item print value,key in range 0 to the length of str1

print(combo)
#output:
# A:1, B:2, C:3

#ex) 4
student = {
    "name": "Hai",
    "last name": "Nguyen",
    "Color": "Blue"
}
student1 = {k.upper():v.upper() for k,v in student.items()}

#student1 = key upper and value upper
#for the key and value from student dict
#since were using both key and value, we will include items()
print (student1)


# Conditional Logic With Dictionaries 
num_list =[1,2,3,4]

parity = {num:("even" if num%2 ==0 else "odd") for num in range(1,101)}
print (parity)
#### Using student example
student = {
    "name": "Hai",
    "last name": "Nguyen",
    "Color": "Blue"
}
student2 = {k.upper() if k is "Color" else k: v.upper() for k,v in student.items()}
#print key in upper only if key = Color
#else print regular key and capitalize all values
print (student2)