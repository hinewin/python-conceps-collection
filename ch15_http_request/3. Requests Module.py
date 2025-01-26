# requests Module
# Makes HTTP requests from Python code
# USeful for web scrapping/crawling, grabbing data from other APIs, etc
# Install using PIP
 
import requests
url = "https://www.google.com" # will need http
response = requests.get(url)

print (f"Your request to {url} came back w/ status code {response.status_code}")

print (response.text)


################
response = requests.get(
    "https://www.google.com",
    headers ={    # Use headers to specify what kind of data we want
        "header1": "value1",
        "header2": "value2"
    }

#JSON is a data format that Python can quickly turn into Python code