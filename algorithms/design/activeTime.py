"""
DoorDash Interview Question

Given a sequence of timestamps & actions of a dasher's activity within a day,
we would like to know the active time of the dasher.
Idle time is defined as the dasher has NO delivery at hand.
(That means all items have been dropped off at this moment and the dasher is just waiting for another pickup)
Active time equals total time minus idle time.

Dropoff can only happen after pickup.
12:00am means midnight and 12:00pm means noon.
All the time is within a day.

Example:
    Timestamp(12h) | Action
    8:30am | pickup
    9:10am | dropoff
    10:20am| pickup
    12:15pm| pickup
    12:45pm| dropoff
    2:25pm | dropoff

    total time = 2:25pm-8:30am = 355 mins;
    idle time = 10:20am-9:10am = 70 mins;
    active time = total time-idle time = 355-70 = 285 mins
"""

from collections import deque


# Algorithm: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def active_time(timestamps: list, actions: list) -> int:
    # Initialize variables
    pickups = 0
    total_time = 0
    queue = deque()

    # Iterate through each timestamp and action
    for i in range(len(timestamps)):
        
        # Convert timestamp to minutes
        timestamp_in_minutes = convert_timestamp(timestamps[i])

        # If action is pickup:
        #   - Add timestamp to queue
        #   - Record last pickup
        # If action is dropoff
        #   - Remove timestamp from queue and record the earlist last pickup
        #   - Calculate total time if queue is not empty.
        if actions[i] == "pickup":
            queue.append(timestamp_in_minutes)
            last_pickup = timestamp_in_minutes
        else:
            # Get the timestamp of the earliest pickup
            last_pickup = min(last_pickup, queue.pop())

            # If queue is not empty, calculate total time.
            # An empty queue means that the dasher has no delivery at hand.
            if not queue:
                total_time += timestamp_in_minutes - last_pickup

    # Calculate active time by subtracting idle time from total time
    return total_time


def convert_timestamp(timestamp):
    """Convert timestamp to minutes"""

    # Split timestamp into hour and minute components
    hour, minute = map(int, timestamp[:-2].split(":"))
    
    # Convert hour to 24-hour format if necessary
    if timestamp[-2:] == "pm" and hour != 12:
        hour += 12
    elif timestamp[-2:] == "am" and hour == 12:
        hour = 0
    
    # Convert timestamp to minutes
    timestamp_in_minutes = hour * 60 + minute
    
    # Return converted timestamp
    return timestamp_in_minutes


if __name__ == "__main__":
    timestamps = ["8:30am", "9:10am", "10:20am", "12:15pm", "12:45pm", "2:25pm"]
    actions = ["pickup", "dropoff", "pickup", "pickup", "dropoff", "dropoff"]
    assert active_time(timestamps, actions) == 285
