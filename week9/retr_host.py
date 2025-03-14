import socket
#getting the host name and ip address of a local machine
name = socket.gethostname()
print(f'Hostname of local machine is {name}')
ip_addr = socket.gethostbyname(name)
print(f'IP address of {name} is {ip_addr}')