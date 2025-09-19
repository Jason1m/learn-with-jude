"""
Session 1: Practice Exercises
=============================

These exercises help students practice the concepts they've learned.
Start with Exercise 1 and work your way up. Each exercise builds on previous skills.

For Instructors: Have students work on these individually or in pairs.
Circulate and help with any questions. Encourage experimentation!
"""

print("🏋️ PYTHON SESSION 1 - PRACTICE EXERCISES 🏋️")
print("Complete these exercises to strengthen your Python skills!")
print("=" * 60)

# =============================================================================
# EXERCISE 1: BASIC PRINT PRACTICE
# =============================================================================

print("\n📝 EXERCISE 1: Getting Comfortable with print()")
print("-" * 50)
print("Your task: Create a program that introduces yourself")
print()
print("Example output:")
print("Hi! My name is Sarah.")
print("I am 15 years old.")
print("I love playing basketball.")
print("I'm excited to learn Python!")
print()
print("Now you try! Write your own introduction using 4 print() statements:")
print("(Write your code below this line)")
print()

# STUDENT SOLUTION SPACE:
# Write your code here:
# print("Hi! My name is ...")
# print("I am ... years old.")
# print("I love ...")
# print("I'm excited to ...")

print("✅ Exercise 1 Complete! Great job with your first Python program!")

# =============================================================================
# EXERCISE 2: BASIC INPUT AND VARIABLES
# =============================================================================

print("\n\n📝 EXERCISE 2: Storing Information")
print("-" * 50)
print("Your task: Ask the user 3 questions and store their answers")
print()
print("Example:")
print("Program asks: What's your favorite food?")
print("User types: pizza")
print("Program says: Cool! You like pizza!")
print()
print("Your program should:")
print("1. Ask for their favorite food")
print("2. Ask for their favorite color") 
print("3. Ask for their favorite animal")
print("4. Tell them what you learned about them")
print()
print("Now you try:")
print()

# STUDENT SOLUTION SPACE:
# Write your code here:
# favorite_food = input("What's your favorite food? ")
# favorite_color = input("What's your favorite color? ")
# favorite_animal = input("What's your favorite animal? ")
# 
# print("Cool! You like " + favorite_food + "!")
# print("And your favorite color is " + favorite_color + "!")
# print("I love that your favorite animal is a " + favorite_animal + "!")

print("✅ Exercise 2 Complete! You're getting good at variables!")

# =============================================================================
# EXERCISE 3: BASIC MATH WITH VARIABLES
# =============================================================================

print("\n\n📝 EXERCISE 3: Python Calculator")
print("-" * 50)
print("Your task: Create a simple calculator")
print()
print("Your program should:")
print("1. Ask the user for two numbers")
print("2. Add them together")
print("3. Show the result")
print()
print("Example:")
print("Enter first number: 5")
print("Enter second number: 3")
print("5 + 3 = 8")
print()
print("Remember: Use int() to convert input to numbers!")
print()
print("Now you try:")
print()

# STUDENT SOLUTION SPACE:
# Write your code here:
# first_num = input("Enter first number: ")
# second_num = input("Enter second number: ")
# 
# num1 = int(first_num)
# num2 = int(second_num)
# result = num1 + num2
# 
# print(first_num + " + " + second_num + " = " + str(result))

print("✅ Exercise 3 Complete! You're becoming a Python mathematician!")

# =============================================================================
# EXERCISE 4: PERSONAL INFORMATION COLLECTOR
# =============================================================================

print("\n\n📝 EXERCISE 4: All About You")
print("-" * 50)
print("Your task: Create a program that learns about the user")
print()
print("Your program should ask for:")
print("- Name")
print("- Age") 
print("- Favorite subject in school")
print("- Dream job")
print()
print("Then create a summary like this:")
print("'Hi Alice! You're 14 years old. You love Math and want to be a Doctor.'")
print()
print("Challenge: Make it personal and encouraging!")
print()

# STUDENT SOLUTION SPACE:
# Write your code here:
# name = input("What's your name? ")
# age = input("How old are you? ")
# subject = input("What's your favorite subject? ")
# job = input("What's your dream job? ")
# 
# print("Hi " + name + "! You're " + age + " years old.")
# print("You love " + subject + " and want to be a " + job + ".")
# print("That's awesome! Keep studying " + subject + " to reach your goals!")

print("✅ Exercise 4 Complete! You're great at making programs personal!")

# =============================================================================
# EXERCISE 5: SIMPLE QUIZ CREATION
# =============================================================================

print("\n\n📝 EXERCISE 5: Build Your Own Mini Quiz")
print("-" * 50)
print("Your task: Create a 2-question quiz on any topic you like")
print()
print("Your quiz should:")
print("1. Ask 2 questions")
print("2. Check if answers are correct")
print("3. Keep score")
print("4. Give encouraging feedback")
print()
print("Topics ideas: Sports, Movies, Music, Animals, Food, Friends")
print()
print("Example structure:")
print("Question 1: What's the biggest planet?")
print("Answer: Jupiter")
print("If correct: 'Great job!' and add 1 to score")
print("If wrong: 'The answer is Jupiter' and don't add to score")
print()

# STUDENT SOLUTION SPACE:
# Write your code here:
# print("Welcome to My Quiz!")
# score = 0
# 
# # Question 1
# answer1 = input("Question 1: What's the biggest planet? ")
# if answer1.lower() == "jupiter":
#     print("Correct!")
#     score = score + 1
# else:
#     print("The answer is Jupiter")
# 
# # Question 2  
# answer2 = input("Question 2: How many legs does a spider have? ")
# if answer2 == "8":
#     print("Correct!")
#     score = score + 1
# else:
#     print("The answer is 8")
# 
# print("Your score: " + str(score) + " out of 2")

print("✅ Exercise 5 Complete! You've built your own quiz program!")

# =============================================================================
# EXERCISE 6: CREATIVE CHALLENGE - MAD LIBS
# =============================================================================

print("\n\n📝 EXERCISE 6: Mad Libs Generator (Creative Challenge!)")
print("-" * 50)
print("Your task: Create a Mad Libs story!")
print()
print("Mad Libs ask for words, then put them in a funny story.")
print()
print("Example:")
print("Enter a name: Bob")
print("Enter an animal: elephant") 
print("Enter a color: purple")
print()
print("Story: Bob has a pet purple elephant that loves to dance!")
print()
print("Your task:")
print("1. Ask for 4-5 different words (names, animals, colors, foods, etc.)")
print("2. Put them together in a creative story")
print("3. Make it fun and silly!")
print()

# STUDENT SOLUTION SPACE:
# Write your code here:
# print("Let's create a silly story!")
# name = input("Enter a person's name: ")
# animal = input("Enter an animal: ")
# color = input("Enter a color: ")
# food = input("Enter a food: ")
# place = input("Enter a place: ")
# 
# print("\n--- YOUR SILLY STORY ---")
# print("Once upon a time, " + name + " found a " + color + " " + animal + ".")
# print("The " + animal + " loved to eat " + food + " all day long.")
# print("Together they traveled to " + place + " and had amazing adventures!")
# print("The end!")

print("✅ Exercise 6 Complete! You're a creative programmer!")

# =============================================================================
# BONUS EXERCISES FOR FAST LEARNERS
# =============================================================================

print("\n\n🌟 BONUS EXERCISES (For Fast Learners)")
print("-" * 50)

print("\n🚀 Bonus 1: Age Calculator")
print("Ask for birth year, calculate and display current age")

print("\n🚀 Bonus 2: Name Length Analyzer") 
print("Ask for a name, tell them how many letters it has")

print("\n🚀 Bonus 3: Multiple Choice Quiz")
print("Create a quiz with A/B/C/D options")

print("\n🚀 Bonus 4: Compliment Generator")
print("Ask for their name and give them a personalized compliment")

print("\n🚀 Bonus 5: Simple Story Builder")
print("Ask for character, setting, problem, solution - create a story!")

# =============================================================================
# SELF-CHECK QUESTIONS
# =============================================================================

print("\n\n🔍 SELF-CHECK: Do You Understand?")
print("-" * 50)
print("After completing these exercises, you should be able to:")
print()
print("✓ Use print() to display messages")
print("✓ Use input() to get information from users") 
print("✓ Create variables with good names")
print("✓ Store text (strings) and numbers in variables")
print("✓ Join strings together with +")
print("✓ Convert between text and numbers")
print("✓ Write simple if statements to check answers")
print("✓ Build an interactive program from start to finish")
print()
print("If you can do all of these, you're ready for Session 2!")
print("If not, that's okay - practice the exercises again!")

# =============================================================================
# TIPS FOR SUCCESS
# =============================================================================

print("\n\n💡 TIPS FOR SUCCESS")
print("-" * 50)
print("• Type the code yourself - don't just read it!")
print("• Make mistakes - that's how you learn!")
print("• Change things and see what happens")
print("• Ask 'What if I tried...?' and experiment")
print("• Don't worry about making it perfect")
print("• Have fun and be creative!")
print("• Remember: Every expert was once a beginner!")

print("\n" + "=" * 60)
print("🎉 CONGRATULATIONS! 🎉")
print("You've completed all the Session 1 practice exercises!")
print("You're well on your way to becoming a Python programmer!")
print("Keep coding and have fun! 🐍✨")
print("=" * 60)