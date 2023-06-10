# Algorithm Used: Greedy Algorithm
# Time Complexity: O(n log n), where n is the number of items
# Space Complexity: O(1)
def knapsack(items, max_weight):
    """
    Solve the knapsack problem using a greedy algorithm.

    The knapsack problem is a classic optimization problem.
    It is encountered in various real-world scenarios such as resource allocation, portfolio optimization,
    and resource-constrained scheduling, where the goal is to make the best use of limited resources.
    Given a set of items, each with a weight and a value, the goal is to determine the most valuable
    combination of items to include in a knapsack (a container) with a limited weight capacity.
    
    Args:
        items (list): List of tuples representing items, where each tuple contains the item's weight and value.
        max_weight (int): Maximum weight that the knapsack can hold.
    
    Returns:
        int: Maximum total value of items that can be included in the knapsack.
    
    Example:
        >>> items = [(2, 10), (3, 12), (5, 20), (7, 25)]
        >>> max_weight = 10
        >>> knapsack(items, max_weight)
        37
    """
    # Sort items by value-to-weight ratio in descending order.
    # This step helps prioritize items with higher value-to-weight ratios,
    # maximizing the total value that can be obtained.
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    # Initialize total value and total weight
    # These variables keep track of the current state of the knapsack
    total_value = 0
    total_weight = 0

    # Iterate over each item
    for item in items:
        # Check if adding the current item exceeds the maximum weight
        if total_weight + item[0] <= max_weight:
            # Add the item to the knapsack
            total_value += item[1]
            total_weight += item[0]

    return total_value
