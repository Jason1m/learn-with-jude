# Session 3: Dictionaries - The Labeled Container

print("SESSION 3: DICTIONARIES")
print("=" * 25)

# What is a Dictionary?
print("\n1. WHAT IS A DICTIONARY?")
print("Think of a real dictionary: word -> definition")
print("Python dictionary: key -> value")

# Creating dictionaries
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
print(f"\nStudent info: {student}")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Accessing values
print(f"\nStudent name: {student['name']}")
print(f"Student age: {student['age']}")

# Adding new data
student["course"] = "Python"
student["email"] = "john@example.com"
print(f"\nAfter adding data: {student}")

# Changing existing data
student["age"] = 21
student["grade"] = "A+"
print(f"\nAfter updating: {student}")

# Different data types
mixed_dict = {
    "name": "Alice",
    "scores": [85, 90, 78],
    "passed": True,
    "attempts": 3
}
print(f"\nMixed data types: {mixed_dict}")

# Dictionary methods
print(f"\nAll keys: {list(student.keys())}")
print(f"All values: {list(student.values())}")
# Using list() to convert dict_items to a list for clearer output for beginners
print(f"All items: {list(student.items())}")

# Safe access with get()
print(f"\nSafe access: {student.get('phone', 'Not provided')}")

# Check if key exists
if "email" in student:
    print(f"Email: {student['email']}")

# Remove items
removed = student.pop("course")
print(f"\nRemoved {removed}")
print(f"Updated dict: {student}")

print("\n" + "=" * 25)
print("Next: Building a contact manager!")