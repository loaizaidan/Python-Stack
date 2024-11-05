#  __         ______     ______     __   
# /\ \       /\  __ \   /\  __ \   /\ \  
# \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \ 
#  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\
#   \/_____/   \/_____/   \/_/\/_/   \/_/

def selection_sort(arr):
    for i in range(len(arr)):#iterate through all array elements
        
        min_index = i#assume the min is the first element of the unsorted list
        
        for j in range(i + 1, len(arr)):#find the min element in the remaining unsorted list
            if arr[j] < arr[min_index]:
                min_index = j
           
        arr[i], arr[min_index] = arr[min_index], arr[i]#swao the found min element with the first element of the unsorted list
    
    return arr

#ex
sorted_list = selection_sort([64, 25, 12, 22, 11])
print(sorted_list)