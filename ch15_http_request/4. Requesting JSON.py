import requests

url = "https://icanhazdadjoke.com/"
#response = requests.get(url, headers = {"Accept": "text/plain"}) #plain text
response = requests.get(url, headers = {"Accept": "application/json"}) #json 
    #headers specify we want the plain text version of the data


print (response.text) # same output but its a STRING
print (type(response.json())) # This will be a dictionary 
# lets save the json in a variable
data = response.json()
print (data["joke"]) # Now we will only print out the joke 
print (f"status: {data['status']}")

