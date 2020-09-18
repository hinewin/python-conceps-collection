#Sorted = returns a new sorted list from items in iterable
# **** Sort() vs Sorted()
# Sort() modify list it is called on
#** more_numbers.(sort)
# Sorted() will create a new list containing a sorted version

more_numbers = [6,1,8,2]
print (sorted(more_numbers))
# sort will make more_numbers unchanged
#sorted will make a new list 

#Reverse

print (sorted(more_numbers, reverse = True))
#return [8,6,2,1]
# It accepts a tuple but will return a list
print (sorted((1,6,3,7,8)))
#return list

#### Example ####
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print (sorted(users,key= lambda user:user['username']))
# use lambda (quick functioN) parameter user
#(user is the value from key 'username')
sorted_list = (sorted(users, key=lambda user: len(user['tweets']),reverse=True))
print (sorted_list)


# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

print (sorted(songs, key=lambda s: s['playcount'],reverse=True))