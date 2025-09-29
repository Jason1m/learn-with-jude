# Dictionary Examples

print("DICTIONARY EXAMPLES")
print("=" * 20)

# Example 1: Student grades
grades = {
    "Math": 85,
    "English": 92,
    "Science": 78
}
print(f"Grades: {grades}")
print(f"Math grade: {grades['Math']}")

# Add new subject
grades["History"] = 88
print(f"After adding History: {grades}")

# Example 2: User profile
profile = {
    "username": "jude_dev",
    "followers": 1250,
    "verified": True,
    "bio": "Teaching Python to everyone"
}

print(f"\nProfile: {profile}")
print(f"Followers: {profile['followers']}")

# Update followers
profile["followers"] += 50
print(f"New followers: {profile['followers']}")

# Example 3: Inventory system
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

print(f"\nInventory: {inventory}")

# Sell some items
inventory["apples"] -= 10
inventory["bananas"] -= 5

print(f"After sales: {inventory}")

# Example 4: Country capitals
capitals = {
    "Nigeria": "Abuja",
    "Ghana": "Accra",
    "Kenya": "Nairobi",
    "Egypt": "Cairo"
}

print(f"\nCapitals: {capitals}")

# Loop through dictionary
print("\nCountries and capitals:")
for country, capital in capitals.items():
    print(f"{country}: {capital}")

# Example 5: Nested dictionary
student_records = {
    "John": {
        "age": 20,
        "grades": [85, 90, 78],
        "major": "Computer Science"
    },
    "Alice": {
        "age": 19,
        "grades": [92, 88, 94],
        "major": "Data Science"
    }
}

print(f"\nStudent records: {student_records}")
print(f"John's grades: {student_records['John']['grades']}")

print("\n" + "=" * 20)