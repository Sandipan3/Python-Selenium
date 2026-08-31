# A class is a blueprint. An object is something created from that blueprint.
# 1. Encapsulation: Encapsulation means keeping data and the methods that operate on that data together
# while controlling access to the data
class Student:

    next_id = 1              # class variable(like static variable)

    def __init__(self,name,age):
        self.id = Student.next_id   # instance variable
        self.name = name  # instance variable
        self.age = age  # instance variable

        Student.next_id += 1

    # A method is a function defined inside a class.
    def showDetails(self):
        print(f"{self.id}. {self.name} is {self.age} years old")

s1 = Student("John", 20)
s2 = Student("Alice", 22)
s3 = Student("Bob", 19)

s1.showDetails()
s2.showDetails()
s3.showDetails()

# Getter amd setters

class Employee:

    def __init__(self,salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setSalary(self,salary):
        if(salary < 0):
            raise ValueError("Can't accept negative error")
        self.salary = salary

e1 = Employee(100)
print(e1.getSalary()) 

e1.setSalary(1000) 
print(e1.getSalary()) 

try:
    e1.setSalary(-100)
except ValueError as e:
    print(e)


print("====Calculator====")

class Calculator:

    calculator_count = 0 # class variable

    def __init__(self, name):
        self.name = name
        Calculator.calculator_count += 1

    # instance methods
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def divide(self,a,b):
        if(b==0):
            raise ZeroDivisionError("Cannot divide by zero")
        return a/b

    # static methods
    @staticmethod
    def power(a,b):
        return a**b

    @staticmethod 
    def is_even(x):
        return x%2 ==0
    
    @staticmethod 
    def is_odd(x):
        return x%2 !=0
    
    @staticmethod
    def percentage(value, percent):
        return value * percent / 100

    # class methods
    # A class method is a method that receives cls (the class) 
    # instead of self (an object), and is mainly used to work with 
    # class-level data or create objects in alternative ways.
    @classmethod
    def get_calculator_count(cls):
        return cls.calculator_count
    
    @classmethod
    def reset_count(cls):
        cls.calculator_count = 0

    @classmethod
    def create_default(cls):
        return cls("Default Calculator")

# Type	                          Decorator	    First parameter	    Can access instance data?	Can access class data?
# Instance method	                None	        self	                ✅	                        ✅
# Class method	@classmethod	    cls	            ❌	                  ✅
# Static method	@staticmethod	    None	        ❌	                   ❌

c1 = Calculator("demo1")
c2 = c1.create_default()
c2.reset_count()
calc = Calculator("my calculator")
a=10
b=5
print(f"The name of the calculator is {calc.name}")
print(f"The calculator count is: {calc.calculator_count}")
print(f"The sum of {a} and {b} is {calc.add(a,b)}")
print(f"The diff {a} and {b} is {calc.subtract(a,b)}")
print(f"The product of {a} and {b} is {calc.multiply(a,b)}")
print(f"The division of {a} and {b} is {calc.divide(a,b)}")

print(f"{a}^{b} is {Calculator.power(a,b)}")
print(f"{a} is {Calculator.is_even(a)} even")
print(f"{a} is {Calculator.is_odd(a)} odd")
print(f"{b} is {Calculator.is_even(b)} even")
print(f"{b} is {Calculator.is_odd(b)} odd")
print(f"Percentage is {Calculator.percentage(a,b)}")


# 2. Inheritance: allows a new class (child/subclass) to acquire the properties (attributes) 
# and behaviors (methods) of an existing class (parent/superclass)
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Barking")

dog1 = Dog()
dog1.eat()
dog1.bark()

# Method overriding: A child can replace a parent's method.
class Dog(Animal):

    def eat(self):
        print("dog eating")

dog2 = Dog()
dog2.eat()

# super() Run the parent's version, then do my additional work
class Dog(Animal):

    def eat(self):
        return super().eat()

dog3 = Dog()
dog3.eat()

# Multilevel Inheritance:
# puppy(Dog) -> Dog(Animal) -> Animal

# Mutiple Inheritance: child extends 2 parents (safe if methods are diff)
class Father:
    def work(self):
        print("working")
class Mother:
    def cook(self):
        print("cooking")

class Child(Father,Mother):
    pass

child = Child()
child.cook()
child.work()

# What if both parents have the same method?
# MRO — Method Resolution Order
# class Child(X,Y): child will select X as parent
class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Mother, Father):
    pass


child = Child()
child.show()

# 3.Polymorphism: Many forms
# Below program also demonstrates Duck Typing
# Duck typing is a core programming concept in Python where an 
# object's suitability for a task is determined by the 
# presence of specific methods and attributes, 
# rather than its actual type or explicit inheritance

class Dog:
    def sound(self):
        print("woof")

class Cat:
    def sound(self):
        print("meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())

# 4.Abstraction: Abstraction is the practice of hiding complex implementation details 
# and showing only the essential features of an object. 
# It reduces complexity by letting you focus on what an object does rather than how it does it.

# ABC:  Abstract Base Classes. 
# It is a built-in module that allows you to define abstract classes and 
# enforce that child classes implement specific methods.

from abc import ABC, abstractmethod
# The Abstract Class (The Blueprint)
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof")
dog = Dog()
dog.sound()