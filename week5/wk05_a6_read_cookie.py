'''
Created by Narendra for COMP216 October 2020
wk05_a6_read_cookie.py

Reads a cookie
'''

import requests

URL = 'https://google.com'                       #this site uses cookies           
URL = 'https://centennialcollege.ca'                       #this site uses cookies           
 
r = requests.get(URL)
d = r.cookies.get_dict()                         #get the data as a dict
for k, v in d.items():                         
    print(f'{k}: {v}')                           #print the key and the value
