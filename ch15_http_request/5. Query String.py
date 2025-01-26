# What's a Query String?
#- A way to pass data to the server as part of a GET request
# http://www.example.com/?key1=value1&key2=value2
#- Give more info for the request


#break it apart using the & sign
# https://www.google.com/search?rlz=1C1CHBF_enUS858US858&
# sxsrf=ALeKk033W1Tju2Q0GAU3k2sSRl5y7yyn3Q%3A1601440321453&
# ei=QQp0X66EG6Ti9APG9L_IBg&
# q=what+is+aan+api& #q = query 
# oq=what+is+aan+api& # oq= original query
# gs_lcp=CgZwc3ktYWIQAzIHCCMQsQIQJzIGCAAQBxAeMgYIABAHEB4yBAgAEAoyBggAEAcQHjIGCAAQBxAeMgQIABAKMgQIABAKMgQIABAKMgQIABAKOgcIABBHELADOgQIIxAnOgcIABAUEIcCOgUIABCRAjoCCABQzw9Y4htgiCFoAXACeACAAV2IAaoBkgEBMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjuqPSLhpDsAhUkMX0KHUb6D2kQ4dUDCA0&uact=
# google internal stuff

# Each website has a different parameter to search

# 2 options of Query string
#Option 1: Hardcoded

import requests
# reponse = requests.get("http://www.example.com?key1=value&key2=value2")

#Option 2: Parameters - most preferable way
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers = {"Accept": "application/json"},
    params ={"term": "cat", "limit": 1}
    )

data = response.json()
print (data["results"])
#print(data["joke"])
#print (f"status:{data['status']}")

