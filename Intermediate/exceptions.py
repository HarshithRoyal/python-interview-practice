# ==========================================
# Python Interview Practice
# Topic: Exception Handling
# ==========================================

# Basic try-except
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Invalid integer")
except TypeError:
    print("Type error")

# try-except-else
try:
    number = int("100")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", number)

# try-except-finally
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

# Raising an exception
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    print(withdraw(1000, 1500))
except ValueError as e:
    print(e)

# Custom exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    print("Eligible")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)
