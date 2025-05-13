# This script demonstrates how to use command line arguments in Python.
# It takes two strings and two integers as input and performs some operations.
# Importing the sys module to access command line arguments

import sys # adds more functions to the current environment

# Variables to store command line arguments
a = sys.argv[1]
b = sys.argv[2]
c = int(sys.argv[3])
d = int(sys.argv[4])

# Function to process the first two arguments and return a formatted string
def process(a, b):
    return f'Hello { a }, Your age is { b }'

# Function to multiply the last two arguments and return a formatted string
def mult(c, d):
    return f'The multiplication of { c } and { d } is { c * d }'

# Print the number of command line arguments and the arguments themselves
print(f'Number of arguments: {len(sys.argv)}')

# Print the command line arguments
print(f'Arguments are: {sys.argv}')

# Print the script name
print(f'The name of the script: {sys.argv[0]}')

print('*' * 30)

print(process(a, b))
print(mult(c, d))