'''
Created by Narendra for COMP216 June 2020
wk05_b1_webservice_get.py

Send a GET request to a webservices
The server returns json like below:
{ 'ilia': { 'fname': 'Ilia', 'lname': 'Nika', 'age': 56 }}
'''

import requests

URL = 'http://127.0.0.1:5000/profs/'             #request all users

r = requests.get(URL, timeout=4)                 # make a HTTP GET request

if r.ok:                                         # check response status
    users = r.json()                             # get the json
    print(users)
    # for user in users:                           # iterate each item
        # print(f"{users[user]['fname']} {users[user]['lname']} ({users[user]['age']})")
else:                                                  
    print(r.status_code)                         # failure so display static code
