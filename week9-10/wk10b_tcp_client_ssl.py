'''
Author: Sohaib Mohiuddin

This is a complex TCP client that utilizes SSL to securely communicate with a server. The client sends a structures payload to the server, which is then stored in a PostgreSQL database. This application will utilize Socket I/O, SSL, Error Handling and logging.
'''

import socket
import ssl
import pickle
import logging
import json
import os
from Student import Student
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a secure SSL context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # For self-signed certificates

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
secure_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Connect to the server
try:
    secure_socket.connect(('localhost', 23456))

    # Create a payload to send
    student = Student(name='Jane Harbinger', age=25, course_name='Python Programming')

    # Serialize the payload
    data = pickle.dumps(student.to_dict())

    # Send the serialized data
    secure_socket.sendall(data)
    logging.info("Data sent successfully.")

except Exception as e:
    logging.error(f"Error: {e}")
finally:
    secure_socket.close()