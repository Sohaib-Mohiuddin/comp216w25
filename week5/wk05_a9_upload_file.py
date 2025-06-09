'''
Created by Narendra for COMP216 October 2020
wk05_a9_upload_file.py

Uploads a file to a server
'''

import requests

file = 'test.txt'
URL = 'http://127.0.0.1:5000/uploads'           
files = {'file': open(file, 'rb')}
r = requests.post(URL, files=files)              # make a HTTP GET request
print(r.ok)                                      # check on the request
print(r.text)                                    # response from server