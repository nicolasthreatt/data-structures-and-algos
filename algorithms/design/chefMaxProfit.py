"""
DoorDash Interview Question

You are given skills, difficulty, profit for dashers. Return the most Profit that the kitchen can be produce.

Example:
    skills = [2, 3, 4]
    difficult = [1, 2, 3, 4, 5, 6]
    profits = [1, 2, 3, 7, 9, 8]
    Output: 2 + 3 + 7
    Explanation: For skill 2, you can create a dish (1) with profit (1) or dish (2) with profit (2) Choose the max profit
"""


# Algorithm Used: Hash Table
# Time Complexity: O(n), where n is the number of skills
# Space Complexity: O(n)
def max_profit(skills, difficulty, profits):
    counts = {skill: 0 for skill in skills}
    
    for i in range(len(profits)):
        if difficulty[i] in skills:
            counts[difficulty[i]] = max(counts[difficulty[i]], profits[i])
    
    return sum(list(counts.values()))


if __name__ == "__main__":
    skills = [2, 3, 4]
    difficulty = [1, 2, 3, 4, 5, 6]
    profits = [1, 2, 3, 7, 9, 8]
    assert max_profit(skills, difficulty, profits) == 12