"""
Write a recursive algorithm to perform multiplication of
positive integers using repeated addition
"""


def multiply(multipier: int, mutliplicand: int):
    # Base Case
    if multipier == 1:
        return mutliplicand

    # Recursive Case
    return mutliplicand + multiply(multipier - 1, mutliplicand) # Moving towards base case
