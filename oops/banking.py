from random import randint

class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter name = ")
        self.phone_number = input("Enter number = ")
        self.balance = 0

    def show_balance(self) -> None:
        print(f"Current balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def deposit(self) -> None:
        amount = int(input("Enter amount to deposit = "))
        self.balance += amount

# Corrected the object creation and method calls
# b1 = Bank()
# b1.show_balance()
# b1.deposit()
# b1.show_balance()
# b1.withdraw()
# b1.show_balance()

# banks = []

# x=Bank()
# banks.append(x)
# print(banks)

# y= Bank()
# banks.append(y)
# print(banks)

# banks[0].show_balance()
# banks[1].deposit()
# banks[1].show_balance()


