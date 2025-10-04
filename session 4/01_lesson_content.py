# Session 4: Making Decisions (if, else)
# Detailed Explanation and Examples

print("=" * 60)
print("SESSION 4: MAKING DECISIONS (IF, ELSE)")
print("=" * 60)

# PART 1: INTRODUCTION TO DECISION MAKING
print("\n1. INTRODUCTION TO DECISION MAKING")
print("-" * 40)

print("In real life, we make decisions every day:")
print("• If it's raining, I'll take an umbrella")
print("• If I'm hungry, I'll eat something")
print("• If the traffic light is red, I'll stop")
print("• If my password is correct, I can log in")

print("\nIn programming, we use 'if statements' to make decisions!")
print("The computer can choose different paths based on conditions.")

# PART 2: YOUR FIRST IF STATEMENT
print("\n\n2. YOUR FIRST IF STATEMENT")
print("-" * 40)

print("Basic syntax:")
print("if condition:")
print("    # do something")

print("\nLet's try a simple example:")

# Simple if statement
weather = "sunny"
print(f"Today's weather: {weather}")

if weather == "sunny":
    print("It's a beautiful day! Let's go outside!")

print("This line runs regardless of the weather.")

print("\n" + "="*50)

# Another example with user input
print("\nLet's try with your input:")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")

if age < 18:
    print("You are a minor.")

# PART 3: COMPARISON OPERATORS
print("\n\n3. COMPARISON OPERATORS")
print("-" * 40) 
print("Comparison operators help us compare values:")
print("==  (equal to)")
print("!=  (not equal to)")
print(">   (greater than)")
print("<   (less than)")
print(">=  (greater than or equal to)")
print("<=  (less than or equal to)")

print("\nExamples:")
a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # False
print(f"a != b: {a != b}")  # True
print(f"a > b: {a > b}")    # True
print(f"a < b: {a < b}")    # False
print(f"a >= 10: {a >= 10}") # True
print(f"b <= 5: {b <= 5}")   # True

# PART 4: IF, ELIF, ELSE
print("\n\n4. IF, ELIF, ELSE")
print("-" * 40)

print("Sometimes we need multiple conditions:")
print("• if: first condition")
print("• elif: additional conditions") 
print("• else: what to do if none of the above")

print("\nExample: Traffic light system")

light = "yellow"
print(f"Traffic light is: {light}")

if light == "green":
    print("GO! Drive safely.")
elif light == "yellow":
    print("CAUTION! Slow down.")
elif light == "red":
    print("STOP! Wait for green.")
else:
    print("Broken light! Proceed with extreme caution.")

print("\n" + "="*50)

# Grade example
print("\nGrading system example:")
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
    print("Excellent work!")
elif score >= 80:
    grade = "B"
    print("Good job!")
elif score >= 70:
    grade = "C"
    print("You passed!")
elif score >= 60:
    grade = "D"
    print("You barely passed.")
else:
    grade = "F"
    print("You need to study more.")

print(f"Your grade is: {grade}")

# PART 5: LOGICAL OPERATORS
print("\n\n5. LOGICAL OPERATORS")
print("-" * 40)

print("Logical operators combine conditions:")
print("and: Both conditions must be true")
print("or:  At least one condition must be true")
print("not: Reverses the condition (True becomes False)")

print("\nExamples:")

# AND operator
age = 25
has_license = True

print(f"Age: {age}, Has license: {has_license}")

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive.")

print()

# OR operator
day = "Saturday"
is_holiday = False

print(f"Day: {day}, Is holiday: {is_holiday}")

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("It's a day off! Relax!")
else:
    print("It's a work day.")

print()

# NOT operator
is_raining = False
print(f"Is raining: {is_raining}")

if not is_raining:
    print("Great! We can go for a walk.")
else:
    print("Let's stay inside.")

# PART 6: PRACTICAL EXAMPLES
print("\n\n6. PRACTICAL EXAMPLES")
print("-" * 40)

print("Let's build some useful programs!")

print("\n--- Password Strength Checker ---")
password = input("Enter a password: ")

# Check password requirements
is_long_enough = len(password) >= 8
has_numbers = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)

print(f"Length >= 8: {is_long_enough}")
print(f"Has numbers: {has_numbers}")
print(f"Has uppercase: {has_uppercase}")

if is_long_enough and has_numbers and has_uppercase:
    print("✅ Strong password!")
elif is_long_enough and (has_numbers or has_uppercase):
    print("⚠️  Moderate password. Consider adding more requirements.")
else:
    print("❌ Weak password. Please improve it.")

print("\n--- Age Category Classifier ---")
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
elif age <= 100:
    print("You are a senior.")
else:
    print("Wow, you're very old! Are you sure about that age?")

# PART 7: NESTED IF STATEMENTS
print("\n\n7. NESTED IF STATEMENTS")
print("-" * 40)

print("You can put if statements inside other if statements!")

weather = input("What's the weather like? (sunny/rainy/cloudy): ").lower()

if weather == "sunny":
    temperature = int(input("What's the temperature? "))
    if temperature > 75:
        print("Perfect beach weather! 🏖️")
    elif temperature > 60:
        print("Nice day for a walk! 🚶")
    else:
        print("Sunny but a bit chilly. Bring a jacket! 🧥")
elif weather == "rainy":
    print("Don't forget your umbrella! ☔")
else:
    print("Not sure what to expect. Check the forecast! 🌤️")

# PART 8: COMMON MISTAKES TO AVOID
print("\n\n8. COMMON MISTAKES TO AVOID")
print("-" * 40)

print("❌ Using = instead of == for comparison")
print("   Wrong: if age = 18")
print("   Right: if age == 18")
print()

print("❌ Forgetting the colon :")
print("   Wrong: if age >= 18")
print("   Right: if age >= 18:")
print()

print("❌ Incorrect indentation")
print("   Wrong:")
print("   if age >= 18:")
print("   print('Adult')  # Not indented!")
print()
print("   Right:")
print("   if age >= 18:")
print("       print('Adult')  # Properly indented")
print()

print("❌ Case sensitivity in strings")
print("   'Hello' != 'hello'")
print("   Use .lower() or .upper() to normalize")

print("\n" + "="*60)
print("🎉 CONGRATULATIONS!")
print("You now know how to make decisions in Python!")
print("Practice with the exercises to master these concepts.")
print("="*60)