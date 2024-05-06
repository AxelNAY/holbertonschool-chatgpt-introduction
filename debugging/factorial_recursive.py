#!/usr/bin/python3
import sys

"""
    Calculates the factorial of a given number recursively.

    Function Description:
    ----------------------
    This function calculates the factorial of a given number using recursion.
    The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.

    Parameters:
    -----------
    n : int
        The number for which the factorial needs to be calculated.

    Returns:
    --------
    int
        The factorial of the given number n.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
