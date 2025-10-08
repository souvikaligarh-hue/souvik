# Factorial Calculator
#  Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# Returns the calculated factorial.
#  Calls the function with a sample number and prints the output.

num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)
# End of the code




