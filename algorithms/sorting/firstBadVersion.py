"""
First Bad Version
https://leetcode.com/problems/first-bad-version

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad.

Implement a function to find the first bad version.

You should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
        * call isBadVersion(3) -> false
        * call isBadVersion(5) -> true
        * call isBadVersion(4) -> true
        * Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1

Constraints:
    * 1 <= bad <= n <= 231 - 1
"""

bad = None


def isBadVersion(version: int) -> bool:
    """
    Simulated API that returns True if the given version is bad.
    """
    return version >= bad


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def firstBadVersion(n: int) -> int:
    l, r = 1, n

    # Binary search for the first bad version
    while l <= r:
        m = (l + r) // 2
        if not isBadVersion(m):  # Keep pushing until bad version is found
            l = m + 1
        else:
            r = m - 1
    return l


if __name__ == "__main__":
    bad = 4
    assert firstBadVersion(5) == 4

    bad = 1
    assert firstBadVersion(1) == 1

    bad = 1
    assert firstBadVersion(2) == 1

    bad = 2
    assert firstBadVersion(2) == 2

    bad = 37
    assert firstBadVersion(100) == 37
