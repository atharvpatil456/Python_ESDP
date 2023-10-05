class Point:
    def set_coordinate(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")


class NewPoint(Point):
    def draw(self):
        print(f"Draw Point coordinates: ({self.x}, {self.y})")


if __name__ == "__main__":
    point_obj = NewPoint()
    point_obj.set_coordinate(3, 4)
    point_obj.show()
    point_obj.draw()
