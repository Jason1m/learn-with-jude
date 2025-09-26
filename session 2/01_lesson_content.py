# Session 2: The List (Your First Container)
# Detailed Explanation and Examples

print("=" * 50)
print("SESSION 2: THE LIST (YOUR FIRST CONTAINER)")
print("=" * 50)

# PART 1: WHAT IS A LIST?
print("\n1. WHAT IS A LIST?")
print("-" * 20)

# A list is like a container that can hold multiple items
# Think of it like a shopping list, a to-do list, or a box of items

# Real-world analogy
print("Real-world analogy:")
print("A list is like a shopping list on paper:")
print("1. Milk")
print("2. Bread") 
print("3. Eggs")
print("4. Apples")

print("\nIn Python, this would look like:")
shopping_list = ["Milk", "Bread", "Eggs", "Apples"]
print(f"shopping_list = {shopping_list}")

print("\nKey characteristics of lists:")
print("✓ Can hold multiple items")
print("✓ Items are ordered (they have positions)")
print("✓ Items can be different types")
print("✓ Lists are changeable (mutable)")

# PART 2: CREATING LISTS
print("\n\n2. CREATING LISTS")
print("-" * 20)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with strings
fruits = ["apple", "banana", "orange", "grape"]
print(f"Fruits list: {fruits}")

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers list: {numbers}")

# List with mixed types
mixed_list = ["John", 25, True, 3.14, "Python"]
print(f"Mixed list: {mixed_list}")

# List with repeated items (this is allowed!)
colors = ["red", "blue", "red", "green", "blue"]
print(f"Colors list: {colors}")

# PART 3: ACCESSING ITEMS (INDEXING)
print("\n\n3. ACCESSING ITEMS")
print("-" * 20)

# Lists use indexing starting from 0
print(f"Our fruits list: {fruits}")
print("\nIndexing (position numbers):")
print("Index:  0       1        2        3")
print(f"Items: {fruits}")

print("\nAccessing individual items:")
print(f"First fruit (index 0): {fruits[0]}")
print(f"Second fruit (index 1): {fruits[1]}")
print(f"Third fruit (index 2): {fruits[2]}")
print(f"Fourth fruit (index 3): {fruits[3]}")

# Negative indexing (counting from the end)
print("\nNegative indexing (counting from the end):")
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second to last (index -2): {fruits[-2]}")

# What happens if we try to access an index that doesn't exist?
print("\nBe careful with index errors!")
print("fruits[4] would cause an error because index 4 doesn't exist")
print("(Our list only has indices 0, 1, 2, 3)")

# PART 4: SLICING (GETTING MULTIPLE ITEMS)
print("\n\n4. SLICING")
print("-" * 20)

print(f"Our fruits list: {fruits}")
print("\nSlicing examples:")
print(f"First two fruits: {fruits[0:2]}")  # Gets index 0 and 1
print(f"Last two fruits: {fruits[2:4]}")   # Gets index 2 and 3
print(f"Everything except first: {fruits[1:]}")  # From index 1 to end
print(f"Everything except last: {fruits[:-1]}")  # From start to second-to-last

# PART 5: ADDING ITEMS TO LISTS
print("\n\n5. ADDING ITEMS TO LISTS")
print("-" * 20)

# Start with a fresh list
my_list = ["apple", "banana"]
print(f"Starting list: {my_list}")

# Method 1: append() - adds to the end
my_list.append("orange")
print(f"After append('orange'): {my_list}")

my_list.append("grape")
print(f"After append('grape'): {my_list}")

# Method 2: insert() - adds at a specific position
my_list.insert(1, "mango")  # Insert "mango" at index 1
print(f"After insert(1, 'mango'): {my_list}")

my_list.insert(0, "kiwi")   # Insert "kiwi" at the beginning
print(f"After insert(0, 'kiwi'): {my_list}")

# Method 3: extend() - adds multiple items
more_fruits = ["pear", "peach"]
my_list.extend(more_fruits)
print(f"After extend(['pear', 'peach']): {my_list}")

# PART 6: REMOVING ITEMS FROM LISTS
print("\n\n6. REMOVING ITEMS FROM LISTS")
print("-" * 20)

# Create a test list
test_list = ["red", "blue", "green", "yellow", "blue"]
print(f"Starting list: {test_list}")

# Method 1: remove() - removes the first occurrence of a value
test_list.remove("blue")  # Removes the first "blue"
print(f"After remove('blue'): {test_list}")

# Method 2: pop() - removes item at specific index and returns it
removed_item = test_list.pop(1)  # Remove item at index 1
print(f"After pop(1): {test_list}")
print(f"Removed item was: {removed_item}")

# pop() without index removes the last item
last_item = test_list.pop()
print(f"After pop(): {test_list}")
print(f"Last item was: {last_item}")

# Method 3: del - removes item at specific index
del test_list[0]  # Remove first item
print(f"After del test_list[0]: {test_list}")

# PART 7: CHANGING ITEMS IN LISTS
print("\n\n7. CHANGING ITEMS IN LISTS")
print("-" * 20)

# Create a test list
change_list = ["Monday", "Tuesday", "Wednesday"]
print(f"Original list: {change_list}")

# Change a single item
change_list[1] = "TUESDAY"
print(f"After changing index 1: {change_list}")

# Change multiple items using slicing
change_list[0:2] = ["MON", "TUE"]
print(f"After changing indices 0-1: {change_list}")

# PART 8: USEFUL LIST METHODS
print("\n\n8. USEFUL LIST METHODS")
print("-" * 20)

demo_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Demo list: {demo_list}")

# Length of list
print(f"Length: {len(demo_list)}")

# Count occurrences
print(f"Count of 1: {demo_list.count(1)}")

# Find index of item
print(f"Index of 4: {demo_list.index(4)}")

# Sort the list
demo_list.sort()
print(f"After sort(): {demo_list}")

# Reverse the list
demo_list.reverse()
print(f"After reverse(): {demo_list}")

# Check if item exists
print(f"Is 5 in the list? {5 in demo_list}")
print(f"Is 10 in the list? {10 in demo_list}")

# PART 9: COMMON PATTERNS
print("\n\n9. COMMON PATTERNS")
print("-" * 20)

# Looping through a list
colors = ["red", "green", "blue"]
print("Looping through colors:")
for color in colors:
    print(f"  - {color}")

# Looping with index
print("\nLooping with index:")
for i in range(len(colors)):
    print(f"  {i}: {colors[i]}")

# Building a list dynamically
print("\nBuilding a list from user input simulation:")
user_list = []
simulated_inputs = ["apple", "banana", "orange"]
for item in simulated_inputs:
    user_list.append(item)
    print(f"Added {item}, list is now: {user_list}")

print("\n" + "=" * 50)
print("END OF LESSON CONTENT")
print("Next: We'll build a shopping list manager!")
print("=" * 50)