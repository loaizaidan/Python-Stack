#       /-\
#      /---\
#     /Loai \
#    /Zaidan \
#   /---------\


print("Number 1: Countdown!")
def countdown(number):
    return [i for i in range(number, -1, -1)]

#ex:
result = countdown(5)
print(result)
print("\n")

print("Number 2: Print and Return!")
def print_and_return(numbers):
    print(numbers[0]) #here it will print the first "index".
    return numbers[1]  #here it will return the secondd "index"

#ex:
result = print_and_return([93,24,76])#added third number, to show it will not print or return it.
print(result)
print("\n")

print("Number 3: First Plus Length!")
def first_plus_length(first):
    return first[0] + len(first)

#ex
result = first_plus_length([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)
print("\n")

print("Number 4: Values greater than second!")
def val_grtr_than_sec(list):
    if len(list) < 2: #checking if the list has less than 2 elements
        return False
    
    second_value = list[1] #grabbing the second value and checking it
    
    new_list = [value for value in list if value > second_value]#creating a new list with the values greater than the second value
    
    print(len(new_list))

    return new_list#returns the new list

#ex:
result = val_grtr_than_sec([7, 8, 9, 11, 13, 12, 10])
print(result)
print("\n")

print("Number 5: This length, That value!")
def length_and_value(size, value):
    return [value] * size#create a list with the secified value and size

#ex:
result1 = length_and_value(4, 7)
print(result1)
result2 = length_and_value(13, 5)
print(result2)
print("\n")

print("Thank you for the taking the time to review my code!")