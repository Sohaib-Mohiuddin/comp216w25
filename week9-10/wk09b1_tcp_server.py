'''
Created by Narendra for COMP216, August 2020
wk09b1_tcp_server.py

Demonstrate how to create a tcp socket that listens.
'''

import socket

HOST = 'localhost'                # host name
PORT = 3457                      # port to listen at

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))         # 
server.listen(5)                  #
server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

print('Server waiting for connection...')
client, addr = server.accept()    # blocks until a request in received
print(f'Client connected from: {addr}')

client.close()
server.close()
