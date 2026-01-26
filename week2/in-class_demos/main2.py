# This script demonstrates how to import and use functions from other modules.
# It imports a constant and two functions from a utility module and uses them.
# It also imports a class from another module and creates an instance of that class.

from comp216_utils import PI, add, diff
from Person import Person

# Main method to demonstrate the use of imported functions and classes
if __name__=="__main__":
    # Constants and variables
    x = 231
    y = 123
    
    # Creating multiple instances of the Person class
    i = Person('Sohaib', 10)
    j = Person('Bob', 100)

    print(PI)
    print(add(x, y))
    print(diff(x, y))
    
    print('*' * 30)
    
    print(i, i.can_walk())
    