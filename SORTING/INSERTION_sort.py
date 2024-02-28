def insertion_sort(array):
    for slot in range(1, len(array)): 
        value = array[slot]
        test_slot = slot - 1
        while test_slot > -1 and array[test_slot] > value:
            array[test_slot + 1] = array[test_slot]
            test_slot = test_slot - 1
        array[test_slot + 1] = value
    return array

def get_user_input():
    array = input("Enter a list of integers separated by spaces: ").split()
    return [int(num) for num in array]

def main():
    array = get_user_input()
    sorted_array = insertion_sort(array)
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    main()