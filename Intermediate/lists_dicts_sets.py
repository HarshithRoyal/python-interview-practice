# ==========================================
# Python Interview Practice
# Topic: Lists, Tuples, Dictionaries & Sets
# ==========================================

# ---------- LIST ----------

numbers = [10, 20, 30, 40]

print(numbers)

numbers.append(50)
print(numbers)

numbers.remove(20)
print(numbers)

numbers.sort()
print(numbers)

print(numbers[0])
print(numbers[-1])

# Loop through list
for num in numbers:
    print(num)

# List Comprehension
squares = [x * x for x in range(5)]
print(squares)

# ---------- TUPLE ----------

employee = ("John", 101, "Data Analyst")

print(employee)

print(employee[0])

# ---------- DICTIONARY ----------

student = {
    "name": "Alice",
    "age": 23,
    "course": "Computer Science"
}

print(student)

print(student["name"])

student["age"] = 24

student["city"] = "Chicago"

print(student)

for key, value in student.items():
    print(key, value)

# ---------- SET ----------

skills = {"Python", "SQL", "Power BI"}

print(skills)

skills.add("Machine Learning")

skills.add("Python")

print(skills)

for skill in skills:
    print(skill)
