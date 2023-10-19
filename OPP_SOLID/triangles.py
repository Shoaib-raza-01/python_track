import math

class Triangles:
    def __init__(self):
        self.list_of_points = []

    def add_points(self, points):
        if len(self.list_of_points) < 3:
            self.list_of_points.append(points)

    def perimeter(self):
        d1 = math.dist(self.list_of_points[0], self.list_of_points[1])
        d2 = math.dist(self.list_of_points[1], self.list_of_points[2])
        d3 = math.dist(self.list_of_points[2], self.list_of_points[0])
        perimeter = d1 + d2 + d3
        print(f"Perimeter of the given triangle is: {perimeter}")
        

    # def is_equal(self, other):
    #     if self.list_of_points == other.list_of_points:
    #         print("The triangles are equal.")
    #     else:
    #         print("The triangles are not equal.")


    def __eq__(self, other):
        if self.list_of_points == other.list_of_points:
            print("The triangles are equal.")
        else:
            print("The triangles are not equal.")

    # def printpoint(self):
    #     print(self.list_of_points)

def input_points(name):
    for i in range(3):
        x = int(input(f"Enter x-coordinate for {i + 1} point: "))
        y = int(input(f"Enter y-coordinate for {i + 1} point: "))
        name.add_points((x, y))
        print()

t1 = Triangles()
t2 = Triangles()

print("Enter points for Triangle 1:")
input_points(t1)

print("Enter points for Triangle 2:")
input_points(t2)


t1.perimeter()

# print("Triangle 2:")
# t1.printpoint()
t2.perimeter()

# t1.is_equal(t2)
t1 == t2