"""
Factorial
"""

def factorial(n: int) -> int:
    # Base Case
    if n <= 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)   # State moving towards base case
    

print(factorial(4))
print(factorial(6))
print(factorial(1))
print(factorial(0))
print(factorial(-3))
