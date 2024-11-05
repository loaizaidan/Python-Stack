from User import User

class Customer(User):
    def __init__(self, points, credit, name, address, phone, email):
        super().__init__(name, address, phone, email)
        self.points = points
        self.credit = credit

    def print_points(self):
        print("The number of points is: " + str(self.points))

loai = Customer(1000, 2000, "Loai", "WB", "0595334401", "loaizaidan@gmail.com")

loai.print_customer_info()
loai.print_points()