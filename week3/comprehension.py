"""
List comprehension
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or a range) and optionally filtering items based on a condition.
List comprehension syntax:
```python
new_list = [expression for item in iterable if condition]
```
"""

# Example of list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: { squares }")

# Example with a condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: { evens }")

# Example with a function
def square(x):
    return x ** 2

squared_values = [square(x) for x in range(10)]
print(f"Squared Values: { squared_values }")

# Example with nested loops
matrix = [
    [1, 2, 3], 
    [5, 3, 4]
]
flattened = [(x, y) for x in matrix[0] for y in matrix[1] if x != y]
print(f"Flattened Matrix: { flattened }")