#intersection accept two lists
# return a list with the values that
#are in both input list
def intersection(list1,list2):
    return [i for i in list1 if i in list2]


print (intersection({1,1,2,4,6},{1,4,3,7,}))

#method 2

def intersection2(l1,l2):
    return [i for i in set(l1) & set(l2)]
print(intersection2({1,1,2,4,6},{1,4,3,7,}))

#method 3
def intersection3(l1,l2):
    final = []
    for i in l1:
        if i in l2:
            final.append(i)
    return final
print(intersection3({1,1,2,4,6},{1,4,3,7,}))
