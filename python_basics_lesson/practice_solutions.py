# Python Basics - Practice Exercises (SOLUTIONS)

# ===== EXERCISE 1: VARIABLES AND INPUT =====
# Create a script that calculates the area of a rectangle

def exercise1_solution():
    print("\n===== EXERCISE 1: RECTANGLE AREA CALCULATOR =====")
    # Ask for dimensions and convert to float
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    
    # Calculate the area
    area = width * height
    
    # Print the result
    print(f"The area of a rectangle with width {width} and height {height} is: {area}")
    print()


# ===== EXERCISE 2: SIMPLE CALCULATOR =====
# Create a basic calculator

def exercise2_solution():
    print("\n===== EXERCISE 2: SIMPLE CALCULATOR =====")
    # Get the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Ask for the operation
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1-4): ")
    
    # Perform calculation based on choice
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
        # Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2
        operation = "/"
    else:
        print("Invalid choice!")
        return
    
    # Show the result
    print(f"\n{num1} {operation} {num2} = {result}")
    print()


# ===== EXERCISE 3: TEMPERATURE CONVERTER =====
# Create a script that converts Celsius to Fahrenheit

def exercise3_solution():
    print("\n===== EXERCISE 3: TEMPERATURE CONVERTER =====")
    # Get temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Display the result
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    print()


# ===== EXERCISE 4: SHOPPING LIST =====
# Create a script for a shopping list

def exercise4_solution():
    print("\n===== EXERCISE 4: SHOPPING LIST =====")
    shopping_list = []
    
    print("Enter items for your shopping list (type 'done' when finished):")
    
    # Keep asking for items until user says "done"
    while True:
        item = input("Add item: ")
        if item.lower() == "done":
            break
        shopping_list.append(item)
    
    # Write the shopping list to a file
    with open("shopping_list.txt", "w") as file:
        for item in shopping_list:
            file.write(item + "\n")
    
    print("\nShopping list saved to 'shopping_list.txt'")
    
    # Read back the list
    print("\nYour shopping list:")
    with open("shopping_list.txt", "r") as file:
        for line in file:
            print(f"- {line.strip()}")
    print()


# ===== EXERCISE 5: GUESSING GAME =====
# Create a number guessing game

def exercise5_solution():
    import random
    
    print("\n===== EXERCISE 5: GUESSING GAME =====")
    print("I'm thinking of a number between 1 and 20...")
    
    # Generate a random number
    secret_number = random.randint(1, 20)
    
    # Initialize counter
    guesses = 0
    
    # Keep looping until they guess correctly
    while True:
        # Get the user's guess
        guess = int(input("Your guess: "))
        guesses += 1
        
        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guesses} tries!")
            break
    
    print()


# ===== CHALLENGE: CUSTOM FILE ORGANIZER =====
"""
# Modified organizer.py with a new category for code files

import os
import shutil

def organize_files():
    # Get the current directory
    current_dir = os.getcwd()
    print(f"Organizing files in: {current_dir}")
    
    # Define what files go where
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp'],  # New category
    }
    
    # Get all files
    all_files = os.listdir(current_dir)
    
    # Organize each file
    for filename in all_files:
        # Skip this script and folders
        if filename in ["organizer.py", "my_organizer.py"] or os.path.isdir(filename):
            continue
            
        # Get file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find category
        found_category = 'Others'
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                found_category = category
                break

        # Create category folder if needed
        category_path = os.path.join(current_dir, found_category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created new folder: {found_category}")

        # Move the file
        old_path = os.path.join(current_dir, filename)
        new_path = os.path.join(category_path, filename)
        
        shutil.move(old_path, new_path)
        print(f"Moved: {filename} -> {found_category}/")

    print("✅ All files organized!")

if __name__ == "__main__":
    print("🚀 Starting File Organizer...")
    organize_files()
"""

# Run the solutions if this file is executed directly
if __name__ == "__main__":
    print("===== PRACTICE EXERCISE SOLUTIONS =====")
    print("This file contains solutions for the practice exercises.")
    print("Run each solution individually or all solutions together.")
    
    while True:
        print("\nChoose an exercise to run:")
        print("1. Rectangle Area Calculator")
        print("2. Simple Calculator")
        print("3. Temperature Converter")
        print("4. Shopping List")
        print("5. Guessing Game")
        print("6. Run All Exercises")
        print("0. Exit")
        
        choice = input("\nYour choice: ")
        
        if choice == '1':
            exercise1_solution()
        elif choice == '2':
            exercise2_solution()
        elif choice == '3':
            exercise3_solution()
        elif choice == '4':
            exercise4_solution()
        elif choice == '5':
            exercise5_solution()
        elif choice == '6':
            exercise1_solution()
            exercise2_solution()
            exercise3_solution()
            exercise4_solution()
            exercise5_solution()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
