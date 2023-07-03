"""
Daily Coding Problem: #754 (Medium) - Square
Date: 06/30/2023

In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game.

You and an opponent take turns choosing either the first or last coin from the row,
removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty,
if you move first, assuming your opponent plays optimally.
"""


# Algorith Used: Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def max_money(coins):
    """
    Returns the maximum amount of money you can win with certainty,
    if you move first, assuming your opponent plays optimally.
    """

    # Base cases
    if not coins:
        return 0
    if len(coins) == 1:
        return coins[0]
    if len(coins) == 2:
        return max(coins)    

    # Recursive cases
    # If you take the first coin, your opponent can take either the first or last coin
    # If you take the last coin, your opponent can take either the first or last coin
    first_coin_move = coins[0] + min(max_money(coins[2:]), max_money(coins[1:-1]))
    last_coin_move = coins[-1] + min(max_money(coins[1:-1]), max_money(coins[:-2]))

    # Return the maximum of the two possible moves
    return max(first_coin_move, last_coin_move)


if __name__ == "__main__":
    assert max_money([]) == 0
    assert max_money([1]) == 1
    assert max_money([1, 2]) == 2 
    assert max_money([1, 2, 3]) == 4 # 3 + 1
    assert max_money([1, 2, 3, 4]) == 6 # 4 + 2
    assert max_money([1, 2, 3, 4, 5]) == 9 # 5 + 3 + 1
    assert max_money([1, 2, 3, 4, 5, 6]) == 12 # 6 + 4 + 2
    assert max_money([6, 2, 3, 4, 5, 1]) == 14 # 6 + 3 + 5
    assert max_money([1, 9, 5, 3, 8, 4, 2, 7, 6, 3]) == 26 # 3 + 7 + 4 + 3 + 9
