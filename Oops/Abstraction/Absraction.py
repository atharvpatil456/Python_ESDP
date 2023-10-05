from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, title, duration, price, instructor):
        self.title = title
        self.duration = duration
        self.price = price
        self.instructor = instructor

    
    def get_details(self):
        pass

    def enroll(self):
        print("Enrolled in", self.title, "course.")

class ProgrammingCourse(Course):
    def __init__(self, title, duration, price, language, instructor):
        super().__init__(title, duration, price, instructor)
        self.language = language

    def get_details(self):
        print("Course Title:", self.title)
        print("Duration:", self.duration)
        print("Price:", self.price)
        print("Programming Language:", self.language)
        print("Instructor:", self.instructor)

class MathCourse(Course):
    def __init__(self, title, duration, price, level, instructor):
        super().__init__(title, duration, price, instructor)
        self.level = level

    def get_details(self):
        print("Course Title:", self.title)
        print("Duration:", self.duration)
        print("Price:", self.price)
        print("Level:", self.level)
        print("Instructor:", self.instructor)

class LanguageCourse(Course):
    def __init__(self, title, duration, price, language, instructor):
        super().__init__(title, duration, price, instructor)
        self.language = language

    def get_details(self):
        print("Course Title:", self.title)
        print("Duration:", self.duration)
        print("Price:", self.price)
        print("Language:", self.language)
        print("Instructor:", self.instructor)


programming_course = ProgrammingCourse("Python Programming", "8 weeks", 200, "Python", "John Doe")
math_course = MathCourse("Algebra", "10 weeks", 150, "Intermediate", "Jane Smith")
language_course = LanguageCourse("Spanish Language", "12 weeks", 180, "Spanish", "Maria Garcia")

programming_course.get_details()
programming_course.enroll()
print()

math_course.get_details()
math_course.enroll()
print()

language_course.get_details()
language_course.enroll()
