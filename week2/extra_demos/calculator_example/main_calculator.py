'''
This is the main file for the calculator program.
It will be used to test the calculator and scientific calculator classes.
It will also be used to demonstrate the use of the calculator and scientific calculator classes.
'''

from scientific_calculator import ScientificCalculator

if __name__ == "__main__":
    # Create an instance of the ScientificCalculator class
    calculator = ScientificCalculator()

    # Test the add method
    print(f'Addition: { calculator.add(1, 2, 3, 4, 5) }')  # Output: 15
    
    # Test the subtract method
    print(f'Subtraction: { calculator.subtract(10, 5, 2) }')  # Output: 3
    
    # Test the multiply method
    print(f'Multiplication: { calculator.multiply(2, 3, 4) }')  # Output: 24
    
    # Test the divide method
    print(f'Division: { calculator.divide(100, 5, 2) }')  # Output: 10.0
    
    # Test the power method
    print(f'Power: { calculator.power(2, 3) }')  # Output: 8.0
    
    # Test the square_root method
    print(f'Square Root: { calculator.square_root(16) }')  # Output: 4.0
    
    # Test the factorial method
    print(f'Factorial: { calculator.factorial(5) }')  # Output: 120
    