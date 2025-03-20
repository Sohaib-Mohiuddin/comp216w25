import socket
import ssl
import pickle
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection parameters
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

# Create a secure SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Wrap the socket with SSL
secure_socket = context.wrap_socket(server_socket, server_side=True)

print("Server is listening...")

while True:
    client_socket, addr = secure_socket.accept()
    print(f"Connection from {addr}")

    try:
        # Receive data from the client
        data = client_socket.recv(4096)
        if not data:
            break

        # Deserialize the data
        payload = pickle.loads(data)
        print(f"Received payload: {payload}")

        # Store the data in Supabase
        conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASS)
        cursor = conn.cursor()

        # Assuming payload is a dictionary with keys 'name', 'age', and 'course_name'
        cursor.execute("INSERT INTO comp216_demo (name, age, course_name) VALUES (%s, %s, %s)", 
                       (payload['name'], payload['age'], payload['course_name']))
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()