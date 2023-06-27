"""
DoorDash Interview Question

Given an integer n representing the number of orders, return the number of possible fullfilment orders.

A fullfilment order is a sequence of "P" and "D" representing pickup and delivery of an order.

A valid fullfilment order is a sequence of "P" and "D" such that:
    1. Each order is picked up before it is delivered
    2. No order is picked up or delivered twice
    3. The car is empty at the end of the drive

Example 1:
    Input: n = 1, orders = ["P1", "D1"]
    Output: 1
    Explanation: There is only one order, so only one fullfilment order.

Example 2:
    Input: n = 2, orders = ["P1", "D1", "P2", "D2"]
    Output: 2
    Explanation: There are two fullfilment orders:
        1. ["P1", "P2", "D1", "D2"]
        2. ["P1", "P2", "D2", "D1"]
        2. ["P1", "D1", "P2", "D2"]
"""

from collections import deque


# Algorithm: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def count_orders(n: int) -> int, list:
    pass