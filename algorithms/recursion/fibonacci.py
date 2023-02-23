"""
Fibonacci
    - https://en.wikipedia.org/wiki/Fibonacci_number
    - In mathematics, the Fibonacci numbers, commonly denoted F(n), form a sequence,
      the Fibonacci sequence, in which EACH NUMBER IS THE SUM OF THE TWO PRECEDING ONES
"""

from functools import lru_cache # Least-Recently-Used


@lru_cache
def fibonacci(n: int) -> int:
    # Base Case
    if n <= 1:
        return n

    # Recursive Case
    return fibonacci(n-1) + fibonacci(n-2)

