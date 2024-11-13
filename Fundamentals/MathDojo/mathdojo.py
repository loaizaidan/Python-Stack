class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

md = MathDojo()
print("X:")
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)
print("\n")
print("Y:")
y = md.subtract(2,3).add(2,3).result
print(y)
print("\n")
print("Z:")
z= md.add(2).subtract(3).result
print(z)