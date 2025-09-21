"""
Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n.
You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
    * -1: Your guess is higher than the number I picked (i.e. num > pick).
    * 1: Your guess is lower than the number I picked (i.e. num < pick).
    * 0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
    Input: n = 10, pick = 6
    Output: 6

Example 2:
    Input: n = 1, pick = 1
    Output: 1

Example 3:
    Input: n = 2, pick = 1
    Output: 1

Constraints:
    * 1 <= n <= 2^31 - 1
    * 1 <= pick <= n
"""

pick = None


def guess(num: int) -> int:
    """
    Simulated API function that compares num with the global pick.
    """
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def guessNumber(n: int) -> int:
    l, r = 1, n

    # Binary search for the number picked
    while l <= r:
        m = (l + r) // 2
        guessed = guess(m)

        if guessed == -1:   # Guess is HIGHER than the number, so decrease
            r = m - 1
        elif guessed == 1:  # Guess is LOWER than the number, so increase
            l = m + 1
        else:
            return m


if __name__ == "__main__":
    pick = 6
    assert guessNumber(10) == 6

    pick = 1
    assert guessNumber(1) == 1

    pick = 1
    assert guessNumber(2) == 1

    pick = 2
    assert guessNumber(2) == 2

    pick = 999
    assert guessNumber(1000) == 999
