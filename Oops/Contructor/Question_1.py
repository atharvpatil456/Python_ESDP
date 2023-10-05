class Time:
    def __init__(self, hour, minute, second):               # __init__ is the Constructor
        self.hour = hour                                    # self Work ass This keyword                           
        self.minute = minute
        self.second = second

    def display(self):
        return f"Time: {self.hour}:{self.minute}:{self.second}"              # f =  formatted string literal

obj1 = Time("2","20","12")
print(obj1.display())

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"Date: {self.day}/{self.month}/{self.year}"

obj1 = Date("19","03","2003")
print(obj1.display())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Person: {self.name}, Age: {self.age}"

obj1 = Person("Atharv","21")
print(obj1.display())


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display(self):
        return f"Student: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

obj1 = Student("Atharv","21","12")
print(obj1.display())

class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        return f"Fan: Brand - {self.brand}, Speed - {self.speed}"

obj1 = Fan("usha","150Rpm")
print(obj1.display())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"Point: ({self.x}, {self.y})"
    
obj1 = Point("12","21")
print(obj1.display())


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def display(self):
        return f"Box: Length - {self.length}, Width - {self.width}, Height - {self.height}"

obj1 = Box("4","2","15")
print(obj1.display())


