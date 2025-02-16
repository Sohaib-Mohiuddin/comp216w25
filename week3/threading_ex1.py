import threading, time

# Function for Thread 1
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate processing delay

# Function for Thread 2
def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulate processing delay

# Function for Thread 3
def print_status():
    for _ in range(5):
        print("Processing...")
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=print_status)

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()

print("All threads have completed execution!")
