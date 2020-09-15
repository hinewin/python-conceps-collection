#Filter - there is a lambda for each value in the iterable
# return filter object that can be converted into other iterables
# object contains ONLY values that return TRUE to lambda

l = [1,2,3,4]
odds = list(filter(lambda x:x%2 != 0, l))
#use list to pass filter. 
# lambda for x in list, if x modulo 2 is not =0, x is odd
print (odds)

#Ex 2 
names = ['austin','penny','anthony','angel','billy']
a_names = list(filter(lambda n: n[0]=='a',names))
print (a_names)

#Ex 3
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#long method
#####    inactive_users = list(filter(lambda u: len(u['tweets'])==0,users)
# False is when list = empty so false if list =[]
inactive_users = list(filter(lambda u: not u['tweets'],users))
# since filter will only returns what is TRUE
# if we leave it lambda u: u['tweets'] in list user, it will return
# users that tweeted. True != []
#hence we have to add not since it will include EMPTY string
#print (inactive_users)
# it will print out the whole dictionary

## Now we want to only Return ONLY usernames
list(map(lambda u: u['username'].upper(),# for each user, only select user
#instead of iterating through the whole dictionary
#we can iterate through the filtered out dictionary
    filter(lambda u: not u['tweets'],users)))
#ex4
#Return a new list with the string 
#"Your instructor is" + each value in the list if value <5 char
names = ['Lasie','Colt','Rusty']
print (list(map(lambda name: f"Your instructor is {name}",
filter(lambda char: len(char)<5,names))))