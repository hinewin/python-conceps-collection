#Generator Expressions-  Save space & Less memory intensive
names = ['Sally','Shay','Jay','Shen']
print(all(name[0]== 'S'for name in names ))
#- To save space you dont have to add list brackets for list comprehension
#  When you dont want to return a list, and to test
#Use generator if youre iterating once.
#List comprehension when you want to store & use the results

###### Demo
import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

