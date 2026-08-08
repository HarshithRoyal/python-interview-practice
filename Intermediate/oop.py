# ==========================================
# Python Interview Practice
# Topic: Object-Oriented Programming (OOP)
# ==========================================

# ---------- Class and Object ----------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")

emp1 = Employee("John", 80000)
emp1.display()

# ---------- Inheritance ----------

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

manager = Manager("Alice", 120000, "Data Science")
manager.display()

# ---------- Polymorphism ----------

class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# ---------- Encapsulation ----------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())

# ---------- Abstraction ----------

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)

print(rectangle.area())
