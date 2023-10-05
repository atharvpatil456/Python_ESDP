class Parent:
    def properties(self):
        print("Cash, Gold")

    def bike(self):
        print("Splender+")


class Child(Parent):
    def bike(self):
        print("Avenger")


c = Child()
c.properties()
c.bike()
