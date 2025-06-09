'''
Created by Narendra for COMP216 June 2020
wk05_b2_webservice_post.py

Send a POST request to a webservices
'''

import requests

URL = 'http://127.0.0.1:5000/admin/add'          #request all users

prof = { 'yin': { 'fname': 'Yin', 'lname': 'Li', 'age': 30 }}
r = requests.post(URL, json=prof, timeout=4)     # make a HTTP GET request
if r.ok:                                         # check response status
    print(r.text)                                # get the json
else:                                                  
    print(r.status_code)                         # failure so display static code

print('fetching all the professors in the database')
URL = 'http://127.0.0.1:5000/profs/'
r = requests.get(URL)
print(r.json())
