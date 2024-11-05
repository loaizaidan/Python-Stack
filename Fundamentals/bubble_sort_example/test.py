def bubble_sort(arr):
    n = len(arr)  # Get the length of the array

    # Outer loop for each element in the array
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # If the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example arrays to sort
array1 = [64, 34, 25, 12, 22, 11, 90, 45, 78, 56]
array2 = [5, 1, 4, 2, 8, 0, 3, 6, 9, 7]
array3 = [12, 11, 13, 5, 6, 7, 14, 10, 9, 8]

# Sorting and printing each array
print("Original Array 1:", array1)
bubble_sort(array1)
print("Sorted Array 1:  ", array1)

print("Original Array 2:", array2)
bubble_sort(array2)
print("Sorted Array 2:  ", array2)

print("Original Array 3:", array3)
bubble_sort(array3)
print("Sorted Array 3:  ", array3)
