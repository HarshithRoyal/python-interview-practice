# ==========================================
# Python Interview Practice
# Topic: Lambda, map(), filter(), reduce()
# ==========================================

# ---------- LAMBDA ----------

# Normal function
def square(x):
    return x * x

print(square(5))

# Lambda version
square_lambda = lambda x: x * x

print(square_lambda(5))


# Lambda with two arguments
add = lambda a, b: a + b

print(add(10, 20))


# ---------- MAP ----------

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)


# ---------- FILTER ----------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)


# ---------- REDUCE ----------

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


# ---------- REALISTIC EXAMPLE ----------

employees = [
    {"name": "Alice", "salary": 80000},
    {"name": "Bob", "salary": 55000},
    {"name": "John", "salary": 90000}
]

high_salary_employees = list(
    filter(
        lambda employee: employee["salary"] > 70000,
        employees
    )
)

print(high_salary_employees)


# Extract only employee names
names = list(
    map(
        lambda employee: employee["name"],
        employees
    )
)

print(names)
