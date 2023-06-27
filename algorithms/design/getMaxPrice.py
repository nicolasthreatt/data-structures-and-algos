"""
DoorDash Interview Question

You're a dasher, and you want to try planning out your schedule.
You can view a list of deliveries along with their associated start time, end time, and dollar amount for completing the order.
Assuming dashers can only deliver one order at a time, determine the maximum amount of money you can make from the given deliveries.

The inputs are as follows:
    - int start_time: when you plan to start your schedule
    - int end_time: when you plan to end your schedule
    - int d_starts[n]: the start times of each delivery[i]
    - int d_ends[n]: the end times of each delivery[i]
    - int d_pays[n]: the pay for each delivery[i]
The output should be an integer representing the maximum amount of money you can make by forming a schedule with the given deliveries.

Example 1:
    start_time = 0
    end_time = 10
    d_starts = [2, 3, 5, 7]
    d_ends   = [6, 5, 10, 11]
    d_pays   = [5, 2, 4, 1]
    Output: 6
    Explanation: You can take the 2nd and 3rd deliveries for a total of $6.
"""

from typing import List
import heapq

class Dasher:
    def __init__(self, start, end, pay):
        self.start = start
        self.end = end
        self.pay = pay


# Algorithm: Heap, Greedy, Interval Scheduling
# Time Complexity: O(nlog(n)), where n is the number of deliveries
# Space Complexity: O(n)
def get_max_price(start_time: int, end_time: int, d_starts: List[int], d_ends: List[int], d_pays: List[int]) -> int:
    # Create a list of dashers
    dashers = [Dasher(start, end, pay) for start, end, pay in zip(d_starts, d_ends, d_pays)]

    # Sort the dashers by end time
    dashers.sort(key=lambda x: x.start)

    # Create a variable to store the max price
    max_price = 0

    # Create a min heap to store the dashers
    heap = []

    # Iterate through the dashers
    for dasher in dashers: # O(n)
        # If the dasher's start time is greater than the end time, pop the heap
        # This signifies that the dasher is no longer available
        while heap and heap[0][0] <= dasher.start:
            max_price = max(max_price, heapq.heappop(heap)[-1])
        
        # Push the dasher onto the heap, with the end time as the key
        heapq.heappush(heap, (dasher.end, dasher.pay + max_price))

    while heap:
        max_price = max(max_price, heapq.heappop(heap)[-1])

    # Return the max price
    return max_price


if __name__ == "__main__":
    start_time = 0
    end_time = 10
    d_starts = [2, 3, 5, 7]
    d_ends   = [6, 5, 10, 11]
    d_pays   = [5, 2, 4, 1]
    assert get_max_price(start_time, end_time, d_starts, d_ends, d_pays) == 6
