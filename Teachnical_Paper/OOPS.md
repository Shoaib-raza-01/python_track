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

- **Definition:** Inheritance is a mechanism that allows a new class (the child or subclass) to inherit all the attributes and methods from an existing class (the parent or superclass). 

- **Example:** If you have a "Vehicle" class, you can create subclasses like "Car" and "Bicycle" that inherit attributes and methods from the parent class.

## 6. Polymorphism

- **Definition:** Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the use of a single interface to represent a general class of actions.

- **Example:** In a "Shape" hierarchy, both "Circle" and "Rectangle" classes can have a method called "area()". You can call `area()` on any shape object, and it will behave differently based on the actual shape type.