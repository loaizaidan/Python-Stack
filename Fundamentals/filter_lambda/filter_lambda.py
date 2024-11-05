
number = [1,2,3,4,5,6,7,8,9,10]

even_number = list(filter(lambda x: x%2==0,number))


print(even_number)
######################################################


string = [' ', " ", 'loai', 'yasser', " ", 'python']

clean_string=list(filter(lambda x: x!= " " and x !="", string))




print(clean_string)



#######################

def is_age(x):
    return x>=18

ages=[10,22,33,91,10,2]

adults = list(filter(lambda x: x>=18, ages))

print(adults)


#########################################

product=[
    {"name":'phone',"price":500},
    {"name":'laptop',"price":3000},
    {"name":'mouse',"price":600},
    {"name":'keyboard',"price":450},
]

expen_items = list(filter(lambda x: x["price"]>500, product))

print(expen_items)
