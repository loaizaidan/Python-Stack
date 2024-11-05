from User import User

class Student(User):
    def __init__(self, firstname, lastname, email, sex, address, grade):
        super().__init__(firstname, lastname, email, sex, address)
        self.grade = grade

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        print(f"Your name is: {self.firstname+" "+ self.lastname}, and your grade is: {self.grade}")
    
s1 = Student("Hamouda", "Owais", "owais@gmail.com", "Male", "WB", 87)
s1.get_grade()
        