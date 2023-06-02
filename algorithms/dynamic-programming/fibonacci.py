"""
Fibonacci
    - https://en.wikipedia.org/wiki/Fibonacci_number
    - In mathematics, the Fibonacci numbers, commonly denoted F(n), form a sequence,
      the Fibonacci sequence, in which EACH NUMBER IS THE SUM OF THE TWO PRECEDING ONES
      
Example:
    Input: n = 5
    Output: 5
    Explanation:
        - The first five Fibonacci numbers are: 0, 1, 1, 2, 3, 5.
"""


# Algorithm Used: Dynamic Programming (1-D), Bottom-Up
# Time Complexity: O(n)
# Space Complexity: O(n)
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.

    Args:
        n (int): The nth Fibonacci number to return.

    Returns:
        int: The nth Fibonacci number.
    """
    fib = [0, 1]  # Base cases

    # For each number from 2 to n + 1, compute the nth Fibonacci number.
    # Recall this is done by summing the previous two Fibonacci numbers.
    # NOTE: The range is from 2 to n + 1 because we want to compute the nth Fibonacci number because
    #       the first two numbers are the base cases.
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Memoization

    return fib[n]
