"""
This script demonstrates how to handle exceptions in Python.
It includes examples of catching specific exceptions, using a try-except block,
and finally block for cleanup actions.
It also shows how to raise exceptions intentionally.
"""

def divide_numbers(num1, num2):
    """
    Divides two numbers and handles division by zero exception.
    
    Args:
        num1 (float): The numerator.
        num2 (float): The denominator.
        
    Returns:
        float: The result of the division if successful, None if an exception occurs.
    """
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero. {e}")
        return None
    else:
        return result
    finally:
        print("Execution of divide_numbers completed.")
        
def int_user_input(prompt):
    """
    Converts user input to an integer and handles ValueError exception.
    
    Args:
        prompt (str): The input prompt for the user.
        
    Returns:
        int: The converted integer if successful, None if an exception occurs.
    """
    try:
        value = int(input(prompt))
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
        return None
    else:
        return value
    finally:
        print("Execution of int_user_input completed.")

def raise_exception():
    """
    Raises a ValueError intentionally to demonstrate exception handling.
    
    Raises:
        ValueError: Always raised to demonstrate exception handling.
    """
    try:
        raise ValueError("This is an intentional error for demonstration.")
    except ValueError as e:
        print(f"Caught an exception: {e}")
    finally:
        print("Execution of raise_exception completed.")

if __name__ == "__main__":
    # Example of dividing numbers
    num1 = 10
    num2 = 0
    result = divide_numbers(num1, num2)
    if result is not None:
        print(f"Result of division: {result}")

    # Example of user input conversion
    user_input = int_user_input("Please enter an integer: ")
    if user_input is not None:
        print(f"You entered: {user_input}")
        
    # Example of raising an exception intentionally
    raise_exception()