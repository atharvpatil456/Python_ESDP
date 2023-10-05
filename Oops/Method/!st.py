class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    def showC(self):
        print("Class C")

obj_c = C()
obj_c.show()  
obj_c.showC()  




