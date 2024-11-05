#  __         ______     ______     __   
# /\ \       /\  __ \   /\  __ \   /\ \  
# \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \ 
#  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\
#   \/_____/   \/_____/   \/_/\/_/   \/_/

class BankAccount:
    
    def __init__(self, balance, currency, interest_rate, account_type):
        self.balance = balance
        self.currency = currency
        self.interest_rate = interest_rate *0.1
        self.account_type = account_type
        
    def balance_withdraw(self, amount):
        return self.balance - amount
    
    def balance_deposit(self, amount):
        self.balance += amount
        return self.balance
    
    
ILS_account= BankAccount(1000, "ILS",0.01, "Saving")
print(ILS_account.balance_deposit(100))
print(ILS_account.balance_withdraw(220))
