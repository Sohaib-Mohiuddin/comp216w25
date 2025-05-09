# Functions Example 
x = 200

def hello(prof='Sohaib', age=0):
    # If statement to check if the age is less than 20
    if (age < 20):
        return f'You are young { prof }'
    # If statement to check if the age is less than 40
    elif (age > 40):
        return f'Damn you are old { prof }'
    else:
        return f'You are dead { prof }'

print(hello('Bob', 500))


# Recursive Function Example
def fact(x: int) -> int:
    if (x == 1):
        return 1
    else:
        return x * fact(x - 1)

print(fact(20))