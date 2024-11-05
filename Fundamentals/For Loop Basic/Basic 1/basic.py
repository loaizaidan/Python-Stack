print("Task #1: Basic")
for z in range(151):
    print(z)  
print("\n")
print("Task #2: Multiples of Five")
for i in range(5,1001,5):
    print(i)  
print("\n")
print("Task #3: Counting, the Dojo Way")
for p in range(1, 101):
    if p % 10 == 0:
        print("Coding Dojo")
    elif p % 5 == 0:
        print("Coding")
    else:
        print(p)
print("\n")
print("Task #4: Whoa! That Sucker's Huge")
total_sum = 0

for i in range(1, 500001, 2):
    total_sum += i

print(total_sum)
print("\n")
print("Task #5: Countdown by fours")
for i in range(2024, 0, -4):
    print(i)
print("\n")
print("Task #6: Flexible Counter")
lowNum = 3
highNum = 9
mult = 6

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)