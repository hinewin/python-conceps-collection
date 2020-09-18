# REVERSED not reverse- return a reverse ITERATOR
num = [1,2,3,4]
num.reverse() # 
print (num)
print (reversed([4,3,2,1]))
#reverse iterator object


for x in reversed(range(0,10)):
    print (x)
# list.reverse() only works with LIST
# use reversed to return reverse ITERATOR( loop thru quickly)
# if we need to assign to a variable we can use a list