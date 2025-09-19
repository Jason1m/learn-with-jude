"""
Session 1: Interactive Quiz Project
===================================

This file contains the main project for Session 1: an interactive quiz that 
demonstrates all the concepts students have learned.

For Instructors: Build this together with students step by step.
Start with the basic version, then add features as time permits.
"""

# =============================================================================
# VERSION 1: BASIC QUIZ (START HERE)
# =============================================================================

def basic_quiz():
    """
    A simple quiz that demonstrates core concepts:
    - print() for questions and feedback
    - input() for getting answers
    - variables for storing information
    - basic if statements for checking answers
    """
    
    print("🎯 WELCOME TO THE PYTHON BASICS QUIZ! 🎯")
    print("Let's see what you've learned!")
    print("=" * 40)
    
    # Get the student's name for personalization
    student_name = input("First, what's your name? ")
    print("Hello, " + student_name + "! Let's begin!")
    print()
    
    # Initialize score to keep track of correct answers
    score = 0
    total_questions = 3
    
    # Question 1: About print() function
    print("Question 1:")
    print("What function do we use to display text on the screen?")
    answer1 = input("Your answer: ")
    
    # Check if the answer is correct (case-insensitive)
    if answer1.lower() == "print":
        print("✅ Correct! The print() function displays text!")
        score = score + 1
    else:
        print("❌ Not quite. The answer is 'print' - that's how we display text!")
    print()
    
    # Question 2: About quotes and strings
    print("Question 2:")
    print("What do we put around text to tell Python it's a string?")
    answer2 = input("Your answer: ")
    
    # Accept multiple correct answers
    if answer2.lower() == "quotes" or answer2 == '"' or answer2 == "'":
        print("✅ Correct! We put quotes around strings!")
        score = score + 1
    else:
        print("❌ Not quite. The answer is 'quotes' - either 'single' or \"double\"!")
    print()
    
    # Question 3: Basic math
    print("Question 3:")
    print("What is 7 + 5?")
    answer3 = input("Your answer: ")
    
    if answer3 == "12":
        print("✅ Correct! 7 + 5 = 12!")
        score = score + 1
    else:
        print("❌ Not quite. 7 + 5 = 12")
    print()
    
    # Show final results with personalized feedback
    print("=" * 40)
    print("QUIZ COMPLETE!")
    print(student_name + ", your final score is: " + str(score) + " out of " + str(total_questions))
    
    # Give encouraging feedback based on score
    if score == total_questions:
        print("🎉 Perfect score! You're a Python superstar!")
    elif score >= 2:
        print("🌟 Great job! You're really getting the hang of this!")
    elif score >= 1:
        print("👍 Good start! Keep practicing and you'll improve!")
    else:
        print("💪 Don't worry! Everyone learns at their own pace. Try again!")
    
    print("Thanks for taking the quiz, " + student_name + "!")

# =============================================================================
# VERSION 2: ENHANCED QUIZ WITH MORE FEATURES
# =============================================================================

def enhanced_quiz():
    """
    An enhanced version with more questions, better feedback, and 
    additional features for advanced students.
    """
    
    print("🚀 ENHANCED PYTHON BASICS QUIZ 🚀")
    print("This version has more questions and features!")
    print("=" * 50)
    
    # Get student information
    student_name = input("What's your name? ")
    grade = input("What grade are you in? ")
    
    print("Hello, " + student_name + " from grade " + grade + "!")
    print("Let's see how much you've learned about Python!")
    print()
    
    # Initialize tracking variables
    score = 0
    total_questions = 5
    
    # Question 1: print() function
    print("📝 Question 1 of " + str(total_questions))
    print("Which function displays text on the screen?")
    print("A) display()")
    print("B) print()")
    print("C) show()")
    print("D) output()")
    
    answer = input("Enter your choice (A, B, C, or D): ")
    
    if answer.upper() == "B":
        print("✅ Excellent! print() is correct!")
        score += 1
    else:
        print("❌ The answer is B - print()")
    print()
    
    # Question 2: Variables
    print("📝 Question 2 of " + str(total_questions))
    print("What symbol do we use to store a value in a variable?")
    print("Example: name ___ 'Alice'")
    
    answer = input("Your answer: ")
    
    if answer == "=":
        print("✅ Perfect! We use = to assign values to variables!")
        score += 1
    else:
        print("❌ The answer is = (the equals sign)")
    print()
    
    # Question 3: String concatenation
    print("📝 Question 3 of " + str(total_questions))
    print("How do we join two strings together?")
    print("Example: 'Hello' ___ 'World'")
    
    answer = input("Your answer: ")
    
    if answer == "+":
        print("✅ Great! We use + to concatenate (join) strings!")
        score += 1
    else:
        print("❌ The answer is + (the plus sign)")
    print()
    
    # Question 4: Interactive question about the student
    print("📝 Question 4 of " + str(total_questions))
    print("Let's practice with your information!")
    birth_year = input("What year were you born? ")
    
    # Convert to number and calculate age
    current_year = 2024
    age = current_year - int(birth_year)
    
    print("So you are about " + str(age) + " years old!")
    confirm = input("Is that correct? (yes/no): ")
    
    if confirm.lower() == "yes" or confirm.lower() == "y":
        print("✅ Great! You understand how variables and math work together!")
        score += 1
    else:
        print("🤔 That's okay - calculating ages with variables takes practice!")
    print()
    
    # Question 5: Creative question
    print("📝 Question 5 of " + str(total_questions))
    print("What's the best thing about learning Python?")
    print("(There's no wrong answer - this is about your opinion!)")
    
    opinion = input("Your answer: ")
    
    print("✅ That's a wonderful answer: '" + opinion + "'")
    print("Everyone has their own reasons for loving Python!")
    score += 1  # Everyone gets this point for participating!
    print()
    
    # Final results with detailed feedback
    print("🏆 " + "=" * 40 + " 🏆")
    print("QUIZ RESULTS FOR " + student_name.upper())
    print("=" * 50)
    print("Final Score: " + str(score) + " out of " + str(total_questions))
    
    # Calculate percentage
    percentage = (score / total_questions) * 100
    print("Percentage: " + str(int(percentage)) + "%")
    
    # Detailed feedback
    if score == total_questions:
        print("🎉 OUTSTANDING! Perfect score!")
        print("You've mastered the basics of Python!")
    elif score >= 4:
        print("🌟 EXCELLENT! You're doing great!")
        print("You understand most of the key concepts!")
    elif score >= 3:
        print("👍 GOOD JOB! You're on the right track!")
        print("Review the concepts you missed and you'll be ready!")
    elif score >= 2:
        print("💪 KEEP GOING! You're learning!")
        print("Practice these concepts and try again!")
    else:
        print("🌱 GREAT START! Everyone begins somewhere!")
        print("Don't give up - programming takes practice!")
    
    print("\nThanks for taking the enhanced quiz, " + student_name + "!")
    print("Keep coding and have fun with Python! 🐍✨")

# =============================================================================
# VERSION 3: MINI QUIZ GENERATOR (BONUS)
# =============================================================================

def mini_quiz_generator():
    """
    A bonus version that lets students create their own mini quiz!
    This shows how the concepts can be used creatively.
    """
    
    print("🎨 MINI QUIZ GENERATOR 🎨")
    print("Let's create your own quiz!")
    print("=" * 35)
    
    # Get quiz creator information
    creator = input("Quiz Creator Name: ")
    quiz_topic = input("What topic is your quiz about? ")
    
    print("\nGreat! " + creator + " is creating a quiz about " + quiz_topic + "!")
    print()
    
    # Help them create questions
    print("Let's create your quiz questions:")
    
    # Question 1
    question1 = input("Enter your first question: ")
    correct1 = input("What's the correct answer? ")
    
    # Question 2
    question2 = input("Enter your second question: ")
    correct2 = input("What's the correct answer? ")
    
    print("\n" + "🎯 " + quiz_topic.upper() + " QUIZ 🎯")
    print("Created by: " + creator)
    print("=" * 30)
    
    # Get quiz taker information
    taker = input("Quiz taker, what's your name? ")
    print("Hello " + taker + "! Let's see how much you know about " + quiz_topic + "!")
    print()
    
    score = 0
    
    # Ask the created questions
    print("Question 1: " + question1)
    answer1 = input("Your answer: ")
    
    if answer1.lower() == correct1.lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ The answer is: " + correct1)
    print()
    
    print("Question 2: " + question2)
    answer2 = input("Your answer: ")
    
    if answer2.lower() == correct2.lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ The answer is: " + correct2)
    print()
    
    # Show results
    print("Quiz Results:")
    print(taker + " scored " + str(score) + " out of 2 on " + creator + "'s " + quiz_topic + " quiz!")
    
    if score == 2:
        print("Perfect! " + taker + " knows a lot about " + quiz_topic + "!")
    elif score == 1:
        print("Good job! " + taker + " is learning about " + quiz_topic + "!")
    else:
        print(taker + " should study more about " + quiz_topic + "!")
    
    print("\nThanks for using the Mini Quiz Generator!")

# =============================================================================
# MAIN PROGRAM - CHOOSE WHICH VERSION TO RUN
# =============================================================================

def main():
    """
    Main function that lets users choose which quiz version to run.
    Instructors can comment/uncomment different versions as needed.
    """
    
    print("🐍 PYTHON SESSION 1 - INTERACTIVE QUIZ PROJECT 🐍")
    print("=" * 55)
    print("Choose which version you'd like to try:")
    print()
    print("1 - Basic Quiz (recommended for first time)")
    print("2 - Enhanced Quiz (more features)")
    print("3 - Mini Quiz Generator (create your own!)")
    print()
    
    choice = input("Enter your choice (1, 2, or 3): ")
    print()
    
    if choice == "1":
        basic_quiz()
    elif choice == "2":
        enhanced_quiz()
    elif choice == "3":
        mini_quiz_generator()
    else:
        print("Let's start with the basic quiz!")
        basic_quiz()

# =============================================================================
# INSTRUCTOR NOTES AND TEACHING SUGGESTIONS
# =============================================================================

"""
TEACHING PROGRESSION:

SESSION FLOW:
1. Start by showing students the basic_quiz() function
2. Run it together, having students type along
3. Ask: "What if we wanted to add more questions?"
4. Show the enhanced_quiz() with additional features
5. For advanced students: demonstrate the mini_quiz_generator()

KEY CONCEPTS DEMONSTRATED:
✅ print() - Used throughout for questions and feedback
✅ input() - Gets user responses and information
✅ Variables - Store names, scores, answers
✅ Strings - All text handling and concatenation
✅ Numbers - Scoring system and basic math
✅ Basic conditionals (if statements) - Check answers

CUSTOMIZATION IDEAS:
- Change questions to match your curriculum
- Add questions about other subjects (math, science, history)
- Modify scoring system (partial credit, bonus points)
- Add more personality with emojis and messages
- Create themed quizzes (sports, movies, books)

COMMON STUDENT QUESTIONS:
Q: "Why do we use .lower() with answers?"
A: So "Print", "PRINT", and "print" all count as correct!

Q: "What does += mean?"
A: It's a shortcut for score = score + 1

Q: "Can we make the quiz longer?"
A: Absolutely! Just add more questions following the same pattern.

Q: "How do we save the quiz results?"
A: Great question! We'll learn about files in a future session.

EXTENSIONS FOR FAST LEARNERS:
- Add multiple choice questions with A/B/C/D options
- Create a quiz about their favorite subject
- Add a timer element (advanced)
- Make the quiz ask random questions
- Add difficulty levels
"""

# Run the main program
if __name__ == "__main__":
    main()