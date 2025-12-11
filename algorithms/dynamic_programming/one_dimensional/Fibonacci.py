"""
Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
      
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1.

That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
    * 0 <= n <= 30
"""


class Fibonacci:
    def __init__(self):
        self.MEMO = {}

    # Algorithm Used: Recursion
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def fibonacciI(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fibonacciI(n - 1) + self.fibonacciI(n - 2)


    # Algorithm Used: Recursion, Memoization
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def fibonacciII(self, n: int) -> int:
        if n in self.MEMO:
            return self.MEMO[n]

        fib = n if n <= 1 else self.fibonacciII(n - 1) + self.fibonacciII(n - 2)

        self.MEMO[n] = fib
        return fib


    # Algorithm Used: Dynamic Programming (1-D), Bottom-Up, Memoization
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def fibonacciIII(self, n: int) -> int:
        if n <= 1:
            return n

        fib = [0, 1]  # Base cases (memo)

        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])  # Memoization

        return fib[n]


    # Algorithm Used: Dynamic Programming (1-D), Bottom-Up
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def fibonacciIV(self, n: int) -> int:
        if n <= 1:
            return n

        prev, curr = 0 , 1
        for _ in range(2, n + 1):
            # prev, curr = curr, prev + curr
            tmp = prev
            prev = curr
            curr = tmp + curr

        return curr


if __name__ == "__main__":
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55),
        (15, 610),
        (20, 6765),
        (30, 832040),
    ]

    Solution = Fibonacci()
    for func in [
        Solution.fibonacciI,
        Solution.fibonacciII,
        Solution.fibonacciIII,
        Solution.fibonacciIV
    ]:
        for n, expected in test_cases:
            result = func(n)
            assert result == expected
