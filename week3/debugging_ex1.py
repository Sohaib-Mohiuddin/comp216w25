"""
Iteration loop for debugging:
"""

sum = 0

for i in range(10):
    if i == 5:
        sum += i
        print("Reached the halfway point!")
    elif i == 9:
        sum += i
        print("Final iteration reached!")
    else:
        print("Continuing to next iteration...")