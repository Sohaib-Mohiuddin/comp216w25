import socket
import ssl
import pickle

# Create a secure SSL context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # For self-signed certificates

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
secure_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Connect to the server
secure_socket.connect(('localhost', 12345))

# Create a payload to send
payload = {
    'name': 'Mark Blue',
    'age': 65,
    'course_name': 'Networking for Software Developers'
}

# Serialize the payload
data = pickle.dumps(payload)

# Send the serialized data
secure_socket.sendall(data)

# Close the socket
secure_socket.close()