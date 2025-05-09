# List of Strings
x = ['Sohaib', 'Bob', 'Angela', 'Jane', 'Christian', 'Builder']

# For Each Loop Example
for a in x:
    print(f'{ a }')

# For Loop with Range Example 1
for b in range(len(x)):
    print(x[b])

# For Loop with Range Example 2
for c in range(10):
    if (c % 2 == 0):
        print(f' { c }', end=' ') # Print all elements c in a single line
