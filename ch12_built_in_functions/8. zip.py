# ZIP- make an iterator that aggregates elements
#from each of the iterables
nums1= [1,2,3,4,5]
nums2= [6,7,8,9,10]
print (list(zip(nums1,nums2)))
#zip is an iterator of tuple, need to put in list
#[1,6],[2,7],[3,8]
print (dict(zip(nums1,nums2)))
# key1: value6
#2:7,3:8
#paring up the two tuples
# doesnt matter if tuples dont match, itll stop at the
#shortest tuple
######

five_by_two= [(0,1),(1,2),(2,3),(3,4),(4,5)]
print (list(zip(*five_by_two)))
# passing in *, will seperate the element into two tuples