class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is performing their job.")

    def getSalary(self):
        print(f"The salary of {self.name} is  {self.salary}")


class HRManager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        

    def work(self):
        print(f"{self.name} is managing human resources.")

    def addEmployee(self, employee):
        print(f"{employee.name} added to the employee list.")



employee1 = Employee("Atharv ", 59000)
hr_manager = HRManager("Vishnu", 78000)

employee1.work()
employee1.getSalary()

hr_manager.work() 
hr_manager.getSalary()

employee2 = Employee("Atharv", 599000)
hr_manager.addEmployee(employee2)  


