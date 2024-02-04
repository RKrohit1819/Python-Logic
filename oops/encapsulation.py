from random import randint

class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.account_no = randint(200000, 999999)
        self.balance = 0
        
    def display(self):
        print(f"Account number = {self.account_no}")
        print(f"Name = {self.name}")
        print(f"Balance = {self.balance}")  # Corrected: added 'self.' before 'balance'

obj = Bank()
obj.display()
obj.account_no = 1
obj.display()
