"""
DoorDash Interview Question

Given cities, x and y coordinates, and a list of queries, return the closest city to city in the query.

If the x, y coordinate of the city matches, then return None.
Else return the closest city to to the city in the query.

If two cities are equidistant, then compare the length of the name of the city.
If the lengths are equal, then return the city which occures first lexicographically.

Example 1:
    Input:
        cities = ["aa", "bbb", "ccc"]
        x = [1, 1, 2]
        y = [1, 3, 4]
        query = ["aa"]
    Output: ["bbb"]
    Explanation: The closest city to "aa" is "bbb".

Example 2:
    Input:
        cities = ["aa", "bbb", "ccc"]
        x = [1, 1, 2]
        y = [1, 3, 4]
        query = ["bbb"]
    Output: ["ccc"]
    Explanation: The closest city to "bbb" is "aa".
"""

from typing import List
import math


# Algorithm: Brute Force, Linear Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def closest_city(cities: List[str], x: List[int], y: List[int], query: List[str]) -> List[str]:
    # Create a string to store the closest city.
    # Initialize the string to an empty string.
    closest_city = ""


    # If the length of cities, x, y, or query is not equal to each other or
    # if any of the lists are empty, then return the closest city, which is an empty string.
    if ((len(cities) != len(x) != len(y)) or
        not cities or not x or not y or not query
    ):
        return closest_city

    # Iterate through the cities list.
    # If the city is the same as the query, then store the x and y coordinates.
    # These x and y coordinates will be used to calculate the distance between the query and the city.
    for i in range(len(cities)):
        if cities[i] == query[0]:
            query_x, query_y = x[i], y[i]

    # Initialize the minimum distance to infinity.
    # This will be used to compare the distance between the query and the city.
    # Set it to infinity so that the first distance will always be less than infinity.
    min_distance = math.inf

    # Iterate through the cities list.
    for i in range(len(cities)):
        # If the city is not the same as the query, then calculate the distance between query and city.
        #   - If the distance is less than the minimum distance, then update minimum distance and closest city.
        #   - If the distance is equal to the minimum distance, then compare the length of the city name.
        if cities[i] != query[0]:
            current_distance = math.sqrt((query_x - x[i]) ** 2 + (query_y - y[i]) ** 2)
            if current_distance < min_distance:
                min_distance = current_distance
                closest_city = cities[i]
            elif current_distance == min_distance:
                if len(cities[i]) < len(closest_city):
                    closest_city = cities[i]
                elif len(cities[i]) == len(closest_city):
                    closest_city = min(cities[i], closest_city)

    # Return the closest city.
    return closest_city


if __name__ == "__main__":
    cities = ["aa", "bbb", "ccc"]
    x = [1, 1, 2]
    y = [1, 3, 4]
    query = ["aa"]
    assert closest_city(cities, x, y, query) == "bbb"

    cities = ["aa", "bbb", "ccc"]
    x = [1, 1, 2]
    y = [1, 3, 4]
    query = ["bbb"]
    assert closest_city(cities, x, y, query) == "ccc"