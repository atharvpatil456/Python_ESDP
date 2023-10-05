class Student:
    def __init__(self, name, roll, address, perc):
        self.name = name
        self.roll = roll
        self.address = address
        self.perc = perc

    @classmethod
    def from_input(cls):
        name = input("Enter your Name: ")
        roll = input("Enter your Roll: ")
        address = input("Enter your Address: ")
        perc = int(input("Enter your Percentage: "))  # Use float for percentage
        return cls(name, roll, address, perc)

    def display(self):
        
        return f"Student: {self.name}, Roll: {self.roll}, Address: {self.address}, Percentage: {self.perc}"

# Get student information
obj1 = Student.from_input()

# Display student information
print(obj1.display())
