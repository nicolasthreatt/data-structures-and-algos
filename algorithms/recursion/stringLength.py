"""
String Length
    - Use recursion to find the length of a string
"""


def strLength(string: str) -> int:
    # Base Case (String Does Not Exist)
    if not string:
        return 0

    # Recursive Case
    # Moving towards Base Case
    return strLength(string[1:]) + 1
