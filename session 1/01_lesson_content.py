"""
Session 1: Talking to Python - Main Lesson Content
==================================================

This file contains the core lesson content with explanations, examples, and 
progressive exercises. Use this as your main teaching resource.

For Instructors: 
- Encourage students to type along rather than just watching
- Pause frequently to check understanding
- Let students experiment and make mistakes - that's how they learn!
"""

# =============================================================================
# SECTION 1: INTRODUCTION TO PYTHON AND PRINT()
# =============================================================================

print("=" * 50)
print("WELCOME TO PYTHON PROGRAMMING!")
print("=" * 50)

"""
INSTRUCTOR NOTE: Start here! This is students' first Python code.

WHAT IS PYTHON?
- Python is a programming language (like English, but for computers)
- We "talk" to Python by writing instructions
- Python reads our instructions from top to bottom, like reading a book

THE print() FUNCTION:
- print() is like Python's mouth - it displays things on the screen
- Anything inside the parentheses () gets displayed
- Text (strings) must be in quotes: "like this" or 'like this'
"""

# Let's start with the most famous programming greeting:
print("Hello, World!")

# We can print multiple things:
print("Python is fun!")
print("I am learning to code!")
print("This is exciting!")

"""
INSTRUCTOR DEMO: Have students type these examples and run them.
Ask: "What do you notice about the quotes?"
"""

# We can print numbers without quotes:
print(42)
print(100)
print(2024)

# We can print calculations:
print(5 + 3)
print(10 - 4)
print(7 * 2)

"""
KEY CONCEPT: Quotes vs No Quotes
- Text (strings) need quotes: "Hello"
- Numbers don't need quotes: 42
- If you put quotes around numbers, they become text: "42"
"""

# Examples to demonstrate:
print("This is text")    # Text - needs quotes
print(123)              # Number - no quotes needed
print("123")            # Text that looks like a number - needs quotes

# We can print empty lines for spacing:
print()  # This prints a blank line
print("Now there's a space above this line!")

"""
STUDENT EXERCISE 1: Your Turn!
Try these on your own:
1. Print your name
2. Print your favorite number
3. Print a message about why you want to learn Python
"""

# =============================================================================
# SECTION 2: GETTING INPUT FROM USERS WITH input()
# =============================================================================

print("\n" + "=" * 50)
print("SECTION 2: TALKING WITH USERS")
print("=" * 50)

"""
INSTRUCTOR NOTE: This is where programming becomes interactive!

THE input() FUNCTION:
- input() is like Python's ears - it listens for user input
- It pauses the program and waits for the user to type something
- The user presses Enter when they're done typing
- We usually store what the user types in a variable (coming up next!)
"""

# Basic input - but this doesn't save what the user types:
# input("What's your name? ")  # Try this, but we lose the answer!

# To save the user's answer, we need VARIABLES!

# =============================================================================
# SECTION 3: VARIABLES - STORING INFORMATION
# =============================================================================

print("\n" + "=" * 50)
print("SECTION 3: VARIABLES - PYTHON'S MEMORY")
print("=" * 50)

"""
WHAT ARE VARIABLES?
- Variables are like labeled boxes where we store information
- We can put things in the box and take them out later
- The label is the variable name, the contents is the data

CREATING VARIABLES:
- Use the = sign to put something in a variable
- Format: variable_name = value
- Variable names should be descriptive and use underscores for spaces
"""

# Creating variables with different types of data:
student_name = "Alice"        # String (text) variable
student_age = 16             # Number (integer) variable
favorite_subject = "Math"    # Another string variable
height = 5.4                 # Float (decimal) variable

# Now we can use these variables:
print("Student name:", student_name)
print("Student age:", student_age)
print("Favorite subject:", favorite_subject)
print("Height:", height)

"""
VARIABLE NAMING RULES:
✓ Use letters, numbers, and underscores
✓ Start with a letter or underscore
✓ Use descriptive names: 'student_name' not 'sn'
✓ Use lowercase with underscores: 'first_name'

✗ No spaces: 'first name' (wrong)
✗ No special characters: 'student-name' (wrong)
✗ Don't start with numbers: '2students' (wrong)
"""

# Good variable names:
user_name = "Bob"
total_score = 95
is_student = True
birth_year = 2008

# Now let's combine input() with variables:
print("\n--- Interactive Example ---")

# Get information from the user and store it:
name = input("What's your name? ")
age = input("How old are you? ")

# Use the stored information:
print("Hello, " + name + "!")
print("You are " + age + " years old.")

"""
INSTRUCTOR NOTE: This is a big moment! Students just created their first 
interactive program. Celebrate this achievement!

Point out:
1. We asked a question
2. We stored the answer
3. We used the answer later
This is the foundation of all interactive programs!
"""

# =============================================================================
# SECTION 4: WORKING WITH STRINGS (TEXT)
# =============================================================================

print("\n" + "=" * 50)
print("SECTION 4: WORKING WITH TEXT (STRINGS)")
print("=" * 50)

"""
STRINGS are sequences of characters (letters, numbers, symbols)
- Always surrounded by quotes: "like this" or 'like this'
- Can contain letters, numbers, spaces, punctuation
- We can join strings together (concatenation)
"""

# Creating string variables:
first_name = "Emma"
last_name = "Johnson"
city = "New York"

# Joining strings with + (concatenation):
full_name = first_name + " " + last_name
print("Full name:", full_name)

# We can join variables and text:
greeting = "Hello, " + first_name + "!"
print(greeting)

location_message = first_name + " lives in " + city
print(location_message)

"""
STRING CONCATENATION RULES:
- Use + to join strings together
- Don't forget spaces! "Hello" + "World" = "HelloWorld"
- Add spaces manually: "Hello" + " " + "World" = "Hello World"
"""

# Interactive string example:
print("\n--- Let's get to know you! ---")
user_name = input("What's your name? ")
favorite_color = input("What's your favorite color? ")
favorite_food = input("What's your favorite food? ")

# Create a personalized message:
message = "Hi " + user_name + "! I love that your favorite color is " + favorite_color + " and you like " + favorite_food + "!"
print(message)

# =============================================================================
# SECTION 5: WORKING WITH NUMBERS
# =============================================================================

print("\n" + "=" * 50)
print("SECTION 5: WORKING WITH NUMBERS")
print("=" * 50)

"""
NUMBERS IN PYTHON:
- Integers: whole numbers like 5, 42, -10
- No quotes needed around numbers
- We can do math with numbers: +, -, *, /
"""

# Number variables:
score1 = 85
score2 = 92
score3 = 78

# Math operations:
total = score1 + score2 + score3
average = total / 3

print("First score:", score1)
print("Second score:", score2)
print("Third score:", score3)
print("Total:", total)
print("Average:", average)

# More math examples:
current_year = 2024
birth_year = 2010
age = current_year - birth_year

print("If you were born in", birth_year, "you would be", age, "years old in", current_year)

"""
IMPORTANT: STRINGS vs NUMBERS
- "5" is text (a string) - you can't do math with it
- 5 is a number - you can do math with it
- input() always gives us text, even if the user types a number!
"""

# Demonstrating the difference:
text_number = "5"
real_number = 5

print("Text version:", text_number)
print("Number version:", real_number)
print("Math with number:", real_number + 3)
# print("Math with text:", text_number + 3)  # This would cause an error!

# Converting text to numbers:
user_input = input("Enter a number: ")  # This is always text
number = int(user_input)  # Convert text to integer
result = number * 2

print("You entered:", user_input, "(as text)")
print("Converted to number:", number)
print("Your number times 2:", result)

"""
CONVERSION FUNCTIONS:
- int() converts to whole numbers: int("5") = 5
- str() converts to text: str(5) = "5"
- float() converts to decimal numbers: float("5.5") = 5.5
"""

# =============================================================================
# SECTION 6: PUTTING IT ALL TOGETHER
# =============================================================================

print("\n" + "=" * 50)
print("SECTION 6: BUILDING A SIMPLE QUIZ")
print("=" * 50)

"""
Now let's combine everything we've learned:
- print() to show questions and messages
- input() to get answers from users
- Variables to store information
- Strings to work with text
- Numbers for scoring

Let's build a simple quiz step by step!
"""

print("Welcome to the Python Basics Quiz!")
print("Let's see what you've learned!")
print()

# Initialize score
score = 0

# Question 1
print("Question 1: What function do we use to display text?")
answer1 = input("Your answer: ")

if answer1.lower() == "print":
    print("Correct! ✓")
    score = score + 1
else:
    print("The answer is 'print' - that's how we display text!")

print()

# Question 2
print("Question 2: What do we put around text in Python?")
answer2 = input("Your answer: ")

if answer2.lower() == "quotes" or answer2 == '"' or answer2 == "'":
    print("Correct! ✓")
    score = score + 1
else:
    print("The answer is 'quotes' - we put quotes around text!")

print()

# Question 3
print("Question 3: What's 5 + 3?")
answer3 = input("Your answer: ")

if answer3 == "8":
    print("Correct! ✓")
    score = score + 1
else:
    print("The answer is 8!")

print()

# Show final score
print("Quiz complete!")
print("Your score:", score, "out of 3")

if score == 3:
    print("Perfect! You're ready for the next lesson! 🎉")
elif score == 2:
    print("Great job! Just review one concept and you'll be ready!")
else:
    print("Good start! Practice these concepts and try again!")

"""
INSTRUCTOR REFLECTION QUESTIONS:
After running this quiz, ask students:

1. "What was the most interesting thing you learned?"
2. "Which part was the most challenging?"
3. "Can you think of other questions we could add to this quiz?"
4. "What kind of program would you like to build next?"

This helps reinforce learning and gets them excited about future sessions!
"""

print("\n" + "=" * 50)
print("CONGRATULATIONS! YOU'VE COMPLETED SESSION 1!")
print("You now know the basics of talking to Python!")
print("=" * 50)