# ==========================================
# Python Interview Practice
# Topic: Conditional Statements
# ==========================================

age = 25

if age >= 18:
    print("Adult")
else:
    print("Minor")


salary = 75000

if salary >= 100000:
    print("High salary")
elif salary >= 60000:
    print("Medium salary")
else:
    print("Entry-level salary")


# AND condition
experience = 3

if salary > 60000 and experience >= 2:
    print("Eligible")


# OR condition
department = "Data"

if department == "Data" or department == "Engineering":
    print("Technical department")
