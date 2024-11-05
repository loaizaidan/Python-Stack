import random

def randInt(min=0, max=100):
    #if only max is provided
    if max is not None and min is None:
        return round(random.random() * max)
    #if only min is provided
    elif min is not None and max is None:
        return round(random.random() * (100 - min) + min)
    #if both min and max are provided
    elif min is not None and max is not None:
        return round(random.random() * (max - min) + min)
    #if no arguments are provided
    elif min is None and max is None: 
        return round(random.random() * 100)

#ex
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
