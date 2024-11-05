from User import User

class Guest(User):
    def __init__(self, firstname, lastname, email, sex, address, freetrial):
        super().__init__(firstname, lastname, email, sex, address)
        self.freetrial = freetrial


    def countdown(self):
        return f"Dear Mr/Mrs. {self.lastname}, you have: {self.freetrial} days left in your free-trial!"
    
ft= Guest("Amani","Mhesen", "amani@yahoo.com","Male","WB",14)
print(ft.countdown())