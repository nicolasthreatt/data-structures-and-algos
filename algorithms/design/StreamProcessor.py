"""
Doordash Interview Question

Given a streaming data of the form (timestamp, value), find the maximum value in the stream in the last X seconds.

Assume time is monotonically increasing.
Assume time is in the order of seconds.
max_value() function finds the max in the last X seconds.

StreamProcessor(5) // last 5 seconds
set_value(0, 5)
set_value(1, 6)
set_value(2, 4)
max_value(3) = 6 -> always the current time

class StreamProcessor:
    def init(self, x):
        self.x = x

    def set_value(self, t, v):
        pass

    def max_value(self, cur_t):
        pass
"""

from collections import deque


class StreamProcessor:
    def __init__(self, x):
        self.x = x
        self.queue = deque() # FIFO
    
    def remove_old(self, cur_t):
        """Remove all elements that are older than cur_t - x.

        Iterate through the queue and remove all elements that are older than cur_t - x,
        which the current time minus the time window to get the time window of the last x seconds.

        Args:
            cur_t (int): current timestamp

        Time Complexity:
            O(n) where n is the number of elements in the queue

        Space Complexity:
            O(n) where n is the number of elements in the queue
        """
        while self.queue and self.queue[0][0] <= cur_t - self.x:
            self.queue.popleft()
    
    def set_value(self, t, v):
        """Set value at time t to v.

        Remove outdated timestamps, then append the new element to the queue.
        
        Args:
            t (int): timestamp
            v (int): value

        Time Complexity:
            O(n) where n is the number of elements in the queue

        Space Complexity:
            O(n) where n is the number of elements in the queue
        """
        self.remove_old(t)
        self.queue.append((t, v))
    
    def max_value(self, cur_t):
        """Get the max value in the last x seconds.

        Remove outdated timestamps, then append the new element to the queue.
        Then return the max value in the queue.

        Args:
            cur_t (int): current timestamp
        
        Returns:
            int: max value in the last x seconds

        Time Complexity:
            O(n) where n is the number of elements in the queue
        
        Space Complexity:
            O(n) where n is the number of elements in the queue
        """
        self.remove_old(cur_t)
        return max(self.queue, key=lambda x: x[1])[1]


if __name__ == "__main__":
    # Test 1
    sp = StreamProcessor(5)
    sp.set_value(0, 5)
    sp.set_value(1, 6)
    sp.set_value(2, 4)
    assert sp.max_value(3) == 6

    # Test 2
    sp = StreamProcessor(5)
    sp.set_value(0, 5)
    sp.set_value(1, 6)
    sp.set_value(2, 4)
    assert sp.max_value(4) == 6

    # Test 3
    sp = StreamProcessor(5)
    sp.set_value(0, 5)
    sp.set_value(1, 6)
    sp.set_value(2, 4)
    assert sp.max_value(5) == 6
