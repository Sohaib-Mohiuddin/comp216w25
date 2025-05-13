# Example Person Class that takes name and age as parameters
# and has a method to check if the person can walk.
# This is a simple example of a class in Python.

class Person:
    #  Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # To String Method 
    def __str__(self):
        return f'This person\'s name is { self.name } and Age is { self.age }'

    def can_walk(self):
        return f'{ self.name } can walk!'
