class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


class Book(Product):
    def __init__(self, name, price, quantity, author, genre):
        super().__init__(name, price, quantity)
        self.author = author
        self.genre = genre

    def display_details(self):
        super().display_details()
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")


class Electronics(Product):
    def __init__(self, name, price, quantity, brand, category):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.category = category

    def display_details(self):
        super().display_details()
        print(f"Brand: {self.brand}")
        print(f"Category: {self.category}")


class Clothing(Product):
    def __init__(self, name, price, quantity, size, color):
        super().__init__(name, price, quantity)
        self.size = size
        self.color = color

    def display_details(self):
        super().display_details()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")



book_example = Book("Batatyachi Chal", 12323, 123, "PUl.Deshpande", "Comedy")
book_example.display_details()

electronics_example = Electronics("Electronics", 2134, 23, "Sony", "TV")
electronics_example.display_details()

clothing_example = Clothing("jocky", 99, 20, "M", "Blue")
clothing_example.display_details()
