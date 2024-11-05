print("Number #1: Biggie-Size!")
def biggie_size(list):    
    for i in range(len(list)):#go through the list and replace positive numbers with "big"
        if list[i] > 0:
            list[i] = "big"
    return list

list = [1,5,4,-4,-21,55,2]
print(biggie_size(list))
print("\n")

print("Number #2: Count Positives")
def count_positives(numbers):
    positive_count = 0
    
    for num in numbers:#iterate through the list and count positive numbers
        if num > 0:#Check if the number is positive
            positive_count += 1#Increment the positive count

    #replace the last value with the count of positive numbers
    if numbers:#check if the list is not empty
        numbers[-1] = positive_count
        
    return numbers

#ex
result1 = count_positives([-1, 1, 1, 1])
print(result1)

result2 = count_positives([1, 6, -4, -2, -7, -2])
print(result2)
print("\n")

print("Sum Total")
def sum_total(numbers):
    total_sum = 0
    
    for num in numbers:#iterate through the list and add each number to the total sum
        total_sum += num#add the current number to the total sum
    
    return total_sum

#ex
result1 = sum_total([1, 2, 3, 4])
print(result1)

result2 = sum_total([6, 3, -2])
print(result2)
print("\n")

print("Average")
def average(numbers):
    # Check if the list is empty to avoid division by zero
    if not numbers:
        return 0#return 0 if the list is empty

    #calculate the sum of the numbers
    total_sum = sum(numbers)
    
    #calculate the average
    avg = total_sum / len(numbers)#divide the total sum by the number of elements
    
    return avg

#ex
result1 = average([1, 2, 3, 4])
print(result1)

result2 = average([6, 3, -2])
print(result2)
print("\n")

print("Length")
def length(lst):
    #initialize a counter to 0
    count = 0
    
    #iterate through each element in the list
    for _ in lst:
        count += 1#increment the counter for each element
    
    return count

#ex
result1 = length([37, 2, 1, -9])
print(result1)

result2 = length([1,5,4,56,7,89,98,65,2])
print(result2)
result3 = length([])
print(result3)
print("\n")

print("Minimum")
def minimum(lst):
    if not lst:
        return False
    
    
    min_value = lst[0]#initialize the minimum value to the first element
    
    
    for num in lst:#iterate through the list to find the minimum value
        if num < min_value:
            min_value = num
            
    return min_value

#ex
result1 = minimum([37, 2, 1, -9])
print(result1)

result2 = minimum([])
print(result2)

result3 = minimum([1,2,-10,-124,-1241,-132,-123,1764])
print(result3)
print("\n")

def maximum(lst):
    if not lst:
        return False
    
    
    max_value = lst[0]#initialize the maximum value to the first element
    
    
    for num in lst:#iterate through the list to find the minimum value
        if num > max_value:
            max_value = num
            
    return max_value

#ex
result1 = maximum([37, 2, 1, -9])
print(result1)

result2 = maximum([])
print(result2)

result3 = maximum([1,2,3,4,5,66,5,234,5,7468])
print(result3)
print("\n")

print("Ultimate Analaysis")
#######I used the built-in functions ("min", "max", "sum", "len")#######
def ultimate_analysis(lst):
    #calculate the sumTotal
    sum_total = sum(lst)
    
    #calculate the average
    average = sum_total / len(lst) if lst else 0
    
    #calculate the minimum
    minimum = min(lst) if lst else None
    
    #calculate the maximum
    maximum = max(lst) if lst else None
    
    #calculate the length
    length = len(lst)
    
    #create the result dictionary
    result = {
        'sumTotal': sum_total,
        'average': average,
        'minimum': minimum,
        'maximum': maximum,
        'length': length
    }
    
    return result

#ex
print(ultimate_analysis([37, 2, 1, -9]))
print("\n")

print("Reverse list")
def rev(lst):
    lst.reverse()
    return lst

lst = [1,2,3,4,5]
print(rev(lst))