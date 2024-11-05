from User import User

class Employee(User):

    def __init__(self, salary,name, address, phone, email):
        super().__init__(name, address, phone, email)
        self.salary = salary
    def print_salary(self):
        print("Your salary is: " + str(self.salary))

ali = Employee(3000, "Ali", "Russia", "0599100200", "ali@axsos.edu")
ali.print_employee_info()
ali.print_salary()