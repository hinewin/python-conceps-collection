import requests
from random import choice
import pyfiglet
from termcolor import colored
header = pyfiglet.figlet_format("DAD JOKE 3000!")
header = colored (header, color = "magenta")
print (header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get (url,
 headers = {"Accept": "application/json"},
 params = {"term": user_input} ).json()

num_jokes = res["total_jokes"] #at the end of the list, theres a total
# jokes dict that tells you the total # of jokes. No need to use LEN
results = res['results']
if num_jokes > 1:
    print(f"I've found {num_jokes} about {user_input}. Here's one: ")
    print (choice(results)['joke']) # randomly pick an item from the list
    # then get key value from dict 'joke'
elif num_jokes == 1:
    print (f"I've found one joke about {user_input}")
    print (results [0]['joke']) # res["results"] is a list, we want to start from 0
#grab the first list, in the list a dict, grab the key 'joke' in the dict     

    

else:
    print (f"Sorry, couldn't find a joke with your term: {user_input}")