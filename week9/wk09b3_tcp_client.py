'''
Created by Narendra for COMP216, August 2020
wk09a2_tcp_client.py

Create a tcp socket and reads the response.
'''

import socket
s = socket.socket(
	family=socket.AF_INET,        #can be AF_INET6
	type=socket.SOCK_STREAM,      #can be SOCK_DGRAM, SOCK_RAW
	proto=0)

# host='www.python.org'             # host
host='www.google.com'
port=80                           # port
s.connect((host, port))           # connect to the remote socket
print(f'Socket Connected to {host} on port: {port}')

BUFSIZ = 4096
request = 'GET / HTTP/1.0\r\n\r\n'
s.send(request.encode('ISO-8859-1'))

while True:
    data = s.recv(BUFSIZ)
    if not data:                  # keep reading until no data
        break
    print(data.decode('ISO-8859-1'))   # decode before printing

s.close()                         # closes the socket


