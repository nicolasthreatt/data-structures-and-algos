"""
Search algorithms for arrays.

Includes:
    - Linear Search
        + Time Complexity: O(n)
        + Space Complexity: O(1)
    - Binary Search Iterative
        + Time Complexity: O(log(n))
        + Space Complexity: O(1)
    - Binary Search, Recursive
        + Time Complexity: O(log(n))
        + Space Complexity: O(log(n))
"""


# Algorithm Used: Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)
def linear_search(numbers: list, key) -> int:
    """
    Search (Linear) for the key in the numbers.

    Args:
        numbers (list): The numbers to search through.
        key (int): The key to search for.

    Returns:
        int: The index of the key in the numbers, -1 if the key is not found.
    """
    for i, num in enumerate(numbers):
        if num == key:
            return i
    return -1


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def binary_search(numbers: list, key) -> int:
    """
    Search (binary) for the key in the numbers.

    Args:
        numbers (list): The numbers to search through.
        key (int): The key to search for.

    Returns:
        int: The index of the key in the numbers, -1 if the key is not found.
    """
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] < key:
            left = mid + 1
        elif numbers[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1


# Algorithm Used: Binary Search, Recursive
# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
def binary_search_recursive(numbers: list, key, left, right) -> int:
    """
    Search (binary) for the key in the numbers.

    Args:
        numbers (list): The numbers to search through.
        key (int): The key to search for.
        left (int): The left index of the numbers to search through.
        right (int): The right index of the numbers to search through.

    Returns:
        int: The index of the key in the numbers, -1 if the key is not found.
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if numbers[mid] < key:
        return binary_search_recursive(numbers, key, mid + 1, right)
    elif numbers[mid] > key:
        return binary_search_recursive(numbers, key, left, mid - 1)
    else:
        return mid


def binary_search_recursive_wrapper(numbers: list, key) -> int:
    """Wrapper function for binary_search_recursive.

    Args:
        numbers (list): The numbers to search through.
        key (int): The key to search for.

    Returns:
        int: The index of the key in the numbers, -1 if the key is not found.
    """
    return binary_search_recursive(numbers, key, 0, len(numbers) - 1)
