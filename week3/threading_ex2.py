import threading
import time

# Shared resources
log_lock = threading.Lock()
pause_event = threading.Event()
pause_event.set()  # Initially not paused

# Function for Number Processor
def number_processor():
    for i in range(1, 11):
        pause_event.wait()  # Wait until not paused
        with log_lock:
            print(f"Number: {i}")
        time.sleep(1)  # Simulate processing delay

# Function for Letter Processor
def letter_processor():
    for letter in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        pause_event.wait()  # Wait until not paused
        with log_lock:
            print(f"Letter: {letter}")
        time.sleep(1)  # Simulate processing delay

# Function for Status Monitor
def status_monitor():
    for _ in range(10):
        with log_lock:
            print("Status: Processing...")
        time.sleep(1)

# Function to pause and resume threads
def control_threads():
    while True:
        command = input("Enter 'pause' to pause, 'resume' to resume, or 'exit' to stop: ").strip().lower()
        if command == 'pause':
            pause_event.clear()  # Pause all threads
            with log_lock:
                print("Threads paused.")
        elif command == 'resume':
            pause_event.set()  # Resume all threads
            with log_lock:
                print("Threads resumed.")
        elif command == 'exit':
            pause_event.clear()  # Stop processing
            break
        else:
            with log_lock:
                print("Unknown command. Please enter 'pause', 'resume', or 'exit'.")

# Creating threads
number_thread = threading.Thread(target=number_processor)
letter_thread = threading.Thread(target=letter_processor)
status_thread = threading.Thread(target=status_monitor)
control_thread = threading.Thread(target=control_threads)

# Starting threads
number_thread.start()
letter_thread.start()
status_thread.start()
control_thread.start()

# Wait for all threads to complete
number_thread.join()
letter_thread.join()
status_thread.join()
control_thread.join()

print("All threads have completed execution!")
