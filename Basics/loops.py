# ==========================================
# Python Interview Practice
# Topic: Loops
# ==========================================

# For Loop
print("For Loop Example")

for i in range(1, 6):
    print(i)

# While Loop
print("\nWhile Loop Example")

count = 1

while count <= 5:
    print(count)
    count += 1

# Break
print("\nBreak Example")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue
print("\nContinue Example")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Loop through a list
print("\nLoop through List")

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

# Enumerate
print("\nEnumerate Example")

for index, fruit in enumerate(fruits):
    print(index, fruit)
