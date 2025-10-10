# Session 5: Automation with for Loops
# Detailed Explanation and Examples

print("=" * 60)
print("SESSION 5: AUTOMATION WITH FOR LOOPS")
print("=" * 60)

# PART 1: INTRODUCTION TO AUTOMATION
print("\n1. INTRODUCTION TO AUTOMATION")
print("-" * 40)

print("In real life, we often repeat the same task:")
print("• Checking each item on a shopping list")
print("• Grading each student's test")
print("• Sending the same email to multiple people")
print("• Processing each file in a folder")

print("\nComputers are PERFECT for repetitive tasks!")
print("Instead of writing the same code over and over...")
print("We use LOOPS to automate the repetition!")

# PART 2: YOUR FIRST FOR LOOP
print("\n\n2. YOUR FIRST FOR LOOP")
print("-" * 40)

print("Basic for loop syntax:")
print("for item in collection:")
print("    # do something with item")

print("\nLet's try a simple example:")

# Simple list iteration
fruits = ["apple", "banana", "orange", "grape"]
print(f"Our fruit list: {fruits}")

print("\nWithout a loop (tedious!):")
print(fruits[0])
print(fruits[1]) 
print(fruits[2])
print(fruits[3])

print("\nWith a for loop (elegant!):")
for fruit in fruits:
    print(fruit)

print("\n" + "="*50)

# Another example with actions
print("\nLet's do something with each fruit:")
for fruit in fruits:
    print(f"I love eating {fruit}!")

print("\nWe can use any variable name:")
for snack in fruits:
    print(f"🍎 {snack} is delicious!")

# PART 3: THE RANGE FUNCTION
print("\n\n3. THE RANGE FUNCTION")
print("-" * 40)

print("Sometimes you want to repeat something a specific number of times.")
print("The range() function creates a sequence of numbers.")

print("\nrange(5) creates: 0, 1, 2, 3, 4")
print("Let's see it in action:")

for number in range(5):
    print(f"Count: {number}")

print("\nOther range patterns:")

print("\nrange(1, 6) - from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nrange(0, 10, 2) - every 2nd number:")
for i in range(0, 10, 2):
    print(f"Even: {i}")

print("\nrange(10, 0, -1) - countdown:")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")
print("Blast off! 🚀")

# PART 4: LOOPS WITH CONDITIONS
print("\n\n4. LOOPS WITH CONDITIONS")
print("-" * 40)

print("You can combine loops with if statements for powerful automation!")

# Filter data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original numbers: {numbers}")

print("\nEven numbers only:")
for num in numbers:
    if num % 2 == 0:
        print(f"Even: {num}")

print("\nNumbers greater than 5:")
for num in numbers:
    if num > 5:
        print(f"Big number: {num}")

# Multiple conditions
print("\nNumbers that are even AND greater than 5:")
for num in numbers:
    if num % 2 == 0 and num > 5:
        print(f"Even and big: {num}")

# PART 5: ACCUMULATING RESULTS
print("\n\n5. ACCUMULATING RESULTS")
print("-" * 40)

print("Loops are great for building up totals or collecting results!")

# Calculate total
prices = [12.99, 8.50, 23.75, 15.20, 7.99]
print(f"Prices: {prices}")

total = 0
for price in prices:
    total = total + price  # or total += price
    print(f"Adding ${price:.2f}, running total: ${total:.2f}")

print(f"Final total: ${total:.2f}")

print("\n" + "="*50)

# Count specific items
words = ["apple", "banana", "apricot", "grape", "avocado"]
print(f"Words: {words}")

a_words = 0
for word in words:
    if word.startswith("a"):
        a_words += 1
        print(f"Found 'a' word: {word}")

print(f"Total words starting with 'a': {a_words}")

# Collect results in a new list
print("\nCreating a new list with uppercase words:")
uppercase_words = []
for word in words:
    uppercase_word = word.upper()
    uppercase_words.append(uppercase_word)
    print(f"{word} → {uppercase_word}")

print(f"New list: {uppercase_words}")

# PART 6: PROCESSING REAL DATA
print("\n\n6. PROCESSING REAL DATA")
print("-" * 40)

print("Let's process some realistic data!")

# Student grades
students_grades = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 87},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95},
    {"name": "Eve", "grade": 83}
]

print("Student Grade Report")
print("-" * 20)

total_score = 0
honor_students = []

for student in students_grades:
    name = student["name"]
    grade = student["grade"]
    
    # Add to total
    total_score += grade
    
    # Check for honors
    if grade >= 90:
        honor_students.append(name)
        status = "🌟 Honor Roll"
    elif grade >= 80:
        status = "✅ Good Standing"
    else:
        status = "⚠️  Needs Improvement"
    
    print(f"{name}: {grade}% {status}")

# Calculate and display summary
average = total_score / len(students_grades)
print(f"\nClass Summary:")
print(f"Average Grade: {average:.1f}%")
print(f"Honor Roll Students: {', '.join(honor_students)}")

# PART 7: INVENTORY PROCESSING
print("\n\n7. INVENTORY PROCESSING EXAMPLE")
print("-" * 40)

inventory = [
    {"item": "Laptop", "quantity": 5, "price": 999.99},
    {"item": "Mouse", "quantity": 25, "price": 29.99},
    {"item": "Keyboard", "quantity": 15, "price": 79.99},
    {"item": "Monitor", "quantity": 3, "price": 299.99},
    {"item": "Headphones", "quantity": 12, "price": 149.99}
]

print("📦 INVENTORY REPORT")
print("=" * 30)

total_value = 0
low_stock_items = []
expensive_items = []

for product in inventory:
    item_name = product["item"]
    qty = product["quantity"]
    price = product["price"]
    
    # Calculate item value
    item_value = qty * price
    total_value += item_value
    
    # Check for low stock
    if qty < 10:
        low_stock_items.append(item_name)
    
    # Check for expensive items
    if price > 100:
        expensive_items.append(item_name)
    
    # Display item info
    print(f"{item_name:<12}: {qty:>3} units × ${price:>7.2f} = ${item_value:>8.2f}")

print("-" * 30)
print(f"Total Inventory Value: ${total_value:,.2f}")

if low_stock_items:
    print(f"⚠️  Low Stock Alert: {', '.join(low_stock_items)}")

print(f"💰 High-Value Items: {', '.join(expensive_items)}")

# PART 8: NESTED LOOPS
print("\n\n8. NESTED LOOPS")
print("-" * 40)

print("Sometimes you need loops inside loops!")
print("Example: Multiplication table")

print("\nSimple multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i} × {j} = {result:2d}", end="  ")
    print()  # New line after each row

print("\n" + "="*50)

# Processing 2D data
departments = [
    {"name": "Sales", "employees": ["Alice", "Bob", "Charlie"]},
    {"name": "Engineering", "employees": ["Diana", "Eve", "Frank"]},
    {"name": "Marketing", "employees": ["Grace", "Henry"]}
]

print("Company Directory:")
for dept in departments:
    dept_name = dept["name"]
    employees = dept["employees"]
    
    print(f"\n{dept_name} Department:")
    for employee in employees:
        print(f"  • {employee}")

# PART 9: COMMON PATTERNS & BEST PRACTICES
print("\n\n9. COMMON PATTERNS & BEST PRACTICES")
print("-" * 40)

print("✅ Good practices:")
print("• Use descriptive variable names")
print("• Keep loop bodies simple")
print("• Use early filtering with if statements")
print("• Break complex loops into smaller functions")

print("\n❌ Common mistakes to avoid:")
print("• Don't modify a list while iterating over it")
print("• Don't use loop variables after the loop ends")
print("• Avoid deeply nested loops when possible")

# Example of descriptive naming
print("\nExample - Good variable naming:")
email_addresses = ["alice@email.com", "bob@email.com", "charlie@email.com"]

for email_address in email_addresses:  # Clear what we're processing
    if "@gmail.com" in email_address:
        print(f"Gmail user: {email_address}")

# PART 10: PERFORMANCE EXAMPLE
print("\n\n10. THE POWER OF AUTOMATION")
print("-" * 40)

print("Let's see how powerful loops can be!")

# Simulate processing a large dataset
import time

large_dataset = list(range(1000))  # 1000 numbers
print(f"Processing {len(large_dataset)} items...")

start_time = time.time()

processed_count = 0
for number in large_dataset:
    # Simulate some processing
    if number % 2 == 0:
        processed_count += 1

end_time = time.time()
processing_time = end_time - start_time

print(f"✅ Processed {len(large_dataset)} items in {processing_time:.4f} seconds")
print(f"Found {processed_count} even numbers")
print("Imagine doing this manually! 🤯")

print("\n" + "="*60)
print("🎉 CONGRATULATIONS!")
print("You now know how to automate repetitive tasks with for loops!")
print("This is one of the most powerful programming concepts!")
print("Practice with the exercises to master automation!")
print("="*60)