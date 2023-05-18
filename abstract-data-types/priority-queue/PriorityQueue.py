"""
https://realpython.com/python-heapq-module/
"""
import heapq


class PriorityQueue:
    """Priority Queue

    A priority queue is a data structure that stores elements in a queue.
    Each element has a priority associated with it and elements are dequeued
    based on their priority.

    Attributes:
        elements: A list of tuples representing the elements in the priority queue.
                  Each tuple contains the priority and the item.
    """

    def __init__(self) -> None:
        """Initializes a list for the PriorityQueue class."""
        self.elements = []

    def is_empty(self) -> bool:
        """Returns True if the priority queue is empty, False otherwise."""
        return not self.elements

    def put(self, item, priority) -> None:
        """Adds an item to the priority queue.

        Args:
            item: An item to be added to the priority queue.
            priority: An integer representing the priority of the item.

        Time Complexity:
            O(log(n))
        """
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """Removes and returns the item with the highest priority.

        Time Complexity:
            O(log(n))

        Returns:
            The item with the highest priority.

        Note:
            Each element in the priority queue is a tuple containing the priority and the item.
        """
        return heapq.heappop(self.elements)[1]

    def __str__(self) -> str:
        return str(self.elements)
