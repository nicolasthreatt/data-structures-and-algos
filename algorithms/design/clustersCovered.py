"""
DoorDash Interview Question

At DoorDash, we need to make sure that drivers are available at popular locations to deliver food.
There are certain location clusters in a city that need drivers,and a driver can only cover certain location clusters.
A location cluster is considered “covered” if the driver can deliver for the entire location cluster.
How many location clusters are covered?

Provided:
    driver_available_locations = {
    {1,1,1,0,0},
    {0,1,1,1,1},
    {0,0,0,0,0],
    {1,0,0,1,0],
    {1,1,0,1,1}
    }
    drivers_needed_at = {
    {1,1,1,0,0},
    {0,0,1,1,1},
    {0,1,0,0,0},
    {1,0,1,1,0},
    {0,1,0,1,0}
    }

Return: Int indicating number of location cluster covered
    3
"""


# Algorithm: Brute Force, Linear Search
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def clusters_covered(driver_available_locations: list[list[int]], drivers_needed_at: list[list[int]]) -> int:
    # Initialize the number of clusters covered to 0.
    clusters_covered = 0

    # Iterate through the driver available locations.
    for i in range(len(driver_available_locations)):

        # If there are more drivers needed at a cluster than there are drivers available, then skip the cluster.
        if len(driver_available_locations[i]) < len(drivers_needed_at[i]):
            continue

        # Initialize the number of drivers needed and available to 0 for each cluster.
        num_drivers_needed, num_drivers_available = 0, 0
    
        # Iterate through the drivers needed at.
        for j in range(len(drivers_needed_at)):
            # Increment the number of drivers needed and available for the cluster.
            num_drivers_needed += drivers_needed_at[i][j]

            # If the driver available location and the drivers needed at are equal, then increment the clusters covered.
            if driver_available_locations[i][j] == drivers_needed_at[i][j] == 1:
                num_drivers_available += driver_available_locations[i][j]
        
        # If the number of drivers needed and available are equal, then the cluster is covered.
        # So increment the number of clusters covered.
        if num_drivers_needed == num_drivers_available:
            clusters_covered += 1

    # Return the number of clusters covered.
    return clusters_covered


if __name__ == "__main__":
    driver_available_locations = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1]
    ]
    drivers_needed_at = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0]
    ]
    assert clusters_covered(driver_available_locations, drivers_needed_at) == 3
