class User:
    def __init__(self, firstname, lastname, email, sex, address):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.sex = sex
        self.address = address

    def full_name(self):
        return self.firstname + " " + self.lastname
    def print_address(self):
        return f"This is the user's address: {self.address}"