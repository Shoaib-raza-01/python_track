import math 
class Triangles:
    list_of_points = []

    def add_points(self,points):
        self.list_of_points.append(points)

    def perimeter(self):
        d1 = math.dist(self.list_of_points[0],self.list_of_points[1])
        d2 = math.dist(self.list_of_points[1],self.list_of_points[2])
        d3 = math.dist(self.list_of_points[2],self.list_of_points[0])
        perimeter = d1 + d2 + d3
        print(f"Perimeter of the given triangle is : {perimeter}")
    
    def is_equal(self,other):
        pass

    def printpoint(self):
        print(self.list_of_points)
def input_points(name):
    for i in range(3):
        x = int(input(f"Enter x co-ordinate for {i+1} point : "))
        y = int(input(f"Enter y co-ordinate for {i+1} point : "))
        name.add_points((x,y))
        print()

t1 = Triangles()
t2 = Triangles()

input_points(t1)
input_points(t2)
t1 = t2
t1.printpoint()
t1.perimeter()