# # 01_variables_and_input.py
# # This script shows how variables and input work in Python

# ===== VARIABLES =====
# Variables are containers for storing data values
# Think of them like labeled boxes where you can store information

# Creating a variable is simple - just use a name and the = sign
name = "Jude"  # This creates a text (string) variable
age = 25       # This creates a number (integer) variable
height = 1.75  # This creates a decimal (float) variable

# We can print the values of variables using print()
print("===== VARIABLES DEMO =====")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print()  # This prints an empty line for better readability

# # We can also change the value of a variable
# name = "Alex"
# print("New name:", name)
# print()

# ===== USER INPUT =====
# # The input() function allows us to get information from the user
# print("===== INPUT DEMO =====")
# user_name = input("What is your name? ")  # The text in quotes is the prompt shown to the user
# print("Hello,", user_name + "!")  # We can use the input in our program

# # We can also convert input to different types
# # By default, input() gives us text (string), even if the user types numbers
# user_age_text = input("How old are you? ")
# user_age = int(user_age_text)  # Convert the text to an integer number
# years_to_100 = 100 - user_age  # Now we can do math with it
# print(f"You will be 100 in {years_to_100} years!")

# # The f"..." format is a modern way to put variables inside text
# # It's called an "f-string" (formatted string)

# ===== CHALLENGE FOR STUDENTS =====
# Try adding a new variable and getting more input from the user!
# For example, ask for their favorite color and print a personalized message.
