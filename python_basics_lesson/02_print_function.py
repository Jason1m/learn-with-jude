# 02_print_function.py
# This script shows how the print() function works in Python

# ===== BASIC PRINTING =====
# The print() function displays text and variables to the screen

# # Printing a simple message
# print("Hello, world!")

# # Printing multiple items (they get separated by spaces)
# print("Python", "is", "awesome!")

# # # ===== FORMATTING OUTPUT =====
# # # There are several ways to format text in Python

# 1. Using commas (adds spaces between items)
name = "Jude"
age = 25
print("Name:", name, "Age:", age)

# 2. Using the + operator (joins strings together without spaces)
print("Name: " + name + " Age: " + str(age))  # We need to convert numbers to strings

# 3. Using f-strings (modern, recommended way)
print(f"Name: {name} Age: {age}")

# ===== SPECIAL CHARACTERS =====
# \n creates a new line
print("First line\nSecond line")

# \t creates a tab space
print("Name:\tJude\nAge:\t25")

# ===== CONTROLLING PRINT BEHAVIOR =====
# By default, print() adds a newline at the end
print("This is on one line.")
print("This is on another line.")

# You can change this with the 'end' parameter
print("This text", end=" ")
print("continues on the same line.")

# The 'sep' parameter controls the separator between items
print("apple", "banana", "cherry", sep=" | ")

# ===== PRINTING FOR DEBUGGING =====
# print() is often used to check values during development
x = 10
y = 20
result = x + y
print(f"DEBUG: x={x}, y={y}, result={result}")

# ===== CHALLENGE FOR STUDENTS =====
# Try creating a small "receipt" using different print formatting techniques!
