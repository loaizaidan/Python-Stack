class User:

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    
    def print_user_info(self):
        print("User's name is: " + self.name + ", " + "User's Email is: " +  self.email)
    def print_employee_info(self):
        print("Employee's name is: " + self.name + ", " + "Employee's Email is: " +  self.email)
    def print_customer_info(self):
        print("Customer's name is: " + self.name + ", " + "Customer's Email is: " +  self.email)