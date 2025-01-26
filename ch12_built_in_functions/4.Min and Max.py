#Max return the LARGESt item in an ITERABLE or
#LARGEST of two or more ARGUMENTS
print (max([2,5,999,99,9]))
#999
print (max('c','d','z'))
# Return the largest item in an iterable/ largest of 2 arguments
print (max({5:'a',3:'c',2:'b'}))
# highest KEY= 5

#Min same, but LOWEST

print (min("hello world"))
# Space is lowest so itll print out nothing 
print (min("helloworld"))
# D is the min (A-Z) Z being highest

#Find the maximum length
names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

min(names) # would only return based on alphabetically (AYRA) a being lowest
#solution1
print (min(len(name) for name in names))  #Generator (short & quick)
#3 -  the lowest(shortest) length is 3
# IF we want to use the list then use List 
print ([len(name) for name in names])
# [4,6,4,3,10]
# max = [10]

# Now we want to print out the NAME that has the longest length

print (max(names,key=lambda n: len(n)))
# "Ollivander"

print (min(names,key =lambda n: len(n)))

### Song Example


songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]
# Song with the minimum of play (least play)

print (min(songs, key=lambda song: (song['playcount'])))

# parameter passed through key must be something callable (lambda)
#in the list of songs, for song, find the minimum playcount
# happy birthday, playcount:1

print(max(songs,key=lambda s: s["playcount"])["title"])
#in list of songs, generate a dict with lowest playcount
# and only shows title 
