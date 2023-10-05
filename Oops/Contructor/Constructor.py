# Local variable
class Test1(object):
    def func(self):
        print(10)
    def func2(self):
        print(50)
p1 = Test1()
p1.func()
p1.func2()

# same Constorcor asel tar last vala hoto falt
class Same:
    def __init__(self):
        print("Not call")
    def __init__(self):
        print("Not call 2 ")
t2 = Same()

# last vala constructor (overloading) consider karata hai 
class Test:
    def __init__(self):
        print("Not call")
    def __init__(self,a):
        print("Not call : ",a)
    def __init__(self,a,b):
        print("Not call :",a,b)

p1 = Test(10,20)

# Overloading Ashi hote
class Overloading:
    def __init__(self,*n):
        print("Constructor with variable : ",n)

t = Overloading()
t = Overloading(10)
t = Overloading(10,20)

#function and constructor 
    
class Function:
    def __init__(self):
        print("Not call")           
    def func(self):
        print("Function call : ")

F2 = Function()
F2.func()






