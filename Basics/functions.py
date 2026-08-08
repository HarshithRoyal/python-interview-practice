# ==========================================
# Python Interview Practice
# Topic: Functions
# ==========================================

# Function without parameters
def greet():
    print("Hello!")

greet()

# Function with parameters
def add(a, b):
    return a + b

print(add(10, 20))

# Default parameter
def greet_user(name="Guest"):
    print(f"Welcome {name}")

greet_user()
greet_user("Harshith")

# Keyword arguments
def employee(name, salary):
    print(name, salary)

employee(salary=80000, name="John")

# Variable length arguments
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40))
