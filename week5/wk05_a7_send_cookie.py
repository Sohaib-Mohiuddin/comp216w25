'''
Created by Narendra for COMP216 October 2020
wk05_a7_send_cookie.py

Sends a cookie to a server
'''

import requests

URL = 'http://127.0.0.1:5000/cookies'            #request all users
cookies = {'professor': 'Narendra Pershad', 'course': 'Networking for Software Developers'}
 
r = requests.get(URL, cookies=cookies)
print(r.text)                                    #ther particular server sends cookies back to client
