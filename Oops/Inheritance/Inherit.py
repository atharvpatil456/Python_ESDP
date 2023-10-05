class Animal:                                 
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def showA(self):
        print(self.name,self.breed)

class fleg(Animal):
    def showB(self):
        self.dog= "four leg"
        print(self.dog)

class dog(fleg):
    def showdog(self):
        print("Its Dog")

class cat(fleg):
    def showcat(self):
        print("Its cat")


obj1 = Animal("Chikku","Lab")
obj1.showA()
obj2 = fleg("Chikku","Lab")
obj2.showA()
obj2.showB()
obj = dog("Chikku","Lab")
obj.showdog()
obj4 = cat("Chikku","Lab")
obj4.showcat()

