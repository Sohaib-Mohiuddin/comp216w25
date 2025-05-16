'''
This is a simple person class that will be used to demonstrate the use of classes, objects, and inheritance in Python.
This person class will have the following attributes:
- name: name of the person
- age: age
- height: height
- weight: weight
This person class will also have the following methods:
- get_name: returns the name of the person
- get_age: returns the age of the person
- get_height: returns the height of the person
- get_weight: returns the weight of the person
- set_name: sets the name of the person
- set_age: sets the age of the person
- set_height: sets the height of the person
- set_weight: sets the weight of the person
- __str__: returns a string representation of the person object
- __init__: initializes the person object with the given name, age, height, and weight
'''

class Person:
    def __init__(self, name, age, height, weight):
        """
        Initializes the person object with the given name, age, height, and weight
        :param name: name of the person
        :param age: age of the person
        :param height: height of the person
        :param weight: weight of the person
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_name(self):
        """
        Returns the name of the person
        :return: name of the person
        """
        return self.name
    
    def get_age(self):
        """
        Returns the age of the person
        :return: age of the person
        """
        return self.age
    
    def get_height(self):
        """
        Returns the height of the person
        :return: height of the person
        """
        return self.height
    
    def get_weight(self):
        """
        Returns the weight of the person
        :return: weight of the person
        """
        return self.weight
    
    def set_name(self, name):
        """
        Sets the name of the person
        :param name: name of the person
        """
        self.name = name
        
    def set_age(self, age):
        """
        Sets the age of the person
        :param age: age of the person
        """
        self.age = age
        
    def set_height(self, height):
        """
        Sets the height of the person
        :param height: height of the person
        """
        self.height = height
        
    def set_weight(self, weight):
        """
        Sets the weight of the person
        :param weight: weight of the person
        """
        self.weight = weight
    
    def __str__(self):
        """
        Returns a string representation of the person object
        :return: string representation of the person object
        """
        return f'Person Identification: \nName: { self.name }, \nAge: { self.age } years old, \nHeight: { self.height }cm, \nWeight: { self.weight }kg'