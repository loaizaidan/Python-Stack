def insertion_sort(arr):
    # Traverse from the second element to the end of the list
    for i in range(1, len(arr)):
        current = arr[i]  # The current element to be compared
        j = i - 1  # Start comparing with the previous element
        
        # Shift elements of arr[0..i-1], that are greater than current, to one position ahead
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move to the next element on the left
        
        # Insert the current element in the correct position
        arr[j + 1] = current

    return arr


    # Example list
    test_list = [12, 11, 13, 5, 6]
    print("Original list:", test_list)
    sorted_list = insertion_sort(test_list)
    print("Sorted list:", sorted_list)  # Should print [5, 6, 11, 12, 13]
