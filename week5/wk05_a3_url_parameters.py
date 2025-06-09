'''
Created by Narendra for COMP216 June 2020
wk05_a2_url_parameters.py

Send a request with url parameters to a web server 
and examine the resulting response object.

Try changing the query string and see if the 
server returns your query string

N.B. You can also use a dictionary to send the 
parameters as payload
'''

import requests

URL = 'http://127.0.0.1:5000/test2?name=pershad&course=COMP216&year=2020'

r = requests.get(URL)
print(f'    url: {r.url}')                  #the url
print(f'     ok: {r.ok}')                   #
print(f'content: {r.content}')              #the byte of the content
print(f'   json: {r.json()}')               #crashes if there is no json

