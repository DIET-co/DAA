#Given a set of intervals, print all non-overlapping intervals after merging the overlapping
#intervals.

def merge_intervals(intervals):
    # Sort intervals based on start times
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize list to store merged intervals
    merged = []

    for interval in sorted_intervals:
        # If the merged list is empty or if current interval does not overlap with the last interval in merged list
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Merge the intervals
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

# Example usage:
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged_intervals = merge_intervals(intervals)
print("Non-overlapping intervals after merging:", merged_intervals)
