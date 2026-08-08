# ==========================================
# Python Interview Practice
# Topic: Decorators
# ==========================================

# Basic Decorator

def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")
    return wrapper


@logger
def greet():
    print("Hello!")

greet()


# Decorator with Arguments

def logger(func):
    def wrapper(name):
        print("Executing function...")
        func(name)
        print("Execution completed")
    return wrapper


@logger
def welcome(name):
    print(f"Welcome {name}")

welcome("Harshith")


# Timing Decorator

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {end-start:.5f} seconds")
    return wrapper


@timer
def calculate():
    total = 0
    for i in range(100000):
        total += i

calculate()
