# Functions Example 
x = 200
lst = [78, 23, 2, 4, 7, 20, 18]

def hello(prof='Sohaib', age=0):
    # If statement to check if the age is less than 20
    if (age < 20):
        return f'You are young { prof }'
    # If statement to check if the age is less than 40
    elif ((age > 40) and (age < 80)):
        return f'Damn you are old { prof }'
    else:
        return f'You are dead { prof }'

# print(hello('Bob', 30))

# Recursive Function Example
def fact(x: int) -> int:
    if (x == 1):
        return 1
    else:
        return x * fact(x - 1)

# print(fact(20))

def take_list(items: list) -> int:
    """Take a list of numbers and multiply all of them together

    Args:
        items (number): list of numbers
    """
    mult = 1
    
    for item in items:
        mult *= item
    
    return mult

print(f'The list { lst } had al values multiplied with each other and gave the following output: { take_list(lst) }')