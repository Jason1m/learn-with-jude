# Session 2: Quick Reference Guide - Lists

## 📋 Lists Quick Reference

### What is a List?
A list is a container that holds multiple items in order. Lists are:
- **Ordered**: Items have positions (indices)
- **Mutable**: Can be changed after creation
- **Allow duplicates**: Same item can appear multiple times
- **Mixed types**: Can contain different data types

### Creating Lists
```python
# Empty list
empty_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["John", 25, True, 3.14]
```

### Accessing Items (Indexing)
```python
fruits = ["apple", "banana", "orange", "grape"]

# Positive indexing (starts at 0)
first = fruits[0]        # "apple"
second = fruits[1]       # "banana"

# Negative indexing (starts from end)
last = fruits[-1]        # "grape"
second_last = fruits[-2] # "orange"

# Slicing (getting multiple items)
first_two = fruits[0:2]  # ["apple", "banana"]
last_two = fruits[2:]    # ["orange", "grape"]
all_but_last = fruits[:-1]  # ["apple", "banana", "orange"]
```

### Adding Items
```python
my_list = ["apple", "banana"]

# append() - adds to the end
my_list.append("orange")
# Result: ["apple", "banana", "orange"]

# insert() - adds at specific position
my_list.insert(1, "grape")
# Result: ["apple", "grape", "banana", "orange"]

# extend() - adds multiple items
my_list.extend(["kiwi", "mango"])
# Result: ["apple", "grape", "banana", "orange", "kiwi", "mango"]
```

### Removing Items
```python
my_list = ["red", "blue", "green", "yellow", "blue"]

# remove() - removes first occurrence of value
my_list.remove("blue")
# Result: ["red", "green", "yellow", "blue"]

# pop() - removes and returns item at index
item = my_list.pop(1)  # Returns "green"
# Result: ["red", "yellow", "blue"]

# pop() without index - removes last item
last = my_list.pop()   # Returns "blue"
# Result: ["red", "yellow"]

# del - removes item at index
del my_list[0]
# Result: ["yellow"]

# clear() - removes all items
my_list.clear()
# Result: []
```

### Changing Items
```python
colors = ["red", "blue", "green"]

# Change single item
colors[1] = "yellow"
# Result: ["red", "yellow", "green"]

# Change multiple items
colors[0:2] = ["orange", "purple"]
# Result: ["orange", "purple", "green"]
```

### List Information
```python
my_list = [1, 2, 3, 2, 4]

# Length
length = len(my_list)           # 5

# Count occurrences
count_2 = my_list.count(2)      # 2

# Find index of item
index_3 = my_list.index(3)      # 2

# Check if item exists
has_5 = 5 in my_list           # False
has_1 = 1 in my_list           # True
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5]

# Sort in ascending order
numbers.sort()
# Result: [1, 1, 3, 4, 5]

# Sort in descending order
numbers.sort(reverse=True)
# Result: [5, 4, 3, 1, 1]

# Reverse the order
numbers.reverse()
# Result: [1, 1, 3, 4, 5]

# Copy a list
new_list = numbers.copy()
```

### Mathematical Operations
```python
numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = sum(numbers)        # 15

# Find maximum
maximum = max(numbers)      # 5

# Find minimum
minimum = min(numbers)      # 1

# Average
average = sum(numbers) / len(numbers)  # 3.0
```

### Looping Through Lists
```python
fruits = ["apple", "banana", "orange"]

# Loop through items
for fruit in fruits:
    print(fruit)

# Loop with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Loop with enumerate (gets index and item)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Loop with enumerate starting from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
```

### Common Patterns
```python
# Build list from user input
my_list = []
for i in range(3):
    item = input(f"Enter item {i+1}: ")
    my_list.append(item)

# Filter list (keep only certain items)
numbers = [1, 2, 3, 4, 5]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Find all positions of an item
my_list = [1, 2, 3, 2, 4, 2]
positions = []
for i, item in enumerate(my_list):
    if item == 2:
        positions.append(i)
# positions = [1, 3, 5]
```

### Error Prevention
```python
my_list = ["a", "b", "c"]

# Safe indexing (avoid IndexError)
if 0 <= index < len(my_list):
    item = my_list[index]

# Safe removal (avoid ValueError)
if item in my_list:
    my_list.remove(item)

# Safe index finding
try:
    index = my_list.index("d")
except ValueError:
    print("Item not found")
```

### List Comparison
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

# Check if lists are equal
equal = list1 == list2      # True
different = list1 == list3  # False

# Check if lists have same items (any order)
same_items = sorted(list1) == sorted(list3)  # True
```

### Performance Tips
```python
# Efficient: append to end
my_list.append(item)

# Less efficient: insert at beginning
my_list.insert(0, item)

# Efficient: check membership
if item in my_list:

# Less efficient: loop to check
found = False
for x in my_list:
    if x == item:
        found = True
```

## 🚨 Common Mistakes

1. **Index out of range**
   ```python
   my_list = [1, 2, 3]
   # ERROR: my_list[3] - index 3 doesn't exist
   # FIX: my_list[2] or my_list[-1]
   ```

2. **remove() on non-existent item**
   ```python
   my_list = [1, 2, 3]
   # ERROR: my_list.remove(4) - 4 is not in list
   # FIX: Check first: if 4 in my_list: my_list.remove(4)
   ```

3. **Confusing remove() and pop()**
   ```python
   # remove() takes the VALUE
   my_list.remove("apple")
   
   # pop() takes the INDEX
   my_list.pop(0)
   ```

4. **Modifying list while iterating**
   ```python
   # WRONG: Don't modify list while looping
   for item in my_list:
       if condition:
           my_list.remove(item)  # Can cause issues
   
   # RIGHT: Loop backwards or create new list
   for i in range(len(my_list)-1, -1, -1):
       if condition:
           my_list.pop(i)
   ```

## 🎯 Quick Reminders

- Lists use **square brackets** `[]`
- Indexing starts at **0**
- Negative indices count from the **end**
- Lists are **mutable** (changeable)
- Use `append()` to add to **end**
- Use `insert()` to add at **specific position**
- Use `remove()` to delete by **value**
- Use `pop()` to delete by **index**
- Use `len()` to get **size**
- Use `in` to **check existence**

## 🚀 Next Steps

After mastering lists, you'll be ready for:
- **Dictionaries** (key-value pairs)
- **Tuples** (immutable lists)
- **Sets** (unique items only)
- **List comprehensions** (advanced list creation)
- **Nested lists** (lists inside lists)