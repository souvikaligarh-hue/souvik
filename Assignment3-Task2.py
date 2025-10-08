# Task 2: Using the Math Module for Calculations
# Write a Python program that:
# Asks the user for a number as input.
# Uses the math module to calculate the:
# Square root of the number
# Natural logarithm (log base e) of the number
# Sine of the number (in radians)
# Displays the calculated results.

import math
num = float(input("Enter a number: "))
sqrt_num = math.sqrt(num)
log_num = math.log(num)
sine_num = math.sin(num)
print("Square root of", num, "is:", sqrt_num)
print("Natural logarithm (log base e) of", num, "is:", log_num)
print("Sine of", num, "is:", sine_num)
# End of the code

