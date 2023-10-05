class ElectricityBill:
    def __init__(self, name, units_cons):
        self.name = name
        self.units_cons = units_cons
        self.total_amount = 0

    def calculate_charge(self):
        if self.units_cons<=30:
            self.total_amount = self.units_cons*1.50
        elif self.units_cons<=230:
            self.total_amount = 30*1.50+(self.units_cons-30)*3.00
        else:
            self.total_amount = 30*1.50+200*3.00+(self.units_cons-230)*4.25

        if self.total_amount > 500.00:
            additional_charge = 0.15*self.total_amount
            self.total_amount += additional_charge

    def display_bill(self):
        print("Name:"+self.name+"")
        print(f"Units Consumed: {self.units_cons}")
        print(f"Total Amount: Rs. {self.total_amount:.2f}")
        print("-"*25)


user_data = [
    ("Atharv", 25),
    ("jatin", 300),
    ("tushar", 550),
]

for name, units in user_data:
    bill = ElectricityBill(name, units)
    bill.calculate_charge()
    bill.display_bill()
