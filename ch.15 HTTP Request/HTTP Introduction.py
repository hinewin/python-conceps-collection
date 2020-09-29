# How the internet works when browsing
# 1) DNS lookup (find the IP with the given domain)

# 2) Computer makes request to server
# 3) Server Processes the Request
# 4) Server issues a RESPONSE
#***** 2>4 is called a Request/Response cycle


# HTTP Headers
# - Sent with both requests and responses
# - Provide additional information about the request/response

# Header Examples

#* Request Headers***
# Accept- Acceptable content-types for response (html,json,xml)
# Cache-Control- Specify caching behavior
# User-Agent - Information about the software used to make the request

#* Response Headers**
# Access-Control-Allow-Origin- specify domains that can make requests
# Allowed- HTTP verbs that are allowed in requests

#Response Status Codes
#- Every request theres a reponse
# 2xx- Success (starts with 2)
# 3xx- Redirect
# 4xx- CLIENT error (your fault)
# 5xx- SERVER Error (NOT your fault)