'''
This class will be used to create a simple calculator that can perform basic arithmetic operations.
It will be used as a base class for the calculator and will be inherited by the scientific calculator class

The calculator class will have the following methods:
- add: adds multiple numbers
- subtract: subtracts multiple numbers
- multiply: multiplies multiple numbers
- divide: divides multiple numbers
'''
class Calculator:
    def add(self, *args):
        """
        Adds multiple numbers
        :param args: numbers to be added
        :return: sum of the numbers
        """
        return sum(args)

    def subtract(self, *args):
        """
        Subtracts multiple numbers
        :param args: numbers to be subtracted
        :return: difference of the numbers
        """
        return args[0] - sum(args[1:])

    def multiply(self, *args):
        """
        Multiplies multiple numbers
        :param args: numbers to be multiplied
        :return: product of the numbers
        """
        result = 1
        for arg in args:
            result *= arg
        return result

    def divide(self, *args):
        """
        Divides multiple numbers
        :param args: numbers to be divided
        :return: quotient of the numbers
        """
        if len(args) == 0:
            raise ValueError("At least one number is required")
        
        result = args[0]
        
        for arg in args[1:]:
            if arg == 0:
                raise ValueError("Cannot divide by zero")
            result /= arg
        
        return result
    