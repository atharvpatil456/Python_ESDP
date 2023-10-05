class BankAccount:
    def __init__(self, name, accnumber, acctype, balance):
        self.name = name
        self.accnumber = accnumber
        self.acctype = acctype
        self.balance_amount = balance

    def deposit(self, amount):
        self.balance_amount += amount
        print(f"Money deposited. Current balance: {self.balance_amount}")

    def withdraw(self, amount):
        if amount > self.balance_amount:
            print("Not enough money in the account.")
        else:
            self.balance_amount -= amount
            print(f"Withdrawal successful. Current balance: {self.balance_amount}")

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance_amount - amount < 100:
            print("Minimum balance of 100 required.")
        else:
            super().withdraw(amount)

    def display(self):
        print("Account Details:")
        print(f"Depositor's Name: {self.name}")
        print(f"Account Number: {self.accnumber}")
        print(f"Account Type: {self.acctype}")
        print(f"Balance: {self.balance_amount}")

    def __del__(self):
        print(f"Account {self.accnumber} for {self.name} has been deleted.")

# Create an instance of SavingAccount
name = input("Enter the Name: ")
accnumber = input("Enter Account Number: ")
acctype = input("Enter The Account Type: ")
balance = int(input("Enter the Amount: "))
account = SavingAccount(name, accnumber, acctype, balance)

while True:
    print()
    print("1. Display Balance")
    print("2. Withdraw Balance")
    print("3. Deposit Balance")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        account.display()
    elif ch == 2:
        witha = int(input("Enter the Withdraw Amount: "))
        account.withdraw(witha)
    elif ch == 3:
        dep = int(input("Enter the Deposit Amount: "))
        account.deposit(dep)
