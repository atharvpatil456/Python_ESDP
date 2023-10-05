class Student:
    def __init__(self):
        print("Arrey bhai _______")
    def fuc1(self):
        print("Atharv patil")
    class inner:
        def __init__(self):
            print("Array innner _________")
        def func2(self):
            print("Inner class Run")
s1 = Student()
s=s1.inner()
s.func2()
obj = Student().inner()
#obj.func2()

