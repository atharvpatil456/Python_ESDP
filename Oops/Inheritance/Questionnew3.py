import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula to calculate the area of a triangle
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == "__main__":
    
    while True:
        print("1 . Rectangle")
        print("2 . Circle")
        print("3 . Triangle")
        print("4 . Exit")

        ch = int(input("Enter you choice: ")) 
        if(ch == 1):
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            rectangle = Rectangle(length, width)
            print("Rectangle Area:", rectangle.area())
            print("Rectangle Perimeter:", rectangle.perimeter())

        elif(ch == 2):
            radius = float(input("Enter radius of circle: "))
            circle = Circle(radius)
            print("Circle Area:", circle.area())
            print("Circle Perimeter:", circle.perimeter())

        elif(ch == 3 ):
            side1 = float(input("Enter side 1 of triangle: "))
            side2 = float(input("Enter side 2 of triangle: "))
            side3 = float(input("Enter side 3 of triangle: "))
            triangle = Triangle(side1, side2, side3)
            print("Triangle Area:", triangle.area())
            print("Triangle Perimeter:", triangle.perimeter())
        elif(ch == 4):
            exit()

            

