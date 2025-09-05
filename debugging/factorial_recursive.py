#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
        n (int): The number to calculate the factorial of.
                 Must be a non-negative integer.

    Returns:
        int: The factorial value of n.
             If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument, convert it to int,
# and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
