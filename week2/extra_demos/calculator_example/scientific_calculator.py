'''
This is a simple scientific calculator class will be used to perform basic arithmetic operations and scientific calculations.
This scientific calculator class will also be used to enhance the calculator class

It will inherit from the calculator class and will have the following methods:

- power: raises a number to the power of another number
- square_root: calculates the square root of a number
- factorial: calculates the factorial of a number
'''

from calculator import Calculator
import math

class ScientificCalculator(Calculator):
    def power(self, base, exponent):
        """
        Raises a number to the power of another number
        :param base: base number
        :param exponent: exponent number
        :return: result of base raised to the power of exponent
        """
        return math.pow(base, exponent)
    def square_root(self, number):
        """
        Calculates the square root of a number
        :param number: number to calculate the square root of
        :return: square root of the number
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(number)
    def factorial(self, number):
        """
        Calculates the factorial of a number
        :param number: number to calculate the factorial of
        :return: factorial of the number
        """
        if number < 0:
            raise ValueError("Cannot calculate factorial of a negative number")
        if number == 0 or number == 1:
            return 1
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result