from User import User

class Employee(User):
    def __init__(self, firstname, lastname, email, sex, address, salary, days_off):
        super().__init__(firstname, lastname, email, sex, address)
        self.salary = salary
        self.days_off= days_off

    def set_salary(self, salary):
        self.salary= salary

    def get_salary(self):
        return f"{self.firstname} {self.lastname}, Your salary is: {self.salary}"

e1=Employee("Loai","Zaidan","loaizaidan@gmail.com","Male","WB",4000, 50)
print(e1.get_salary())