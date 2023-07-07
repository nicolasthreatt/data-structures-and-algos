"""
Daily Coding Problem: #5 (Medium) - Jane Street
Date: 07/07/2023

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given the implementation of cons below, implement car and cdr.
"""

# Helper function to construct a pair
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# Algorith Used: Functional Programming
# Time Complexity: O(1)
# Space Complexity: O(1)
def car(pair):
    def get_first(a, b):
        return a

    return pair(get_first)


# Algorith Used: Functional Programming
# Time Complexity: O(1)
# Space Complexity: O(1)
def cdr(pair):
    def get_last(a, b):
        return b

    return pair(get_last)


if __name__ == '__main__':
    a, b = 3, 4
    pair = cons(a, b)
    assert car(cons(a, b)) == a
    assert cdr(cons(a, b)) == b
