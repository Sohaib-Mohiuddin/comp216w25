'''
Created by Narendra for COMP216, August 2020
wk09c1_udp_server.py

Create a udp server, read a message and then sends a response.
'''

#create a UDP socket (SOCK_DGRAM)
import socket

HOST = 'localhost'                # host name
PORT = 12345                      # port to listen at
ADDRESS = (HOST, PORT)            # 

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDRESS)

data, addr = server.recvfrom( 1024 )
resreq = f'UDP server is sending the following: {data}'
server.sendto(resreq.encode('utf-8'), addr)
