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

    def display(self):
        print("Account Details:")
        print(f"Depositor's Name: {self.name}")
        print(f"Account Number: {self.accnumber}")
        print(f"Account Type: {self.acctype}")
        print(f"Balance: {self.balance_amount}")

    def __del__(self):
        print(f"Account {self.accnumber} for {self.name} has been deleted.")

name  = input("Enter the Name :")
accnumber = input("Enter Account Number :")
acctype  = input("Enter The Account Type :")
balance = int(input("Enther the Ammount :"))
account = BankAccount(name,accnumber,acctype,balance)

account.display()


while True:
    print()
    print("1. Display Balance ")
    print("2. Withdraw Balance ")
    print("3. Deposit Balance ")
    ch = int(input("Enter Your Choice : "))
    if(ch==1):
        account.display()
    elif(ch==2):
        witha= int(input("Enther the Withdraw Ammount :"))
        account.withdraw(witha)
        # account.display()
    elif(ch==3):
        dep = int(input("Enther the deposit Ammount :"))
        account.deposit(dep)
        # account.display()


