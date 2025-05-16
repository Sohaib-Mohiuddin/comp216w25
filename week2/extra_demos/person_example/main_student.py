'''
This is the main file for the student class
It will be used to test the student class
'''

from student import Student
from person import Person

if __name__ == "__main__":
    # Create an instance of the Person class
    person = Person("Jane Doe", 25, 165, 60)
    
    # Print the person object
    print(person)
    
    print(f'\n{ '*' * 20 }\n')
    
    # Create an instance of the Student class
    student = Student("John Doe", 20, 180, 75, "301301301", "Computer Science")
    
    # Print the student object
    print(student)