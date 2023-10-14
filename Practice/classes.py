class Car:

    #these are static variabe or class variable i.e. these will be same for all the objects that will be created 
    #and if we change this it will affect all the object 
    wheels = 4
    company = 'BMW'

    # this is the constructor of the class, we don't need to call this, it is called automatically one the object of the class is created
    def __init__(self,engine, model, color):

        # these are instance variables, these are specific to the objects, 
        self.engine = engine
        self.model = model
        self.color = color

    # creting the method of the class / behaviour
    # this is a instance method as it works with objects (self)
    def getDetails(self):
        print(f"Engine : {self.engine}")
        print(f"Model : {self.model}")
        print(f"Color : {self.color}")

    #declaring class method to work with class variables like company and wheels
    @classmethod
    def info(cls):
        print(f"No. of wheels : {cls.wheels}")

    # declaring static method
    #static methods are those which dont have any relation with class variable as well as instance variable 
    @staticmethod
    def calculate():
        print("this is a static method nothing to do with class or instance variables")
        print("we use this when we need to work with other variable maybe from other class ")



#creating the object to the class with specific features
c1 = Car('Diesel',1968,'Red')
c2 = Car('Petrol',2004,'Blue')
c3 = Car('Electric',2022,'White')

#we have two ways to call the methods of the class 
# first 
Car.getDetails(c1)

#second
c2.getDetails()

# We can also cahnge the attributes of any object like color engine model etc
c3.model =2021
c3.getDetails()

# we can print the class variable with help of object and can also modify but it will be modified for all the object created for that class
print(c2.company)
Car.company = "Audi"

print(c1.company)
print(c2.company)

c1.info()

Car.calculate()