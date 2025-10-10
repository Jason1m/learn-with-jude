# Session 6: Power with while Loops
# Detailed Explanation and Examples

print("=" * 60)
print("SESSION 6: POWER WITH WHILE LOOPS")
print("=" * 60)

# PART 1: INTRODUCTION TO WHILE LOOPS
print("\n1. INTRODUCTION TO WHILE LOOPS")
print("-" * 40)

print("For loops vs While loops:")
print("• For loops: 'Do this X times' or 'Do this for each item'")
print("• While loops: 'Keep doing this UNTIL something changes'")

print("\nReal-world while loop examples:")
print("• ATM: Keep showing menu until user selects 'Exit'")
print("• Game: Keep playing until player dies or quits")
print("• Security: Keep asking for password until correct")
print("• Monitoring: Keep checking system until error occurs")

print("\nWhile loop syntax:")
print("while condition:")
print("    # do something")
print("    # update condition (important!)")

# PART 2: YOUR FIRST WHILE LOOP
print("\n\n2. YOUR FIRST WHILE LOOP")
print("-" * 40)

print("Simple counting example:")

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Very important! Update the condition

print("Loop finished!")

print("\n" + "="*50)

# Comparison with for loop
print("Same task with for loop:")
for count in range(1, 6):
    print(f"Count: {count}")

print("\nBoth do the same thing, but while loop gives more control!")

# PART 3: INPUT VALIDATION WITH WHILE LOOPS
print("\n\n3. INPUT VALIDATION WITH WHILE LOOPS")
print("-" * 40)

print("While loops are perfect for input validation!")
print("Keep asking until the user gives valid input.")

def get_valid_age():
    """Get a valid age from user using while loop"""
    while True:  # Loop forever until we break out
        try:
            age = int(input("Enter your age (1-120): "))
            if 1 <= age <= 120:
                print(f"Thank you! Age {age} is valid.")
                return age
            else:
                print("❌ Age must be between 1 and 120. Try again.")
        except ValueError:
            print("❌ Please enter a valid number. Try again.")

print("Testing age validation:")
# Uncomment to test interactively:
# user_age = get_valid_age()

def get_yes_no_answer(question):
    """Get a yes/no answer from user"""
    while True:
        answer = input(f"{question} (y/n): ").lower().strip()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("❌ Please answer 'y' for yes or 'n' for no.")

print("\nTesting yes/no validation:")
# result = get_yes_no_answer("Do you like Python?")
# print(f"Your answer: {result}")

# PART 4: MENU-DRIVEN PROGRAMS
print("\n\n4. MENU-DRIVEN PROGRAMS")
print("-" * 40)

print("While loops are perfect for creating interactive menus!")

def simple_calculator():
    """Simple calculator with menu"""
    print("\n🧮 SIMPLE CALCULATOR")
    print("=" * 25)
    
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '5':
            print("👋 Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice! Please select 1-5.")
            continue
        
        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numbers!")
            continue
        
        # Perform calculation
        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                continue
            result = num1 / num2
            operation = "/"
        
        print(f"Result: {num1} {operation} {num2} = {result}")

print("Testing simple calculator:")
# Uncomment to test interactively:
# simple_calculator()

# PART 5: ENHANCED SHOPPING LIST MANAGER
print("\n\n5. ENHANCED SHOPPING LIST MANAGER")
print("-" * 40)

def enhanced_shopping_list():
    """Enhanced shopping list with while loop menu"""
    shopping_list = []
    
    print("\n🛒 ENHANCED SHOPPING LIST MANAGER")
    print("=" * 40)
    
    while True:
        # Display current list
        print(f"\nCurrent list ({len(shopping_list)} items):")
        if shopping_list:
            for i, item in enumerate(shopping_list, 1):
                print(f"  {i}. {item}")
        else:
            print("  (empty)")
        
        # Display menu
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Edit item")
        print("4. Clear all")
        print("5. Search items")
        print("6. Quit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == '1':
            # Add item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ Added '{item}' to list")
            else:
                print("❌ Cannot add empty item!")
        
        elif choice == '2':
            # Remove item
            if not shopping_list:
                print("❌ List is empty!")
                continue
            
            try:
                index = int(input("Enter item number to remove: ")) - 1
                if 0 <= index < len(shopping_list):
                    removed_item = shopping_list.pop(index)
                    print(f"✅ Removed '{removed_item}' from list")
                else:
                    print("❌ Invalid item number!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '3':
            # Edit item
            if not shopping_list:
                print("❌ List is empty!")
                continue
            
            try:
                index = int(input("Enter item number to edit: ")) - 1
                if 0 <= index < len(shopping_list):
                    old_item = shopping_list[index]
                    new_item = input(f"Enter new value for '{old_item}': ").strip()
                    if new_item:
                        shopping_list[index] = new_item
                        print(f"✅ Changed '{old_item}' to '{new_item}'")
                    else:
                        print("❌ Cannot use empty value!")
                else:
                    print("❌ Invalid item number!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '4':
            # Clear all
            if shopping_list:
                confirm = input("Are you sure you want to clear all items? (y/n): ")
                if confirm.lower() in ['y', 'yes']:
                    shopping_list.clear()
                    print("✅ All items cleared!")
                else:
                    print("❌ Clear cancelled.")
            else:
                print("❌ List is already empty!")
        
        elif choice == '5':
            # Search items
            if not shopping_list:
                print("❌ List is empty!")
                continue
            
            search_term = input("Enter search term: ").strip().lower()
            found_items = []
            
            for i, item in enumerate(shopping_list):
                if search_term in item.lower():
                    found_items.append((i + 1, item))
            
            if found_items:
                print(f"Found {len(found_items)} matching items:")
                for index, item in found_items:
                    print(f"  {index}. {item}")
            else:
                print("❌ No matching items found!")
        
        elif choice == '6':
            # Quit
            print(f"👋 Goodbye! Final list had {len(shopping_list)} items.")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-6.")

print("Testing enhanced shopping list:")
# Uncomment to test interactively:
# enhanced_shopping_list()

# PART 6: GAME LOOP EXAMPLE
print("\n\n6. GAME LOOP EXAMPLE")
print("-" * 40)

def number_guessing_game():
    """Number guessing game with while loop"""
    import random
    
    print("\n🎯 NUMBER GUESSING GAME")
    print("=" * 30)
    print("I'm thinking of a number between 1 and 100!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as attempt
            continue
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print(f"📈 Too low! {remaining} attempts remaining.")
        else:
            print(f"📉 Too high! {remaining} attempts remaining.")
        
        # Give hints
        if attempts == max_attempts // 2:
            if secret_number % 2 == 0:
                print("💡 Hint: The number is even!")
            else:
                print("💡 Hint: The number is odd!")
    
    else:
        # This runs if the while loop completes without breaking
        print(f"💀 Game over! The number was {secret_number}")
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        number_guessing_game()  # Recursive call to play again

print("Testing number guessing game:")
# Uncomment to test interactively:
# number_guessing_game()

# PART 7: ADVANCED WHILE LOOP PATTERNS
print("\n\n7. ADVANCED WHILE LOOP PATTERNS")
print("-" * 40)

def demonstrate_loop_controls():
    """Demonstrate break and continue statements"""
    
    print("Example 1: Using 'break' to exit early")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = 0
    
    while index < len(numbers):
        number = numbers[index]
        print(f"Processing: {number}")
        
        if number == 5:
            print("Found 5! Breaking out of loop.")
            break
        
        index += 1
    
    print("\nExample 2: Using 'continue' to skip iterations")
    index = 0
    
    while index < 10:
        index += 1  # Update counter first!
        
        if index % 2 == 0:  # Skip even numbers
            continue
        
        print(f"Odd number: {index}")

demonstrate_loop_controls()

# PART 8: INPUT VALIDATION PATTERNS
print("\n\n8. INPUT VALIDATION PATTERNS")
print("-" * 40)

def get_valid_email():
    """Get a valid email address"""
    while True:
        email = input("Enter your email address: ").strip()
        
        # Basic email validation
        if '@' not in email:
            print("❌ Email must contain @ symbol")
            continue
        
        if '.' not in email:
            print("❌ Email must contain a domain (e.g., .com)")
            continue
        
        if len(email) < 5:
            print("❌ Email too short")
            continue
        
        if email.count('@') != 1:
            print("❌ Email must contain exactly one @ symbol")
            continue
        
        print(f"✅ Email '{email}' is valid!")
        return email

def get_menu_choice(options):
    """Generic function to get a valid menu choice"""
    while True:
        print("\nAvailable options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input(f"\nEnter choice (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return choice - 1  # Return index
            else:
                print(f"❌ Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("❌ Please enter a valid number")

# Example usage
menu_options = ["View Profile", "Edit Settings", "View History", "Logout"]
print("Testing generic menu choice:")
# choice_index = get_menu_choice(menu_options)
# print(f"You selected: {menu_options[choice_index]}")

# PART 9: MONITORING AND AUTOMATION
print("\n\n9. MONITORING AND AUTOMATION EXAMPLE")
print("-" * 40)

def system_monitor_simulation():
    """Simulate a system monitoring loop"""
    import random
    import time
    
    print("🖥️  SYSTEM MONITOR SIMULATION")
    print("=" * 35)
    print("Monitoring system health... (Press Ctrl+C to stop)")
    
    check_count = 0
    error_count = 0
    
    try:
        while True:
            check_count += 1
            
            # Simulate system checks
            cpu_usage = random.randint(10, 95)
            memory_usage = random.randint(20, 90)
            disk_usage = random.randint(30, 85)
            
            print(f"\nCheck #{check_count}")
            print(f"CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}%")
            
            # Check for issues
            issues = []
            if cpu_usage > 90:
                issues.append("HIGH CPU")
            if memory_usage > 85:
                issues.append("HIGH MEMORY")
            if disk_usage > 80:
                issues.append("HIGH DISK")
            
            if issues:
                error_count += 1
                print(f"⚠️  ALERT: {', '.join(issues)}")
            else:
                print("✅ All systems normal")
            
            # Simulate waiting (normally would be longer)
            time.sleep(1)  # Wait 1 second
            
    except KeyboardInterrupt:
        print(f"\n\n📊 MONITORING SUMMARY")
        print(f"Total checks: {check_count}")
        print(f"Errors detected: {error_count}")
        print("Monitoring stopped by user.")

print("System monitor simulation:")
print("(This would run continuously - commented out for demo)")
# system_monitor_simulation()

# PART 10: COMMON PITFALLS AND DEBUGGING
print("\n\n10. COMMON PITFALLS AND DEBUGGING")
print("-" * 40)

print("❌ Common mistakes with while loops:")

print("\n1. Infinite loops (forgetting to update condition)")
print("# BAD:")
print("count = 0")
print("while count < 5:")
print("    print(count)")
print("    # Forgot: count += 1")

print("\n# GOOD:")
print("count = 0")
print("while count < 5:")
print("    print(count)")
print("    count += 1  # Always update!")

print("\n2. Wrong initial conditions")
print("# BAD:")
print("count = 5")
print("while count < 5:")  # Never executes!
print("    print(count)")

print("\n3. Updating in wrong place")
print("# BAD:")
print("while condition:")
print("    if something:")
print("        continue")
print("    update_condition()  # Might be skipped!")

print("\n# GOOD:")
print("while condition:")
print("    update_condition()  # Always executes")
print("    if something:")
print("        continue")

print("\n✅ Debugging tips:")
print("• Add print statements to see loop variables")
print("• Check your condition logic carefully")
print("• Make sure you can always exit the loop")
print("• Test with simple examples first")
print("• Use a debugger or step through manually")

print("\n" + "="*60)
print("🎉 CONGRATULATIONS!")
print("You now understand the power of while loops!")
print("Key concepts mastered:")
print("• Condition-based iteration")
print("• Menu-driven programs")
print("• Input validation")
print("• Interactive applications")
print("• Loop control and debugging")
print("="*60)