# This script demonstrates the usage of exception handling in Python along with importing a class from another module.

from Person import Person

# Main method to demonstrate the use of exception handling
if __name__ == "__main__":
    # List of names
    some_list = ['bob', 'jane', 'cat', 'dog', 'scooby doo']
    
    # Try block to handle exceptions
    # It attempts to create instances of the Person class with names from the list.
    # If an exception occurs, it will be caught in the except block.
    # The exception message will be printed along with the traceback.
    # The traceback provides information about where the exception occurred in the code.
    # The traceback is useful for debugging and understanding the flow of the program.
    try:
        for some_name in range(6):
            print(Person(some_list[some_name], 20))
    except Exception as e:
        print(f'Some exception occurred: { e }')