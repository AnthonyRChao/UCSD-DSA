# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_stop = 0
    num_stops = len(stops) # total number of stops/stations

    # Add start and end points to stops list to prevent IndexError: list index out of range 
    stops.insert(0, 0)
    stops.append(distance)

    # Loop until current_stop is at most num_stops 
    while current_stop <= num_stops:
        last_stop = current_stop

        # Increment current_stop until distance from last stop is greater than tank
        while (current_stop <= num_stops) and ((stops[current_stop + 1] - stops[last_stop]) <= tank):
            current_stop = current_stop + 1
        # If after inner while loop, current_stop is equal to last_stop, then
        # the next stop is farther than our tank can take us, return impossible
        if current_stop == last_stop:
            return -1
        # Otherwise, if current_stop is at most num_stops, increment num_refills
        if current_stop <= num_stops:
            num_refills = num_refills + 1
    # Exit when current_stop becomes > than num_stops
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

