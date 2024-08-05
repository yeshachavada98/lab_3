def insertion_sort(arr):
    # Traverse from the second element to the end of the list
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be placed in the sorted portion
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

# List of elements
elements = [1, 4, 2, 8, 23]

# Perform insertion sort
insertion_sort(elements)

# Display the sorted list
print("Sorted List:", elements)
