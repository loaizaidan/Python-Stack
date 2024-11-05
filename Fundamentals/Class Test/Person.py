#  __         ______     ______     __   
# /\ \       /\  __ \   /\  __ \   /\ \  
# \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \ 
#  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\
#   \/_____/   \/_____/   \/_/\/_/   \/_/

from BankAccount import BankAccount
class Person:
    
    def __init__(self, firstname, famname, phonenum, address):
        self.firstname = firstname
        self.lastname = famname
        self.mobilenum = phonenum
        self.ad = address
        self.bankaccount = BankAccount(1000,"ILS",0.2,"savings")

    def get_firstname(self):
        return self.firstname
    
    def get_fullname(self):
        return self.firstname + " " + self.lastname
    
    def print_msg(self):
        print("Hello I do not use Self")
        
    def set_first_name(self, name):
        self.firstname = name

    def bankacc(self):
        return self.bankaccount.balance

        
loai = Person("Loai", "Zaidan", "0595334401", "Al-Tireh")
omar = Person("Omar", "Rayyan", "0599111111", "Canada")

print(loai.get_firstname())
print(loai.print_msg())
print(loai.get_fullname())
print(omar.get_fullname())
#print(omar.print_msg())
print(loai.bankacc())