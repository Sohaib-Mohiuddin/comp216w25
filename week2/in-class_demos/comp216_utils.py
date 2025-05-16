# This script demonstrates a utility file that will be imported in another script.

# PI is a constant that represents the mathematical constant pi.
PI = 3.141592653589793

# This function takes two numbers as input and returns their sum.
def add(x, y):
    return x + y

# This function takes two numbers as input and returns their absolute difference.
def diff(x, y):
    return (x - y) if x > y else (y - x)

# This function takes a radius as input and returns the area of a circle.
def area_of_circle(radius):
    return PI * radius * radius

# This function takes a width and length as input and returns the area of a rectangle.
def area_of_rectangle(width , length):
    return width * length