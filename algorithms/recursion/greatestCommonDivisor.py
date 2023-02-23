"""
Greatest Common Divisor
    - Euclid's Algorithm
        > GCD(a, b) = GCD(b, a - b)
            * GCD(12, 8) = GCD(8, 12 - 8) = GCD(8, 4)
        > Since division can be seen as repeated subtraction, the more
          efficient version is:
            * GCD(a, b) = GCD(b, a % b)
            * % is the modulo operator (remainder on division)
"""


def gcd(a: int, b: int) -> int:
    # Base Case
    if b == 0:
        return a
    
    # Recursive Case
    return gcd(b, a % b)  # Move towards base case
