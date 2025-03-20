'''
Created by Narendra for COMP216, August 2020
wk09a1_tcp_client.py

Demonstrate how to create a tcp socket.
'''

'''
First argument of the socket() method
class AddressFamily(enum.IntEnum)
 |  AF_APPLETALK = <AddressFamily.AF_APPLETALK: 16>
 |  AF_INET = <AddressFamily.AF_INET: 2>
 |  AF_INET6 = <AddressFamily.AF_INET6: 30>
 |  AF_IPX = <AddressFamily.AF_IPX: 23>
 |  AF_LINK = <AddressFamily.AF_LINK: 18>
 |  AF_ROUTE = <AddressFamily.AF_ROUTE: 17>
 |  AF_SNA = <AddressFamily.AF_SNA: 11>
 |  AF_SYSTEM = <AddressFamily.AF_SYSTEM: 32>
 |  AF_UNIX = <AddressFamily.AF_UNIX: 1>
 |  AF_UNSPEC = <AddressFamily.AF_UNSPEC: 0>

Second argument of the socket() method
class SocketKind(enum.IntEnum)
 |  SOCK_DGRAM = <SocketKind.SOCK_DGRAM: 2>
 |  SOCK_RAW = <SocketKind.SOCK_RAW: 3>
 |  SOCK_RDM = <SocketKind.SOCK_RDM: 4>
 |  SOCK_SEQPACKET = <SocketKind.SOCK_SEQPACKET: 5>
 |  SOCK_STREAM = <SocketKind.SOCK_STREAM: 1>

'''


#create a TCP client socket (SOCK_STREAM)

import socket

s = socket.socket(
	family=socket.AF_INET,        #can be AF_INET6
	type=socket.SOCK_STREAM,      #can be SOCK_DGRAM, SOCK_RAW
	proto=0)
# print(s)

host='localhost'
# host='www.python.org'             # host

# host='45.55.99.72'
port=12345
# port=80                           # port
address=(host, port)              # address must be a tuple
s.connect(address)                # connect to the remote socket
# print(s)
print(f'Socket Connected to {host} on port: {port}')
# s.close()

# #communicate with the host
BUFSIZ = 4096
# while True:
request = 'GET / HTTP/1.0\r\n\r\n'
s.send(request.encode('utf-8'))
data = s.recv(BUFSIZ)
# if not data:
# 	break
print(data.decode('utf-8'))

s.close()                         # closes the socket


