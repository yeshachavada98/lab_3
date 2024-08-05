def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        
        # Check the rest of the array to find the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# List of elements
elements = [22, 13, 4, 8, 17, 20, 53, 4]

# Perform selection sort
selection_sort(elements)

# Display the sorted list
print("Sorted List:", elements)
