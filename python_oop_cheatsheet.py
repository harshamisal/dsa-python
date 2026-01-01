"""
Python OOP Cheat Sheet with Interview Q&A (Jupyter Notebook Ready)

This notebook demonstrates core Object-Oriented Programming concepts in Python, step-by-step,
with short runnable examples and printed outputs. It also includes **common interview questions with answers**.

Concepts covered:
- Class & Object
- __init__ (constructor)
- Attributes: instance vs class variables
- Methods (instance / static / class)
- Encapsulation (private attributes + property)
- Inheritance & method overriding
- Polymorphism & duck typing
- Abstraction (ABC)
- Magic methods (dunder methods)
- Composition (has-a relationship)

Run each cell to see results.
"""

# -----------------------------
# 1) Class & Object, __init__
# -----------------------------
class Dog:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says Woof!"

# Q: What is the difference between a class and an object?
# A: Class is a blueprint, object is an instance of that class.

Dog("Rex").speak()


# -----------------------------
# 2) Attributes: class vs instance
# -----------------------------
class Student:
    school = "XYZ High School"  # class variable

    def __init__(self, name: str, roll: int):
        self.name = name
        self.roll = roll

s1 = Student("Alice", 1)
s2 = Student("Bob", 2)

# Q: Difference between class variable and instance variable?
# A: Class variable is shared across all objects, instance variable is unique per object.
(s1.name, s1.school, s2.school)


# -----------------------------
# 3) Methods: instance, classmethod, staticmethod
# -----------------------------
class MathOps:
    def instance_add(self, a, b):
        return a + b

    @classmethod
    def identity(cls):
        return cls.__name__

    @staticmethod
    def multiply(a, b):
        return a * b

mo = MathOps()
mo.instance_add(2, 3), MathOps.identity(), MathOps.multiply(4, 5)

# Q: Difference between staticmethod and classmethod?
# A: classmethod gets class as first argument, staticmethod does not.


# -----------------------------
# 4) Encapsulation
# -----------------------------
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = float(balance)  # private

    def deposit(self, amount: float):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = BankAccount("Harsh", 100)
acct.deposit(50)
acct.get_balance()

# Q: How do you achieve encapsulation in Python?
# A: By using private attributes (prefix __) or @property decorators.


# -----------------------------
# 5) Inheritance & Polymorphism
# -----------------------------
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

animals = [Dog("Buddy"), Cat("Mittens"), Animal("Generic")]
[a.speak() for a in animals]

# Q: What is method overriding?
# A: Redefining a parent class method in the child class.


# -----------------------------
# 6) Abstraction (ABC)
# -----------------------------
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * (self.r ** 2)

Rectangle(3, 4).area(), round(Circle(2.5).area(), 2)

# Q: Can we instantiate an abstract class?
# A: No, it can only be inherited and implemented.


# -----------------------------
# 7) Magic methods
# -----------------------------
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)

b1 = Book("Python", 200)
b2 = Book("ML", 150)
(str(b1), len(b1), str(b1+b2))

# Q: Why use magic methods?
# A: To make objects behave like built-ins (len, +, str, etc.).


# -----------------------------
# 8) Composition (has-a)
# -----------------------------
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

car = Car("Tesla", Engine(300))
car.brand, car.engine.horsepower

# Q: Difference between inheritance and composition?
# A: Inheritance is "is-a" relationship, composition is "has-a".


# -----------------------------
# 9) Duck typing
# -----------------------------
class Bird:
    def fly(self): return "Bird flies"

class Airplane:
    def fly(self): return "Airplane flies"

[obj.fly() for obj in (Bird(), Airplane())]

# Q: What is duck typing?
# A: If an object implements required method/behavior, type doesn’t matter.
