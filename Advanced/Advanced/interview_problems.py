# ==========================================
# Python Interview Practice
# Topic: Common Coding Interview Problems
# ==========================================

# -------------------------------------------------
# 1. Reverse a String
# -------------------------------------------------

text = "Python"

print(text[::-1])

# -------------------------------------------------
# 2. Check Palindrome
# -------------------------------------------------

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# -------------------------------------------------
# 3. Find Largest Number
# -------------------------------------------------

numbers = [12, 45, 2, 98, 67]

print(max(numbers))

# -------------------------------------------------
# 4. Find Second Largest Number
# -------------------------------------------------

numbers = [12, 45, 2, 98, 67]

numbers.sort()

print(numbers[-2])

# -------------------------------------------------
# 5. Remove Duplicates
# -------------------------------------------------

numbers = [1,2,2,3,4,4,5]

unique = list(set(numbers))

print(unique)

# -------------------------------------------------
# 6. Count Character Frequency
# -------------------------------------------------

text = "banana"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char,0) + 1

print(frequency)

# -------------------------------------------------
# 7. Count Words
# -------------------------------------------------

sentence = "Python SQL Python Machine Learning"

words = sentence.split()

print(len(words))

# -------------------------------------------------
# 8. Fibonacci
# -------------------------------------------------

a,b = 0,1

for _ in range(10):
    print(a)
    a,b = b,a+b

# -------------------------------------------------
# 9. Prime Number
# -------------------------------------------------

number = 29

prime = True

for i in range(2,number):
    if number%i==0:
        prime=False
        break

print(prime)

# -------------------------------------------------
# 10. Factorial
# -------------------------------------------------

n = 5

fact = 1

for i in range(1,n+1):
    fact*=i

print(fact)

# -------------------------------------------------
# 11. Two Sum
# -------------------------------------------------

nums = [2,7,11,15]

target = 9

lookup = {}

for index,num in enumerate(nums):

    diff = target-num

    if diff in lookup:
        print(lookup[diff],index)

    lookup[num]=index

# -------------------------------------------------
# 12. Count Vowels
# -------------------------------------------------

text = "Machine Learning"

count = 0

for char in text.lower():
    if char in "aeiou":
        count+=1

print(count)

# -------------------------------------------------
# 13. Merge Two Lists
# -------------------------------------------------

list1=[1,2,3]
list2=[4,5,6]

print(list1+list2)

# -------------------------------------------------
# 14. Sort Dictionary by Value
# -------------------------------------------------

student = {
    "Alice":85,
    "Bob":91,
    "John":78
}

sorted_dict = sorted(student.items(), key=lambda x:x[1])

print(sorted_dict)

# -------------------------------------------------
# 15. Find Missing Number
# -------------------------------------------------

numbers = [1,2,3,5]

for i in range(1,6):
    if i not in numbers:
        print(i)
