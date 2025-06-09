'''
Created by Narendra for COMP216 June 2020
wk05_1d_client_headers.py

Send a request with  customized headers

Try changing the payload dictionary and check 
the server console to see the modified header.
'''

import requests

URL = 'http://127.0.0.1:5000/test0'


# Allows you to spoof the server: 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'

payload = {'secret': 'h7#$@(&', 'boo': 'narendra'}
r = requests.get(URL, headers=payload)
print(f'        url: {r.url}')
# print(f'       json: {r.json()}')                #prints the json data
