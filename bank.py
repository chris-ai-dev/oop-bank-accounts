from owner import Owner


class Bank:
    def __init__(self):
        # #conatians
        # self.account = Account()
        pass
    
class Account(Owner):
    def __init__(self, id, balance,owner,last_name, first_name, street_address, city, state):
        super()__init__(id=id, last_name=last_name, first_name=first_name, street_address=street_address, city=city, state=state)
        if balance >= 0:
            self.balance = balance
        else:
            raise ValueError("Hi error")
        self.owner = owner

    def create_owner(self, owner):
        self.owner = owner
    
    def withdraw(self, money_to_withdraw):
        if self.balance == 0:
            raise Exception('Your Balance {self.balance}')
            
        new_balance = self.balance - money_to_withdraw
        if new_balance > 0:
            return self.balance
        else:
            raise Exception("Not enough moeny")
    
    def deposit(self, money_to_deposit):
        self.balance = self.balance + money_to_deposit
        return self.balance 
          
    def get_balance(self):
        return "Your current balance is:{self.balance}"

#Banco = Bank()
chris = Account(123,300)
# print(chris.id)
print(chris.balance)
chris.withdraw(100)
print(chris.balance)

 
            
    
    