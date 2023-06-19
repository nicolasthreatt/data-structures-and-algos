"""
Doordash interview question

A driver's route can be represented as follows:
    Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.
        * A delivery cannot happen for an order before pickup.
        * The same order cannot be delivered or picked up twice
        * The car must be empty at the end of the drive.

Examples below:
    [P1, P2, D1, D2]==>valid
    [P1, D1, P2, D2]==>valid
    [P1, D2, D1, P2]==>invalid
    [P1, D2]==>invalid
    [P1, P2]==>invalid
    [P1, D1, D1]==>invalid
    []==>valid
    [P1, P1, D1]==>invalid
    [P1, P1, D1, D1]==>invalid
    [P1, D1, P1]==>invalid
    [P1, D1, P1, D1]==>invalid

Follow up:
    Find the longest valid subarray.
    O(n^2) is obvious.
    O(n) involves careful consideration of all the cases of invalidity.
"""

from collections import deque


# Algorithm: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_valid_route(route):
    """Find the longest valid subarray of the given route.

    Args:
        route (List[str]): route

    Returns:
        List[str]: longest valid subarray
    """
    # If the route is empty, return an empty list
    if not route:
        return True

    # Pickups
    pickups, deliveries = set(), set()
    last_pickup = float("-inf")

    for order in route:
        order_type, order_id = order[0], int(order[1:])

        if order_type == "P":
            if order_id in pickups or order_id in deliveries or order_id < last_pickup:
                return False
            pickups.add(order_id)
            last_pickup = order_id
        else:
            if order_id in deliveries or order_id not in pickups:
                return False
            deliveries.add(order_id)
        
    return len(pickups) == len(deliveries)


def longest_valid_route(route):
    """Find the longest valid subarray of the given route.

    Args:
        route (List[str]): route

    Returns:
        List[str]: longest valid subarray
    """
    # If the route is empty, return 0
    if not route:
        return 0

    # Create a hash set to store the order ids
    pickups, deliveries = set(), set()
    
    # Initialize a queue to store the valid subarray
    queue = deque()

    # Initialize a variable to store the length of the current and longest valid subarray
    longest_valid_subarray = 0
    current_valid_subarray = 0

    # Iterate through the route
    for order in route:
        order_type, order_id = order[0], int(order[1:])

        # If the order is a pickup, add it to the queue
        if order_type == "P":
            if order_id in pickups:
                current_valid_subarray = 0
                queue.clear()
            else:
                pickups.add(order_id)
                queue.append(order_id)
                current_valid_subarray += 1
        
        # If the order is a delivery, check if the queue is empty
        else:
            # If the queue is empty, the route is invalid
            if not queue:
                current_valid_subarray = 0
            else:
                # If the queue is not empty, check if the order_id is the same as the first element in the queue
                if order_id == queue[0]:
                    queue.popleft()
                    deliveries.add(order_id)
                    current_valid_subarray += 1
                # If the order_id is not the same as the first element in the queue, the route is invalid
                else:
                    current_valid_subarray = 0
                    queue.clear()
        
        # Update the longest valid subarray
        longest_valid_subarray = max(longest_valid_subarray, current_valid_subarray)

    return longest_valid_subarray



if __name__ == "__main__":
    routes = [
        ["P1", "P2", "D1", "D2"], # valid
        ["P1", "D1", "P2", "D2"], # valid
        ["P1", "D2", "D1", "P2"], # invalid
        ["P1", "D2"], # invalid
        ["P1", "P2"], # invalid
        ["P1", "D1", "D1"], # invalid
        [], # valid
        ["P1", "P1", "D1"], # invalid
        ["P1", "P1", "D1", "D1"], # invalid
        ["P1", "D1", "P1"], # invalid
        ["P1", "D1", "P1", "D1"], # invalid
    ]

    for route in routes:
        print("Route: {}".format(route))
        print("Valid Route: {}".format(is_valid_route(route)))
        print("Longest Valid Subarray: {}".format(longest_valid_route(route)))
        print()
