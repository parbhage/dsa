#Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index if element found
    return -1  # Return -1 if element not found

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
print("Original array:", arr)
print("Searching for element", target)

index = linear_search(arr, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the array")
