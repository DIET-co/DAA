#Given a set of activities, along with the starting and finishing time of each activity, find the
#maximum number of activities performed by a single person assuming that a person can
#only work on a single activity at a time.


def max_activities(activities):
    # Sort activities based on finish times
    sorted_activities = sorted(activities, key=lambda x: x[1])

    # Initialize variables
    count = 1
    prev_finish_time = sorted_activities[0][1]

    # Iterate through activities
    for activity in sorted_activities[1:]:
        start_time, finish_time = activity
        # If the current activity can be performed
        if start_time >= prev_finish_time:
            count += 1
            prev_finish_time = finish_time

    return count

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
max_activities_count = max_activities(activities)
print("Maximum number of activities performed by a single person:", max_activities_count)
