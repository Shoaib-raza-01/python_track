# Objects and Object Oriented Programming

**Object-Oriented Programming (OOP)** is one of the widely used concept and is essential for building complex and maintainable codes. Objects are instances of classes, and classes serve as blueprints or templates for creating objects and everything is an object in Python, even the variable are an object of class int or float and so on.

## 1. Objects

- **Definition :** An object is an instance of a class that are self-contained unit i.e it contains both data (attributes) and behavior (methods).

- For our better understanding let's take one real-world scenario, a car can be considered as an object. It has attributes like color, model, and speed, and it can perform actions(methods) like starting, stopping, and accelerating.

```Python
c = 10
print(type(c))
#output   :    <class 'int'>

# Here c is an object of class int

```


## 2. Classes

- **Definition:** A class is a blueprint or a template for creating objects. It defines the attributes and methods that the objects of the class will have.

- **Example:** If we consider a "Car" class, it would specify that a car object will have attributes like color and model and methods like start() and stop().

```python
# This is how we create a class
class Car:
    def __init__(self, brand, model):
        #these are attributes
        self.brand = brand
        self.model = model

    # methods
    def start(self):
        pass
    def stop(self):
        pass

# here my_car is an object of class Car
my_car = Car("Toyota", "Corolla")
print(type(my_car))
# output    <class '__main__.Car'> 
```

## 3. Attributes and Methods

- **Attributes:** Attributes are properties that describe the object. They can be of different data types (e.g., strings, integers, etc.).

- **Methods:** Methods are functions defined within a class that define the behaviors or actions that objects of that class can perform.

- **Example:** In a "Person" class, attributes could be "name" and "age," and methods could be "walk()" and "talk()".

```Python
class Person:
    #constructor of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #these are the methods that define the behaviour of the object
    def greet(self):
        return f"Hello {self.name}, you are {self.age} years old."

    def walk(self):
        print(f"{self.name} walks.")

    def talk(self):
        print(f"{self.name} talks.")

# creating object
person1 = Person("John Doe", 40)
# methods of the class can be called using dot(.) operator
# object_name.method_name
print(person1.greet()) 
person1.walk()
person1.talk()
```

## 4. Encapsulation

- **Definition:** Encapsulation is one of the fundamental principles of OOP. It involves bundling data (attributes) and the methods that operate on that data into a single unit (a class).

- **Purpose:** Encapsulation helps in hiding the internal details of a class and exposing only the necessary functionalities. This promotes data integrity and reduces complexity.

## 5. Inheritance

- **Definition :** Inheritance is a mechanism that allows a new class (the child or subclass) to inherit all the attributes and methods from an existing class (the parent or superclass). 

- **Types of inheritance :** 
    - **Single Inheritance :**  Single inheritance enables a derived class to inherit properties from a single parent class

        ```Python
        # Base class
        class Parent:
            def func1(self):
                print("This function is in parent class.")

        # Derived class
        class Child(Parent):
            def func2(self):
                print("This function is in child class.")

        # Driver's code
        object = Child()
        object.func1()
        object.func2()
        ```
    - **Multiple Inheritance :**  When a class is derived from more than one class so that it can have the methods of both the class is called multipe inheritance
        ```Python
        # Base class1
        class Mother:
            mothername = ""
            def mother(self):
                print(self.mothername)

        # Base class2
        class Father:
            fathername = ""
            def father(self):
                print(self.fathername)

        # Derived class
        class Son(Mother, Father):
            def parents(self):
                print("Father :", self.fathername)
                print("Mother :", self.mothername)

        # Driver's code
        s1 = Son()
        s1.fathername = "RAM"
        s1.mothername = "SITA"
        s1.parents()
        ```
    - **Multilevel Inheritance :** In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
        ```Python
        # Base class
        class Grandfather:
            def __init__(self, grandfathername):
                self.grandfathername = grandfathername
        # Intermediate class
        class Father(Grandfather):
            def __init__(self, fathername, grandfathername):
                self.fathername = fathername
                Grandfather.__init__(self, grandfathername)

        # Derived class
        class Son(Father):
            def __init__(self, sonname, fathername, grandfathername):
                self.sonname = sonname
                Father.__init__(self, fathername, grandfathername)
            def print_name(self):
                print('Grandfather name :', self.grandfathername)
                print("Father name :", self.fathername)
                print("Son name :", self.sonname)

        # Driver code
        s1 = Son('Prince', 'Rampal', 'Lal mani')
        print(s1.grandfathername)
        s1.print_name()
        ```

## 6. Polymorphism

- **Definition:** Polymprphism simply means having many form, base class will inherit methods from it's parent calss but it can also have it's own same methods with different implementation

```Python
class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
```