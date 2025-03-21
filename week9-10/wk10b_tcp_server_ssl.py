'''
Author: Sohaib Mohiuddin

This is a complex TCP server that utilizes SSL to securely accept communication from 1 or more clients. The server receives a structures payload from the client, which is then stored in a PostgreSQL database. This application will utilize Socket I/O, SSL, Error Handling, logging, threading, serialization, and database operations.
'''

import socket
import ssl
import pickle
import psycopg2
import threading
import logging
import json
import os
from Student import Student
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create secure SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.load_cert_chain(certfile=os.getenv('SSL_CERT'), keyfile=os.getenv('SSL_KEY'))
context.load_cert_chain(certfile='randomcert.crt', keyfile='randomcert.key')

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 23456))
server_socket.listen(5)

# Function to handle client connections
def handle_client(client_socket, addr):
    logging.info(f"Connection from {addr}")
    try:
        # Wrap the client socket with SSL
        secure_client_socket = context.wrap_socket(client_socket, server_side=True)

        # Receive data from the client
        data = secure_client_socket.recv(4096)
        if not data:
            return

        # Deserialize the data
        payload = pickle.loads(data)
        student = Student.from_dict(payload)
        logging.info(f"Received payload: { student.to_dict() }")

        # Store the data in Supabase
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS')
        )
        cursor = conn.cursor()

        # If statement to check whether data already exists. If exists do not input data
        
        # Insert the data into the database
        cursor.execute(
            "INSERT INTO comp216_demo (name, age, course_name) VALUES (%s, %s, %s)",
            (student.name, student.age, student.course_name)
        )
        conn.commit()

        cursor.close()
        conn.close()
        logging.info("Data inserted successfully.")

    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        client_socket.close()

# Main server loop
try:
    logging.info("Server is listening...")
    while True:
        client_socket, addr = server_socket.accept()
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()
except KeyboardInterrupt:
    logging.info("Shutting down the server.")
finally:
    server_socket.close()