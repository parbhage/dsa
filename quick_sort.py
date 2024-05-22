
#Quick Sort
def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as the pivot
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot with element at i+1
    return i + 1  # Return the partitioning index


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # pi is partitioning index
        quick_sort(arr, low, pi - 1)  # Sort elements before partition
        quick_sort(arr, pi + 1, high)  # Sort elements after partition


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)