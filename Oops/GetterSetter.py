class Student:
    def setName(self,name):
        self.name = name 
    def getName(self):
        return self.name
    def setperc(self,perc):
        self.perc = perc 
    def getperc(self):
        return self.perc

n = int(input("Enter the NO of Student :"))
s1 = Student()


for i in range(n):
    name = input("Enter the Name :")
    s1.setName(name)
    print(s1.getName())
    perc = float(input("Enter the Percentage :"))
    s1.setperc(perc)
    print(s1.getperc())