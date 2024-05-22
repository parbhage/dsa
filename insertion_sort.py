
#Insertion Sort:
def insertion_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array starting from the second element
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted at the correct position
        j = i - 1     # Index of the previous element

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

insertion_sort(arr)

print("Sorted array:", arr)
