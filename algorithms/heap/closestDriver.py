"""
Closest Driver (DoorDash)

Given a restaurant geolocation (longitude / latitude),
find 3 closest Dashers (drivers) near the restaurant who can be assigned for delivery, ordered by their distance from the restaurant.
In case 2 Dashers are equidistant from the restraunt, use Dasher rating as tie breaker.

Each Dasher has 3 properties:
    * Dasher ID
    * Last known location [x,y]
    * Rating (0 - 100). Higher the better

Assume you have a method GetDashers() which returns a list of all Dashers.

Input
    - Restaurant Location

Output
    - List of 3 nearest Dasher IDs. Example: [11, 14, 17]

Assume GetDashers() returns a List<Dasher> where Dasher is represented by:
    class Dasher {
        long id;
        Location lastLocation
        int rating;
        
        public Dasher(long id, Location lastLocation, int rating) {
            this.id = id;
            this.lastLocation = lastLocation;
            this.rating = rating;
        }
    }

and Location is represented by:
    class Location {
        double longitude;
        double lattitude;
        
        Location(double longitude, double lattitude) {
            this.longitude = longitude;
            this.lattitude = lattitude;
        }
    }
"""

import heapq
import math
import random


class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude


class Dasher:
    def __init__(self, id: int, location: Location, rating: int):
        self.id = id
        self.location = location    
        self.rating = rating

class ClosestDrivers:
    def __init__(self, restaurant_location: Location):
        self.restaurant_location = restaurant_location
        self.dashers = []
        self.k = 3

    def get_distance(self, location1: Location, location2: Location):
        # Calculate the distance between the two locations
        return math.sqrt(
            (location1.longitude - location2.longitude) ** 2 +
            (location1.latitude - location2.latitude) ** 2
        )

    def get_closest_drivers_with_rating(self):
        """Get the closest drivers with rating
        
        Time Complexity: O(klogn), where:
            * k is the number of closest drivers to return
            * n is the number of dashers
        Space Complexity: O(n)

        Returns:
            List[int]: A list of the IDs of the closest drivers with rating
        """
        # Initialize the heap
        heap = []

        # Iterate over the dashers
        for dasher in self.dashers:
            # Calculate the distance between the dasher and the restaurant
            distance = self.get_distance(dasher.location, self.restaurant_location)

            # Push the dasher onto the heap
            heapq.heappush(heap, (distance, dasher.rating, dasher))

        # Initialize the top_k_drivers list
        top_k_drivers = []

        # Iterate over the heap
        for i in range(self.k):
            # Pop the dasher with the smallest distance from the heap
            dasher = heapq.heappop(heap)[-1]

            # Append the dasher's ID to the top_k_drivers list
            top_k_drivers.append(dasher.id)

        # Return the top_k_drivers list
        return top_k_drivers


if __name__ == "__main__":
    # Initialize the dashers list
    dashers = []

    # Iterate over the range of 10
    for i in range(10):
        # Create a dasher object with a random location and rating
        dasher = Dasher(i, Location(random.randint(0, 10), random.randint(0, 10)), random.randint(0, 100))

        # Append the dasher to the dashers list
        dashers.append(dasher)
    
    # Create a random restaurant location
    restaurant_location = Location(random.randint(0, 10), random.randint(0, 10))

    # Create a ClosestDrivers object
    closest_drivers = ClosestDrivers(restaurant_location)

    # Set the dashers attribute of the closest_drivers object
    closest_drivers.dashers = dashers

    # Print the closest drivers with rating
    print(closest_drivers.get_closest_drivers_with_rating())
