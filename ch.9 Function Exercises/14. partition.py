#function partition- accepts a list and a callback function (True or False)
#function iterate over each element in the list,
#invoke callback each iteration
# if callback = True, element goes into the FIRST list (truthy list)
# if callback = False, element goes into SECOND list (falsy list)
# when finished, partition return both lists in 1 large list


def isEven(num):
    return num%2 ==0 

def partition(list,callback):
    true_list = []
    false_list = []
    for i in list:
        if callback(i):
            true_list.append(i)
        else:
            false_list.append(i)
    return true_list,false_list

print(partition([1,2,3,4], isEven))


#Solution 2:
def partition2(list,fn):
    return [i for i in list if fn(i)], [i for i in list if not fn(i)]

print(partition2([1,2,3,4], isEven))
