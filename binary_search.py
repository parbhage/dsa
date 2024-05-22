#Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If the element is not present in the array
    return -1

# Example usage:
arr = [11, 12, 22, 25, 34, 64, 90]
target = 22
print("Original array:", arr)
print("Searching for element", target)

index = binary_search(arr, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the array")