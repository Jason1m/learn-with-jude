# 05_logic_and_conditionals.py
# This script shows how to use conditionals and logic in Python

# ===== IF STATEMENTS =====
# If statements let you make decisions in your code

print("===== BASIC IF STATEMENT =====")

# Simple if statement
age = 20
if age >= 18:
    print("You are an adult")

# if-else statement
temperature = 15
print("\nChecking temperature...")
if temperature > 25:
    print("It's warm outside")
else:
    print("It's cool outside")

# if-elif-else for multiple conditions
score = 85
print("\nCalculating grade...")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ===== COMPARISON OPERATORS =====
print("\n===== COMPARISON OPERATORS =====")
a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a < b: {a < b}")    # Less than
print(f"a > b: {a > b}")    # Greater than
print(f"a <= b: {a <= b}")  # Less than or equal to
print(f"a >= b: {a >= b}")  # Greater than or equal to

# ===== LOGICAL OPERATORS =====
print("\n===== LOGICAL OPERATORS =====")

# AND: both conditions must be true
x = 5
print(f"x = {x}")
print(f"x > 0 and x < 10: {x > 0 and x < 10}")  # True
print(f"x > 0 and x > 10: {x > 0 and x > 10}")  # False

# OR: at least one condition must be true
y = 15
print(f"y = {y}")
print(f"y < 10 or y > 20: {y < 10 or y > 20}")  # False
print(f"y < 10 or y > 10: {y < 10 or y > 10}")  # True

# NOT: reverses the result
z = 7
print(f"z = {z}")
print(f"not z > 10: {not z > 10}")  # True
print(f"not z < 10: {not z < 10}")  # False

# ===== NESTED CONDITIONALS =====
print("\n===== NESTED CONDITIONALS =====")

# One conditional inside another
user_age = 22
has_license = True

if user_age >= 18:
    print("Age requirement met")
    if has_license:
        print("You can rent a car")
    else:
        print("You need a license to rent a car")
else:
    print("You must be 18 or older to rent a car")

# ===== CHECKING MULTIPLE CONDITIONS =====
print("\n===== COMBINING CONDITIONS =====")

# Weather example
is_raining = False
temperature = 28

print("Weather check:")
if is_raining and temperature < 15:
    print("Cold and rainy - stay inside!")
elif is_raining:
    print("Warm but rainy - take an umbrella!")
elif not is_raining and temperature > 25:
    print("Warm and sunny - perfect for outdoors!")
else:
    print("Cool but not raining - light jacket recommended")

# ===== CHECKING MEMBERSHIP =====
print("\n===== MEMBERSHIP CHECKS =====")

# Using 'in' to check if an item is in a collection
fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")

# Using 'in' with strings
name = "Alexander"
print(f"name = {name}")
print(f"'Alex' in name: {'Alex' in name}")
print(f"'Z' in name: {'Z' in name}")

# ===== PRACTICAL EXAMPLE =====
print("\n===== PRACTICAL EXAMPLE: AUTHENTICATION =====")

# Simple login system
correct_username = "admin"
correct_password = "password123"

# Get user input
username = input("Username: ")
password = input("Password: ")

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful! Welcome, admin.")
elif username == correct_username:
    print("Incorrect password. Please try again.")
elif password == correct_password:
    print("Incorrect username. Please try again.")
else:
    print("Both username and password are incorrect.")

# ===== CHALLENGE FOR STUDENTS =====
# Create a simple "rock, paper, scissors" game using conditionals!
