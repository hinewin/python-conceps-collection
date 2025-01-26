# Psudo code
# Ask for topic- input("Give me a topic")
# Genera a list of jokes, counts how many "results"("i've got 4 jokes")
# if result >1 randomly sample one/choose one
# Import random.choice to select one of the jokes ("here's one:")
#print out the joke
 
#if jokes ==1, "i got one joke about the fruit"
# if theres no jokes, "sorry theres no jokes about {input}"

import requests
from random import choice 

topic = input("Let me tell you a joke!, Give me a topic: ")
url = "https://icanhazdadjoke.com/search"

get_jokes = requests.get(url,
        headers = {"Accept": "application/json"},
        params= {"term":topic})

data = get_jokes.json()

jokes = data['results']
jokes_len = len([(joke) for joke in jokes])


all_jokes = (choice([(joke) for joke in jokes])) # one of the jokes

final_joke = all_jokes['joke']

if jokes_len > 1:
    print (f"I've got {jokes_len} jokes about {topic}. Here's one:\n{final_joke}")

