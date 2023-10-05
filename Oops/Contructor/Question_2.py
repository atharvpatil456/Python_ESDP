class Sphere:
    def __init__(self,r):
        self.r = r
        self.total = 0
    
    def area(self):
        self.total = 4*3.14*self.r*self.r
        return f"Sphere Area :{self.total}"
    
    def volume(self):
        self.total = (4/3)*3.14*self.r*self.r*self.r
        return f"Volume Area :{self.total}"


obj1 = Sphere(12)
print(obj1.area())
print(obj1.volume())