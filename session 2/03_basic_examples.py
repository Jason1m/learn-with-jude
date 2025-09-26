# Session 2: Basic List Examples
# Simple examples to understand lists step by step

print("🎯 BASIC LIST EXAMPLES")
print("=" * 40)

# EXAMPLE 1: Your First List
print("\n1️⃣ EXAMPLE 1: Creating Your First List")
print("-" * 35)

# Let's create a list of your favorite colors
favorite_colors = ["blue", "green", "purple"]
print(f"My favorite colors: {favorite_colors}")

# Access the first color
first_color = favorite_colors[0]
print(f"My most favorite color is: {first_color}")

# Add a new favorite color
favorite_colors.append("orange")
print(f"After adding orange: {favorite_colors}")

print("\n💡 Key learning: Lists hold multiple items in order!")

# EXAMPLE 2: Numbers List
print("\n2️⃣ EXAMPLE 2: Working with Numbers")
print("-" * 35)

# List of your test scores
test_scores = [85, 92, 78, 96, 88]
print(f"Test scores: {test_scores}")

# Find the highest score
highest_score = max(test_scores)
print(f"Highest score: {highest_score}")

# Add a new test score
test_scores.append(94)
print(f"After new test: {test_scores}")

# Calculate average (we'll learn more math later)
average = sum(test_scores) / len(test_scores)
print(f"Average score: {average:.1f}")

print("\n💡 Key learning: Lists work great with numbers too!")

# EXAMPLE 3: Mixed Lists
print("\n3️⃣ EXAMPLE 3: Mixed Types in Lists")
print("-" * 35)

# Information about a student
student_info = ["Alice", 16, "10th grade", True, 3.8]
print(f"Student info: {student_info}")

# Access different parts
name = student_info[0]
age = student_info[1]
grade = student_info[2]
honor_roll = student_info[3]
gpa = student_info[4]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Grade: {grade}")
print(f"Honor Roll: {honor_roll}")
print(f"GPA: {gpa}")

print("\n💡 Key learning: Lists can mix different types of data!")

# EXAMPLE 4: Building Lists Gradually
print("\n4️⃣ EXAMPLE 4: Building Lists Step by Step")
print("-" * 40)

# Start with empty list
grocery_list = []
print(f"Starting list: {grocery_list}")

# Add items one by one
print("\nBuilding grocery list...")
grocery_list.append("milk")
print(f"Added milk: {grocery_list}")

grocery_list.append("bread")
print(f"Added bread: {grocery_list}")

grocery_list.append("eggs")
print(f"Added eggs: {grocery_list}")

# Oops, forgot something important!
grocery_list.insert(0, "shopping bags")  # Add at the beginning
print(f"Added bags at start: {grocery_list}")

print("\n💡 Key learning: You can build lists gradually!")

# EXAMPLE 5: Removing Items
print("\n5️⃣ EXAMPLE 5: Removing Items")
print("-" * 30)

# List of weekend tasks
weekend_tasks = ["clean room", "do homework", "play games", "call grandma"]
print(f"Weekend tasks: {weekend_tasks}")

# Completed homework!
weekend_tasks.remove("do homework")
print(f"After doing homework: {weekend_tasks}")

# Changed mind about games, want to read instead
weekend_tasks[1] = "read book"  # Change "play games" to "read book"
print(f"Changed games to reading: {weekend_tasks}")

# Completed the first task
completed_task = weekend_tasks.pop(0)
print(f"Completed: {completed_task}")
print(f"Remaining tasks: {weekend_tasks}")

print("\n💡 Key learning: Lists are flexible - add, remove, change!")

# EXAMPLE 6: List Information
print("\n6️⃣ EXAMPLE 6: Getting List Information")
print("-" * 35)

# List of pets in the neighborhood
pets = ["dog", "cat", "dog", "fish", "bird", "cat", "hamster"]
print(f"Neighborhood pets: {pets}")

# How many pets total?
total_pets = len(pets)
print(f"Total pets: {total_pets}")

# How many dogs?
dog_count = pets.count("dog")
print(f"Number of dogs: {dog_count}")

# Where is the first cat?
first_cat_position = pets.index("cat")
print(f"First cat is at position: {first_cat_position}")

# Is there a rabbit?
has_rabbit = "rabbit" in pets
print(f"Is there a rabbit? {has_rabbit}")

print("\n💡 Key learning: Lists have useful methods for information!")

# EXAMPLE 7: Simple List Patterns
print("\n7️⃣ EXAMPLE 7: Common List Patterns")
print("-" * 35)

# Making a countdown
countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Countdown: {countdown}")

# Get last 3 numbers
last_three = countdown[-3:]
print(f"Last three: {last_three}")

# Get first half
first_half = countdown[:5]
print(f"First half: {first_half}")

# Reverse the countdown (make it count up!)
countdown.reverse()
print(f"Count up: {countdown}")

print("\n💡 Key learning: Slicing and methods make lists powerful!")

# MINI CHALLENGE
print("\n🏆 MINI CHALLENGE")
print("-" * 20)
print("Try to create a list of your 3 favorite foods,")
print("then add 2 more, then remove the first one.")
print("What does your final list look like?")

# Solution example:
print("\nExample solution:")
foods = ["pizza", "ice cream", "tacos"]
print(f"Started with: {foods}")
foods.append("sushi")
foods.append("chocolate")
print(f"After adding 2 more: {foods}")
foods.pop(0)  # Remove first item
print(f"After removing first: {foods}")

print("\n" + "=" * 40)
print("🎉 Great job! You understand lists now!")
print("Next: Let's build the shopping list manager!")
print("=" * 40)