# Session 2: Practice Exercise Solutions
# Check your answers against these solutions

print("✅ LIST EXERCISE SOLUTIONS")
print("=" * 40)
print("Compare your solutions with these!")
print("Remember: There might be multiple correct ways!")
print("=" * 40)

# SOLUTION 1: Basic List Creation
print("\n🔥 SOLUTION 1: Create Your Lists")
print("-" * 35)

# Example answers (yours might be different!)
movies = ["Spider-Man", "Avatar", "Frozen", "Toy Story"]
numbers = [1, 2, 3, 4, 5]
my_list = []

print(f"movies = {movies}")
print(f"numbers = {numbers}")
print(f"my_list = {my_list}")

print("\n✅ Key points:")
print("• Movies can be any 4 films you like")
print("• Numbers should be exactly [1, 2, 3, 4, 5]")
print("• Empty list uses just []")

# SOLUTION 2: Accessing Items
print("\n\n🔥 SOLUTION 2: Access List Items")
print("-" * 35)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"fruits = {fruits}")

first_fruit = fruits[0]
last_fruit = fruits[-1]  # or fruits[4]
middle_fruit = fruits[2]
second_and_third = fruits[1:3]

print(f"first_fruit = {first_fruit}")
print(f"last_fruit = {last_fruit}")
print(f"middle_fruit = {middle_fruit}")
print(f"second_and_third = {second_and_third}")

print("\n✅ Key points:")
print("• First item is always index 0")
print("• Last item can be index -1 or len(list)-1")
print("• Slicing [1:3] gets items at index 1 and 2 (not 3)")

# SOLUTION 3: Adding Items
print("\n\n🔥 SOLUTION 3: Add Items to Lists")
print("-" * 35)

colors = ["red", "blue"]
print(f"Starting colors = {colors}")

# Step by step
colors.append("green")
print(f"After append('green'): {colors}")

colors.insert(0, "yellow")
print(f"After insert(0, 'yellow'): {colors}")

# Find where to insert purple (between blue and green)
# After yellow was inserted: ["yellow", "red", "blue", "green"]
# Blue is now at index 2, so insert at index 3
colors.insert(3, "purple")
print(f"After insert(3, 'purple'): {colors}")

print("\n✅ Key points:")
print("• append() always adds to the end")
print("• insert(0, item) adds to the beginning")
print("• Be careful with positions when inserting multiple items!")

# SOLUTION 4: Removing Items
print("\n\n🔥 SOLUTION 4: Remove Items from Lists")
print("-" * 35)

animals = ["cat", "dog", "fish", "bird", "cat", "hamster"]
print(f"Starting animals = {animals}")

animals.remove("cat")  # Removes first "cat"
print(f"After remove('cat'): {animals}")

animals.pop(2)  # Remove item at index 2
print(f"After pop(2): {animals}")

animals.pop()  # Remove last item
print(f"After pop(): {animals}")

print("\n✅ Key points:")
print("• remove() deletes by value (first occurrence)")
print("• pop(index) deletes by position")
print("• pop() without index removes the last item")

# SOLUTION 5: List Information
print("\n\n🔥 SOLUTION 5: Get List Information")
print("-" * 35)

grades = [85, 92, 78, 85, 96, 88, 85]
print(f"grades = {grades}")

length = len(grades)
count_85 = grades.count(85)
position_96 = grades.index(96)
has_100 = 100 in grades

print(f"length = {length}")
print(f"count_85 = {count_85}")
print(f"position_96 = {position_96}")
print(f"has_100 = {has_100}")

print("\n✅ Key points:")
print("• len() gives the number of items")
print("• count() counts occurrences of a value")
print("• index() finds the position of first occurrence")
print("• 'in' checks if a value exists (returns True/False)")

# SOLUTION 6: Mini Shopping List
print("\n\n🔥 SOLUTION 6: Mini Shopping List")
print("-" * 35)

shopping = []
print(f"1. Starting list: {shopping}")

# Add items
shopping.append("bread")
shopping.append("milk")
shopping.append("eggs")
print(f"2. After adding items: {shopping}")

# Print with nice format
print("3. Shopping list:")
for i, item in enumerate(shopping, 1):
    print(f"   {i}. {item}")

# Remove milk
shopping.remove("milk")
print(f"4. After removing milk: {shopping}")

# Add cheese at beginning
shopping.insert(0, "cheese")
print(f"5. After adding cheese at start: {shopping}")

print("6. Final shopping list:")
for i, item in enumerate(shopping, 1):
    print(f"   {i}. {item}")

print("\n✅ Key points:")
print("• enumerate() helps with numbering items")
print("• insert(0, item) adds to the beginning")
print("• Nice formatting makes output more readable")

# SOLUTION 7: List Math
print("\n\n🔥 SOLUTION 7: Math with Lists")
print("-" * 35)

scores = [78, 85, 92, 88, 95]
print(f"scores = {scores}")

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

print(f"highest = {highest}")
print(f"lowest = {lowest}")
print(f"total = {total}")
print(f"average = {average}")

print("\n✅ Key points:")
print("• max() and min() work great with number lists")
print("• sum() adds all numbers in a list")
print("• Average = sum ÷ count")

# SOLUTION 8: List Sorting
print("\n\n🔥 SOLUTION 8: Sorting Lists")
print("-" * 35)

names = ["Charlie", "Alice", "Bob", "Diana"]
print(f"Original names = {names}")

names.sort()
print(f"After sort(): {names}")

names.reverse()
print(f"After reverse(): {names}")

print("\n✅ Key points:")
print("• sort() arranges items alphabetically")
print("• reverse() flips the order")
print("• These methods change the original list")

# CHALLENGE SOLUTION: Advanced Shopping List
print("\n\n🏆 CHALLENGE SOLUTION: Advanced Shopping List")
print("-" * 50)

# Step by step solution
shopping_advanced = ['apples', 'bread', 'milk']
print(f"1. Starting list: {shopping_advanced}")

# Add items
shopping_advanced.append('cheese')
shopping_advanced.append('eggs')
print(f"2. After adding cheese and eggs: {shopping_advanced}")

# Remove bread
shopping_advanced.remove('bread')
print(f"3. After removing bread: {shopping_advanced}")

# Check if milk is in list
milk_present = 'milk' in shopping_advanced
print(f"4. Is milk in the list? {milk_present}")

# Count total items
total_items = len(shopping_advanced)
print(f"5. Total items: {total_items}")

# Sort alphabetically
shopping_advanced.sort()
print(f"6. After sorting: {shopping_advanced}")

# Print each item with position
print("7. Final list with positions:")
for i, item in enumerate(shopping_advanced, 1):
    print(f"   {i}. {item}")

# BONUS SOLUTION: List Detective
print("\n\n🌟 BONUS SOLUTION: List Detective")
print("-" * 40)

mystery_list = [5, 3, 8, 3, 1, 8, 2, 3]
print(f"Original mystery_list = {mystery_list}")

# 1. How many items?
item_count = len(mystery_list)
print(f"1. Number of items: {item_count}")

# 2. Most common number
# Count each number
count_dict = {}
for num in mystery_list:
    count_dict[num] = mystery_list.count(num)
most_common = max(count_dict, key=count_dict.get)
print(f"2. Most common number: {most_common} (appears {count_dict[most_common]} times)")

# 3. Sum of all numbers
total_sum = sum(mystery_list)
print(f"3. Sum of all numbers: {total_sum}")

# 4. Remove all occurrences of 3
# Make a copy first to show the process
mystery_copy = mystery_list.copy()
while 3 in mystery_copy:
    mystery_copy.remove(3)
print(f"4. After removing all 3's: {mystery_copy}")

# 5. Sort the remaining numbers
mystery_copy.sort()
print(f"5. After sorting: {mystery_copy}")

print("\n✅ Detective insights:")
print("• The number 3 appeared most frequently")
print("• Use while loop to remove all occurrences")
print("• copy() creates a duplicate to preserve original")

# SUMMARY
print("\n" + "=" * 50)
print("🎉 CONGRATULATIONS!")
print("You've completed all the list exercises!")
print("\n📚 What you've learned:")
print("• Creating lists with []")
print("• Accessing items with indexing")
print("• Adding items with append() and insert()")
print("• Removing items with remove() and pop()")
print("• Getting information with len(), count(), index()")
print("• Using 'in' to check if items exist")
print("• Sorting and reversing lists")
print("• Working with lists in loops")

print("\n🚀 Next steps:")
print("• Practice building your own list programs")
print("• Try the shopping list manager")
print("• Experiment with different list methods")
print("• Get ready for Session 3!")

print("=" * 50)