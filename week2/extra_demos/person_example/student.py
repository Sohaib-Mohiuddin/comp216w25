'''
This class will be used to extend the person class and will be used to initialize the student object with the given name, age, height, weight, student_id, and program
It will also be used to get the student_id of the student

It will have the following attributes:
- student_id: student id of the student
- program: program of the student

It will also have the following methods:
- get_student_id: returns the student id of the student
- set_student_id: sets the student id of the student
- get_program: returns the program of the student
- set_program: sets the program of the student
- __str__: returns a string representation of the student object
- __init__: initializes the student object with the given name, age, height, weight, and student_id
'''

from person import Person

class Student(Person):
    def __init__(self, name, age, height, weight, student_id, program):
        """
        Initializes the student object with the given name, age, height, weight, student_id, and program
        :param name: name of the student
        :param age: age of the student
        :param height: height of the student
        :param weight: weight of the student
        :param student_id: student id of the student
        :param program: program of the student
        """
        super().__init__(name, age, height, weight)
        self.student_id = student_id
        self.program = program
        
    def get_student_id(self):
        """
        Returns the student id of the student
        :return: student id of the student
        """
        return self.student_id
    
    def set_student_id(self, student_id):
        """
        Sets the student id of the student
        :param student_id: student id of the student
        """
        self.student_id = student_id
        
    def get_program(self):
        """
        Returns the program of the student
        :return: program of the student
        """
        return self.program
    
    def set_program(self, program):
        """
        Sets the program of the student
        :param program: program of the student
        """
        self.program = program
        
    def __str__(self):
        """
        Returns a string representation of the student object
        :return: string representation of the student object
        """
        return f'Student Identification: \nName: { self.name }, \nAge: { self.age } years old, \nHeight: { self.height }cm, \nWeight: { self.weight }kg, \nStudent ID: { self.student_id }, \nProgram: { self.program }'