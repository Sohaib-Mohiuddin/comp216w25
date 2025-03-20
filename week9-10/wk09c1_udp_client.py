'''
Created by Narendra for COMP216, August 2020
wk10e1_udp_client.py

Create a udp client, sends a message and read the response.
'''

import socket

HOST = 'localhost'                # host name
PORT = 12345                      # port to listen at
ADDRESS = (HOST, PORT)            # 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'Hello UDP server from Client'
client.sendto(message.encode(), ADDRESS)
data, addr = client.recvfrom( 1024 )
print(f'From server: {data.decode("utf-8")}')
client.close()
