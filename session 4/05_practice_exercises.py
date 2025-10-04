# Session 4: Practice Exercises - If/Else Decision Making

print("=" * 60)
print("PRACTICE EXERCISES: IF/ELSE DECISION MAKING")
print("=" * 60)

print("Complete these exercises to practice if/else statements!")
print("Try to solve them before looking at the solutions.")

# EXERCISE 1: Temperature Converter and Advisor
print("\n" + "="*50)
print("EXERCISE 1: TEMPERATURE ADVISOR")
print("="*50)

print("Create a program that:")
print("1. Takes a temperature in Fahrenheit")
print("2. Converts it to Celsius") 
print("3. Gives clothing advice based on temperature")

print("\nTemperature ranges:")
print("• Above 80°F: Hot - wear light clothes")
print("• 60-80°F: Warm - comfortable clothes")
print("• 40-60°F: Cool - bring a jacket")
print("• Below 40°F: Cold - bundle up!")

def temperature_advisor():
    """Your code here!"""
    # TODO: Get temperature input from user
    # TODO: Convert Fahrenheit to Celsius: C = (F - 32) * 5/9
    # TODO: Give advice based on temperature ranges
    pass

# Example solution (try yours first!)
def temperature_advisor_solution():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    
    print(f"Temperature: {fahrenheit}°F ({celsius:.1f}°C)")
    
    if fahrenheit > 80:
        advice = "Hot - wear light clothes! 🌞"
    elif fahrenheit >= 60:
        advice = "Warm - comfortable clothes 👕"
    elif fahrenheit >= 40:
        advice = "Cool - bring a jacket 🧥"
    else:
        advice = "Cold - bundle up! 🧤"
    
    print(f"Advice: {advice}")

# EXERCISE 2: BMI Calculator with Categories
print("\n" + "="*50)
print("EXERCISE 2: BMI CALCULATOR")
print("="*50)

print("Create a BMI calculator that:")
print("1. Takes weight (kg) and height (m)")
print("2. Calculates BMI = weight / (height^2)")
print("3. Categorizes the result")

print("\nBMI Categories:")
print("• Below 18.5: Underweight")
print("• 18.5-24.9: Normal weight")
print("• 25.0-29.9: Overweight")
print("• 30.0 and above: Obese")

def bmi_calculator():
    """Your code here!"""
    # TODO: Get weight and height from user
    # TODO: Calculate BMI
    # TODO: Determine category
    # TODO: Print results with health advice
    pass

# Example solution
def bmi_calculator_solution():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = weight / (height ** 2)
    
    print(f"Your BMI: {bmi:.1f}")
    
    if bmi < 18.5:
        category = "Underweight"
        advice = "Consider consulting a nutritionist"
    elif bmi < 25:
        category = "Normal weight"
        advice = "Great! Maintain your healthy lifestyle"
    elif bmi < 30:
        category = "Overweight"
        advice = "Consider diet and exercise changes"
    else:
        category = "Obese"
        advice = "Consult with a healthcare professional"
    
    print(f"Category: {category}")
    print(f"Advice: {advice}")

# EXERCISE 3: Simple ATM Machine
print("\n" + "="*50)
print("EXERCISE 3: SIMPLE ATM MACHINE")
print("="*50)

print("Create a simple ATM that:")
print("1. Has a starting balance")
print("2. Allows deposit, withdrawal, or balance check")
print("3. Validates transactions")
print("4. Shows appropriate messages")

def simple_atm():
    """Your code here!"""
    # TODO: Set initial balance
    # TODO: Ask user for operation (deposit/withdraw/balance)
    # TODO: Handle each operation with appropriate checks
    # TODO: Update balance and show result
    pass

# Example solution
def simple_atm_solution():
    balance = 1000.00  # Starting balance
    
    print(f"Welcome to Simple ATM")
    print(f"Current balance: ${balance:.2f}")
    
    operation = input("Choose operation (deposit/withdraw/balance): ").lower()
    
    if operation == "balance":
        print(f"Your current balance is: ${balance:.2f}")
    elif operation == "deposit":
        amount = float(input("Enter deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount:.2f}")
            print(f"New balance: ${balance:.2f}")
        else:
            print("Invalid amount! Must be positive.")
    elif operation == "withdraw":
        amount = float(input("Enter withdrawal amount: $"))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn ${amount:.2f}")
                print(f"Remaining balance: ${balance:.2f}")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid amount! Must be positive.")
    else:
        print("Invalid operation!")

# EXERCISE 4: Quiz Grader
print("\n" + "="*50)
print("EXERCISE 4: QUIZ GRADER")
print("="*50)

print("Create a quiz grader that:")
print("1. Asks 5 multiple choice questions")
print("2. Checks answers against correct answers")
print("3. Calculates score and percentage")
print("4. Gives final grade and feedback")

def quiz_grader():
    """Your code here!"""
    # TODO: Create questions and correct answers
    # TODO: Ask questions and collect user answers
    # TODO: Compare answers and count correct ones
    # TODO: Calculate percentage and assign grade
    pass

# Example solution
def quiz_grader_solution():
    questions = [
        "What is the capital of France? (a) London (b) Paris (c) Berlin: ",
        "What is 2 + 2? (a) 3 (b) 4 (c) 5: ",
        "Which planet is closest to the sun? (a) Venus (b) Mercury (c) Mars: ",
        "What is the largest ocean? (a) Atlantic (b) Indian (c) Pacific: ",
        "Who wrote 'Romeo and Juliet'? (a) Shakespeare (b) Dickens (c) Austen: "
    ]
    
    correct_answers = ['b', 'b', 'b', 'c', 'a']
    user_answers = []
    
    print("Welcome to the Quiz! Choose a, b, or c for each question.")
    print("-" * 50)
    
    # Ask questions
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        answer = input("Your answer: ").lower()
        user_answers.append(answer)
        print()
    
    # Grade the quiz
    correct_count = 0
    print("QUIZ RESULTS:")
    print("-" * 20)
    
    for i, (user_ans, correct_ans) in enumerate(zip(user_answers, correct_answers), 1):
        if user_ans == correct_ans:
            print(f"Question {i}: ✅ Correct")
            correct_count += 1
        else:
            print(f"Question {i}: ❌ Wrong (correct answer: {correct_ans})")
    
    # Calculate final results
    percentage = (correct_count / len(questions)) * 100
    
    print(f"\nFinal Score: {correct_count}/{len(questions)} ({percentage:.0f}%)")
    
    if percentage >= 90:
        grade = "A"
        feedback = "Excellent work!"
    elif percentage >= 80:
        grade = "B" 
        feedback = "Good job!"
    elif percentage >= 70:
        grade = "C"
        feedback = "Satisfactory"
    elif percentage >= 60:
        grade = "D"
        feedback = "Needs improvement"
    else:
        grade = "F"
        feedback = "Study more and try again"
    
    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")

# EXERCISE 5: Rock Paper Scissors Game
print("\n" + "="*50)
print("EXERCISE 5: ROCK PAPER SCISSORS")
print("="*50)

print("Create a Rock Paper Scissors game that:")
print("1. Gets player choice")
print("2. Generates computer choice randomly")
print("3. Determines winner using game rules")
print("4. Shows results clearly")

def rock_paper_scissors():
    """Your code here!"""
    # TODO: Import random module
    # TODO: Get player choice (rock/paper/scissors)
    # TODO: Generate computer choice randomly
    # TODO: Compare choices and determine winner
    # TODO: Display results
    pass

# Example solution
def rock_paper_scissors_solution():
    import random
    
    choices = ["rock", "paper", "scissors"]
    
    print("Let's play Rock Paper Scissors!")
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if player_choice not in choices:
        print("Invalid choice!")
        return
    
    computer_choice = random.choice(choices)
    
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win! 🎉"
    else:
        result = "Computer wins! 🤖"
    
    print(f"Result: {result}")

# EXERCISE 6: Age Group Classifier
print("\n" + "="*50)
print("EXERCISE 6: AGE GROUP CLASSIFIER")
print("="*50)

print("Create an age classifier that:")
print("1. Takes person's age")
print("2. Classifies into appropriate group")
print("3. Provides relevant information for each group")

print("\nAge groups:")
print("• 0-2: Baby")
print("• 3-12: Child") 
print("• 13-19: Teenager")
print("• 20-64: Adult")
print("• 65+: Senior")

def age_classifier():
    """Your code here!"""
    pass

# BONUS EXERCISE: Simple Password Manager
print("\n" + "="*50)
print("BONUS: SIMPLE PASSWORD MANAGER")
print("="*50)

print("Create a password manager that:")
print("1. Stores passwords for different websites")
print("2. Allows adding, retrieving, or listing passwords")
print("3. Has a master password for access")
print("4. Validates password strength when adding")

def password_manager():
    """Your code here!"""
    pass

print("\n" + "="*60)
print("🎯 PRACTICE EXERCISES COMPLETE!")
print("Work through these exercises at your own pace.")
print("Remember to test your code with different inputs!")
print("Ask for help if you get stuck on any exercise.")
print("="*60)

# Uncomment these lines to test the solution functions:
# temperature_advisor_solution()
# bmi_calculator_solution()
# simple_atm_solution()
# quiz_grader_solution()
# rock_paper_scissors_solution()