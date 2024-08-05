def sequential_search(elements, target):
    # Iterate through the list
    for index, element in enumerate(elements):
        # Check if the current element matches the target
        if element == target:
            return index  # Return the index if found
    return -1  # Return -1 if the target is not found

# List of elements
elements = [1, 3, 5, 8, 10, 23, 35]

# Target value to search for
target = 10

# Perform sequential search
result = sequential_search(elements, target)

# Display the result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
