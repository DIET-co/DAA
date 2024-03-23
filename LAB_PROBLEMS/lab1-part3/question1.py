#Given an unsorted integer array, find a pair with the given sum in it

def find_pair_with_sum(arr, target_sum):
    # Create an empty dictionary to store complements
    complement_dict = {}

    # Iterate through the array
    for num in arr:
        # Check if the complement of the current number exists in the dictionary
        complement = target_sum - num
        if complement in complement_dict:
            # If complement exists, return the pair
            return (complement, num)
        else:
            # Otherwise, store the current number as a potential complement
            complement_dict[num] = True

    # If no pair is found, return None
    return None


arr = [1, 4, 5, 7, 3, 9]
target_sum = 12
pair = find_pair_with_sum(arr, target_sum)
if pair:
    print("Pair with sum", target_sum, ":", pair)
else:
    print("No pair with sum", target_sum, "found in the array.")
