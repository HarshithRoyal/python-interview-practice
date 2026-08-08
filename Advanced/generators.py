# ==========================================
# Python Interview Practice
# Topic: Generators
# ==========================================

# Basic Generator

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

# ------------------------------------------

# Generator using a loop

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for number in count_up_to(5):
    print(number)

# ------------------------------------------

# Generator Expression

squares = (x * x for x in range(5))

for square in squares:
    print(square)

# ------------------------------------------

# Generator vs List

list_example = [x for x in range(10)]

generator_example = (x for x in range(10))

print(type(list_example))
print(type(generator_example))

# ------------------------------------------

# Fibonacci Generator

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b

for value in fibonacci(10):
    print(value)
