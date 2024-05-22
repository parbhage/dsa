# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so we can reduce the inner loop iterations
        for j in range(0, n-i-1):
            # Compare adjacent elements and swap if necessary
            if arr[j] > arr[j+1]:
                # Swap elements without using inbuilt functions
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)
