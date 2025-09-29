# Dictionary Quick Reference

## Creating Dictionaries
```python
# Empty dictionary
empty = {}

# With data
student = {"name": "John", "age": 20, "grade": "A"}

# Using dict()
person = dict(name="Alice", age=25)
```

## Accessing Data
```python
# Direct access
name = student["name"]

# Safe access (returns None if key doesn't exist)
phone = student.get("phone")

# With default value
phone = student.get("phone", "Not provided")
```

## Modifying Data
```python
# Add new key-value
student["email"] = "john@example.com"

# Update existing
student["age"] = 21

# Update multiple
student.update({"grade": "A+", "course": "Python"})
```

## Removing Data
```python
# Remove and get value
removed = student.pop("course")

# Remove key (KeyError if not found)
del student["email"]

# Remove and get value with default
grade = student.pop("grade", "No grade")

# Clear all
student.clear()
```

## Dictionary Methods
```python
# Get all keys
keys = student.keys()

# Get all values  
values = student.values()

# Get key-value pairs
items = student.items()

# Check if key exists
if "name" in student:
    print(student["name"])

# Get length
count = len(student)
```

## Looping
```python
# Loop through keys
for key in student:
    print(key, student[key])

# Loop through values
for value in student.values():
    print(value)
    
# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

## Common Patterns
```python
# Count items
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Group items
groups = {}
for item in items:
    key = item.category
    if key not in groups:
        groups[key] = []
    groups[key].append(item)

# Default values with setdefault
groups.setdefault(key, []).append(item)
```

## Key Points
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any type and can repeat
- Dictionaries are unordered (but maintain insertion order in Python 3.7+)
- Use `get()` to avoid KeyError
- Much faster than lists for lookups