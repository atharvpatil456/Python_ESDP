class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

student_name = input("Enter Student's Name: ")
student_age = int(input("Enter Student's Age: "))
student_id = input("Enter Student's ID No. : ")


student = Student(student_name, student_age, student_id)

teacher_name = input("Enter Teacher's Name: ")
teacher_age = int(input("Enter Teacher's Age: "))
teacher_subject = input("Enter Teacher's Subject: ")


teacher = Teacher(teacher_name, teacher_age, teacher_subject)

student.study()
teacher.teach()
