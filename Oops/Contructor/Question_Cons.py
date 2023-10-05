class Student:
    def __init__(self):
        self.name = None
        self.roll = None
        self.address = None
        self.perc = None

    def from_input(self):
        self.name = input("Enter your Name: ")
        self.roll = input("Enter your Roll: ")
        self.address = input("Enter your Address: ")
        self.perc = float(input("Enter your Percentage: "))  # Use float for percentage

    def display(self):
        return f"Student: {self.name}, Roll: {self.roll}, Address: {self.address}, Percentage: {self.perc} %"


obj1 = Student()

obj1.from_input()

print(obj1.display())
