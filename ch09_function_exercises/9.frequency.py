# frequency - accepts a list and a search_term (primitive value)
# returns the number of times the search_term appears in the list


# def frequency(list,term):
#     count = 0
#     for word in list:
#         if word == term:
#             count += 1
#     return count
    
def frequency(list,word):
    return list.count(word)

print (frequency([1,2,3,4,4,4], 4))
print (frequency([True, False, True, True], False))