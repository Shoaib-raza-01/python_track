class Student:
    collage = "LPU"

    def __init__(self,name,rollno) -> None:
        self.name = name
        self.rollno = rollno

        #we can create the object of inner class here also in the init method
        self.lap1 = self.Laptop("16 GB", "core i7")
    
    def show(self):
        print(self.collage)
        print(self.name, self.rollno)
        print()
        self.lap1.show()
    
    #declaring inner class 
    class Laptop:
        brand = "ASUS"

        def __init__(self,ram,cpu) -> None:
            self.ram = ram
            self.cpu = cpu
        
        def show(self):
            print(self.brand)
            print(self.cpu, self.ram)

s1 = Student("Shoaib", 12017811)

#calling show methods

s1.show()
print()

#creating inner class object outside the outer class
lap = Student.Laptop('8 GB', "core i5")
lap.show()