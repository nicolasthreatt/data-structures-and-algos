"""
Exponentiation
    - Raise one number to a power of another
        + Positive numbers only
"""


def exp(b: int, x: int) -> int:
    # Base Case
    if x == 1:
        return b
    
    # Recursive Case
    return b * exp(b, x - 1) # Moving towards base case
