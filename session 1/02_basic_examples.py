"""
Session 1: Step-by-Step Examples
================================

This file contains progressive examples that build from simple concepts to 
more complex interactions. Use these to demonstrate how concepts connect.

For Instructors: Run each example with students, then have them modify it.
Ask "What happens if we change...?" to encourage experimentation.
"""

# =============================================================================
# EXAMPLE 1: BABY STEPS WITH PRINT()
# =============================================================================

print("EXAMPLE 1: Getting Started with print()")
print("-" * 40)

# Step 1: Simple messages
print("Hello!")
print("Welcome to Python!")

# Step 2: Multiple lines create a conversation
print("Computer: Hello there!")
print("Computer: How are you today?")
print("Computer: I'm excited to learn Python with you!")

# Step 3: Using print() for formatting
print()  # Empty line for space
print("*** PYTHON LESSON 1 ***")
print("Topics: print, input, variables")
print("Goal: Build an interactive quiz")
print()

"""
INSTRUCTOR TIP: Point out how print() creates output line by line.
Ask students: "What if we wanted the computer to wait for our answer?"
This sets up the need for input()!
"""

# =============================================================================
# EXAMPLE 2: FIRST INTERACTION WITH INPUT()
# =============================================================================

print("\nEXAMPLE 2: Making Programs Interactive")
print("-" * 40)

# Step 1: Basic input (but we lose the answer!)
print("Let's try getting input...")
input("What's your favorite color? ")
print("Thanks for telling me, but I already forgot! 😅")

# Step 2: Saving input in a variable
print("\nNow let's save your answer...")
color = input("What's your favorite color? ")
print("I'll remember that you like " + color + "!")

# Step 3: Using the stored information multiple times
print("Since you like " + color + ", here are some " + color + " things:")
print("- " + color + " flowers")
print("- " + color + " cars")
print("- " + color + " shirts")

"""
INSTRUCTOR TIP: This example shows the power of variables!
Students can see why we need to store information.
"""

# =============================================================================
# EXAMPLE 3: BUILDING A SIMPLE CONVERSATION
# =============================================================================

print("\n\nEXAMPLE 3: Creating a Conversation")
print("-" * 40)

# Step 1: Get multiple pieces of information
name = input("Hi! What's your name? ")
age = input("Nice to meet you, " + name + "! How old are you? ")
hobby = input("Cool! What do you like to do for fun? ")

# Step 2: Use all the information to create a personalized response
print("\nLet me tell you what I learned about you:")
print("Your name is " + name)
print("You are " + age + " years old")
print("You enjoy " + hobby)

# Step 3: Create a more natural conversation
print("\n" + name + ", since you're " + age + " and you like " + hobby + ",")
print("I think you'll really enjoy learning Python!")
print("Programming is like " + hobby + " - it's creative and fun!")

"""
INSTRUCTOR TIP: Show how variables make programs personal and engaging.
Ask: "How is this different from a program that just prints the same thing every time?"
"""

# =============================================================================
# EXAMPLE 4: WORKING WITH NUMBERS STEP BY STEP
# =============================================================================

print("\n\nEXAMPLE 4: Python as a Calculator")
print("-" * 40)

# Step 1: Simple math
print("Python can do math!")
print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("6 * 7 =", 6 * 7)

# Step 2: Math with variables
first_number = 15
second_number = 8
result = first_number + second_number

print("\nUsing variables for math:")
print("First number:", first_number)
print("Second number:", second_number)
print("Sum:", result)

# Step 3: Interactive math
print("\nLet's do math together!")
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")

# Important: Convert text to numbers!
number1 = int(num1)
number2 = int(num2)
answer = number1 + number2

print("Math time!")
print(num1 + " + " + num2 + " = " + str(answer))

"""
INSTRUCTOR TIP: This example shows the difference between text and numbers.
Demonstrate what happens if you forget int() - you get "5" + "3" = "53"!
"""

# =============================================================================
# EXAMPLE 5: BUILDING TOWARD A QUIZ
# =============================================================================

print("\n\nEXAMPLE 5: Question and Answer Pattern")
print("-" * 40)

# Step 1: Simple question with feedback
question = "What is the capital of France?"
print(question)
user_answer = input("Your answer: ")

print("You answered:", user_answer)
if user_answer.lower() == "paris":
    print("Correct! Well done! 🎉")
else:
    print("The answer is Paris. Good try!")

# Step 2: Multiple choice makes it easier
print("\nLet's try a multiple choice question:")
print("What language are we learning?")
print("A) Java")
print("B) Python") 
print("C) Spanish")
print("D) French")

choice = input("Enter your choice (A, B, C, or D): ")

if choice.upper() == "B":
    print("Correct! We're learning Python! 🐍")
else:
    print("The answer is B - Python!")

# Step 3: Keeping score
print("\nLet's keep track of correct answers:")
score = 0  # Start with 0 points

# Question 1
print("\nQuestion 1: What symbol do we use for addition?")
answer = input("Your answer: ")
if answer == "+":
    print("Correct!")
    score = score + 1
else:
    print("The answer is +")

# Question 2  
print("\nQuestion 2: What function displays text?")
answer = input("Your answer: ")
if answer.lower() == "print":
    print("Correct!")
    score = score + 1
else:
    print("The answer is print")

# Show final score
print("\nYour final score:", score, "out of 2")

"""
INSTRUCTOR TIP: This shows the basic structure of any quiz program:
1. Ask a question
2. Get an answer
3. Check if it's correct
4. Update the score
5. Repeat!
"""

# =============================================================================
# EXAMPLE 6: PUTTING PERSONALITY INTO PROGRAMS
# =============================================================================

print("\n\nEXAMPLE 6: Adding Personality and Fun")
print("-" * 40)

# Step 1: Friendly introduction
print("🤖 Hello! I'm PyBot, your friendly Python assistant!")
print("I'm here to help you learn programming!")

name = input("What should I call you? ")
print("Great to meet you, " + name + "! 😊")

# Step 2: Personalized interaction
print("\n" + name + ", I have a fun fact about your name!")
print("Your name '" + name + "' has " + str(len(name)) + " letters in it!")

if len(name) <= 4:
    print("Short and sweet! I like it!")
elif len(name) <= 8:
    print("That's a nice length for a name!")
else:
    print("Wow, that's a long name! Very distinguished!")

# Step 3: Encouraging conclusion
print("\n" + name + ", you're doing great with Python!")
print("Every programmer started exactly where you are now.")
print("Keep practicing, and soon you'll be building amazing programs!")
print("See you in the next lesson! 👋")

"""
INSTRUCTOR TIP: This example shows how programming can be fun and personal.
Students see that programs don't have to be boring!

Key points to highlight:
- Programs can have personality
- We can make users feel welcome and encouraged
- Small touches (like counting letters) can make programs feel magical
- Programming is about solving problems AND creating experiences
"""

print("\n" + "=" * 60)
print("END OF STEP-BY-STEP EXAMPLES")
print("=" * 60)
print("These examples showed the building blocks of interactive programming!")
print("Next: Let's put it all together in a complete quiz program!")