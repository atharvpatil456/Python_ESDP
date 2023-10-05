class Distructor:
    def __init__(self):
        print("Constructor is called")
    def __del__(self):
        print("Distructor is called")
d1 = Distructor()
del d1
