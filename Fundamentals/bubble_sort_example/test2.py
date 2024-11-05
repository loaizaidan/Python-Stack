def bubble_sort(arr):
    index_length=len(arr)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,index_length):
            if arr[i]>arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1],arr[i]
    return arr

array1=[5,1,2,4,6,88,9,98,65,234,231]
array2=[1,2,3,4,5,7,6,8,9]

print("Unsorted array 1:")
print(array1)
print("Sorted array 1:")
print(bubble_sort(array1))
print("Unsorted array 2: ")
print(array2)
print("Sorted array 2:")
print(bubble_sort(array2))