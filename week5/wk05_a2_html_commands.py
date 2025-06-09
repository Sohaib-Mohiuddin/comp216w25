'''
Created by Narendra for COMP216 June 2020
wk05_a2_html_commands.py

Sends an html command to a web page and examine 
the resulting response object
'''

import requests

# URL = 'http://127.0.0.1:5000/'                   #first try
URL = 'http://127.0.0.1:5000/test0'              #then try this
#                                                Now try with different clients 
#                                                e.g. different browsers
#                                                curl 'http://127.0.0.1:5000/test0'
#                                                nc 127.0.0.1 5000
#                                                then enter the following
#                                                GET /test0 /HTTP/1.1

# URL = 'http://127.0.0.1:5000/test1'              #second try, gets a json
# URL = 'https://w3schools.com/python/demopage.htm'#third attempt
# URL = 'http://httpbin.org/'                      #fourth attempt

res = requests.get(URL)                     # make a HTTP GET request
# res = requests.head(URL)                    # makes a HEAD request
# res = requests.options(URL)                 # makes an OPTION request
#                                             # examine the ALLOW key of
#                                             # the response headers
# res = requests.post(URL)                    # makes a POST request
# res = requests.put(URL)                     # makes a PUT request
# res = requests.delete(URL)                  # makes a DELETE request
# res = requests.patch(URL)                   # makes a PATCH request

print(f'         ok: {res.ok}')             # a better way to check on success
print(f'status code: {res.status_code}')    # status code of the response
print(f'   encoding: {res.encoding}')       # the encoding of the response
print(f'    content: {res.content}')        # the byte representation of the response
print(f'    headers: {res.headers}')        # the headers
print(f'       text: {res.text}')           # display the text of the response
print(f'        url: {res.url}')            # the url
print(f'    history: {res.history}')        # the history
print(f'    cookies: {res.cookies}')        # the history
# print(f'       json: {res.json()}')         #there is no json in the first or second try

# Request verbs that may be sent to a web server

# GET requests a specific resource in its entirety
# HEAD requests a specific resource without the body content. Useful for caching purposes or to check if the document exist at all
# POST adds content, messages, or data to a new page under an existing web resource
# OPTIONS shows users which HTTP methods are available for a specific URL
# PUT directly modifies an existing web resource or creates a new URI if need be
# DELETE gets rid of a specified resource
# TRACE shows users any changes or additions made to a web resource
# CONNECT converts the request connection to a transparent TCP/IP tunnel
# PATCH partially modifies a web resource

# All HTTP servers use the GET and HEAD methods, but not all support the rest of these request methods.