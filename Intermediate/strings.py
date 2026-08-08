# ==========================================
# Python Interview Practice
# Topic: Strings
# ==========================================

text = "Data Analyst"

# Convert to uppercase
print(text.upper())

# Convert to lowercase
print(text.lower())

# Length
print(len(text))

# Replace text
print(text.replace("Analyst", "Scientist"))

# Check beginning and ending
print(text.startswith("Data"))
print(text.endswith("Analyst"))

# Split string
skills = "Python,SQL,Power BI"
skill_list = skills.split(",")

print(skill_list)

# Join strings
words = ["Machine", "Learning", "Engineer"]
result = " ".join(words)

print(result)

# Remove spaces
name = "   Harshith   "
print(name.strip())

# String slicing
word = "Python"

print(word[0])      # P
print(word[-1])     # n
print(word[0:3])    # Pyt

# Reverse a string
print(word[::-1])

# Count occurrences
sentence = "Python SQL Python"
print(sentence.count("Python"))

# Find position
print(sentence.find("SQL"))

# Check if string contains text
if "SQL" in sentence:
    print("SQL found")
