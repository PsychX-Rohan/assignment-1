def insertion_sort(arr):
    """
    Sorts a list in ascending order using the insertion sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    # Traverse from index 1 to end of list
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to insert
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key after the element just smaller than it
        arr[j + 1] = key

    return arr


# Example usage
numbers = [12, 11, 13, 5, 6]
print("Original list:", numbers)
sorted_list = insertion_sort(numbers)
print("Sorted list:", sorted_list)
