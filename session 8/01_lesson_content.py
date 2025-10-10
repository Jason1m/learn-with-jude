# Session 8: Creating Your Own Tools with Functions
# Detailed Explanation and Examples

print("=" * 60)
print("SESSION 8: CREATING YOUR OWN TOOLS WITH FUNCTIONS")
print("=" * 60)

# PART 1: INTRODUCTION TO FUNCTIONS
print("\n1. INTRODUCTION TO FUNCTIONS")
print("-" * 40)

print("What are functions?")
print("• Reusable blocks of code that perform specific tasks")
print("• Like tools in a toolbox - each has a specific purpose")
print("• Help organize and structure your programs")
print("• Avoid repeating the same code over and over")

print("\nReal-world analogy:")
print("🔨 Hammer: Does one thing well (drives nails)")
print("🔧 Wrench: Specialized tool for specific task")
print("📱 Phone: Complex tool made of many simple parts")
print("🍳 Recipe: Step-by-step instructions you can reuse")

print("\nIn programming:")
print("• Functions are like recipes - follow the steps to get results")
print("• You can use the same function many times")
print("• Functions can take inputs (ingredients) and give outputs (results)")

# PART 2: YOUR FIRST FUNCTION
print("\n\n2. YOUR FIRST FUNCTION")
print("-" * 40)

print("Function syntax:")
print("def function_name(parameters):")
print("    \"\"\"Optional description\"\"\"")
print("    # do something")
print("    return result  # optional")

print("\nLet's create our first function:")

def greet_user():
    """A simple function that greets the user"""
    print("Hello! Welcome to Python functions!")
    print("Functions make programming so much easier!")

# Call the function
print("\nCalling our function:")
greet_user()

print("\nLet's call it again:")
greet_user()

print("\nSee? Same result each time - that's the power of functions!")

# PART 3: FUNCTIONS WITH PARAMETERS
print("\n\n3. FUNCTIONS WITH PARAMETERS")
print("-" * 40)

print("Parameters make functions flexible!")
print("They're like variables that get values when you call the function.")

def greet_person(name):
    """Greet a specific person by name"""
    print(f"Hello, {name}! Great to see you!")

def greet_person_with_time(name, time_of_day):
    """Greet a person with time-specific message"""
    print(f"Good {time_of_day}, {name}! Hope you're having a wonderful day!")

# Test the functions
print("\nTesting functions with parameters:")
greet_person("Alice")
greet_person("Bob")
greet_person_with_time("Charlie", "morning")
greet_person_with_time("Diana", "evening")

print("\nSame function, different results based on input!")

# PART 4: FUNCTIONS THAT RETURN VALUES
print("\n\n4. FUNCTIONS THAT RETURN VALUES")
print("-" * 40)

print("Functions can calculate and return results!")
print("This is more powerful than just printing.")

def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

def calculate_area_rectangle(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

def get_user_info(name, age, city):
    """Create a formatted user information string"""
    info = f"{name} is {age} years old and lives in {city}"
    return info

# Test return functions
print("\nTesting functions that return values:")

sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

area = calculate_area_rectangle(10, 6)
print(f"Rectangle area: {area} square units")

user_details = get_user_info("Eve", 28, "Seattle")
print(f"User info: {user_details}")

print("\nWe can store the results and use them later!")

# PART 5: PRACTICAL FUNCTION EXAMPLES
print("\n\n5. PRACTICAL FUNCTION EXAMPLES")
print("-" * 40)

def validate_email(email):
    """Check if an email address looks valid"""
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    if len(email) < 5:
        return False
    if email.count('@') != 1:
        return False
    return True

def calculate_grade(score):
    """Convert numerical score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def format_phone_number(number):
    """Format a 10-digit phone number"""
    # Remove any non-digit characters
    digits = ''.join(char for char in number if char.isdigit())
    
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return "Invalid phone number"

def calculate_tip(bill_amount, tip_percentage=18):
    """Calculate tip amount and total bill"""
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    return tip, total

# Test practical functions
print("\nTesting practical functions:")

emails = ["user@example.com", "invalid.email", "test@site.org"]
for email in emails:
    is_valid = validate_email(email)
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"{email}: {status}")

scores = [95, 87, 72, 65, 45]
for score in scores:
    grade = calculate_grade(score)
    print(f"Score {score}: Grade {grade}")

phone_numbers = ["1234567890", "(555) 123-4567", "555.123.4567"]
for phone in phone_numbers:
    formatted = format_phone_number(phone)
    print(f"{phone} → {formatted}")

bill = 50.00
tip_amount, total_bill = calculate_tip(bill)
print(f"Bill: ${bill:.2f}, Tip: ${tip_amount:.2f}, Total: ${total_bill:.2f}")

# PART 6: FUNCTIONS WITH DEFAULT PARAMETERS
print("\n\n6. FUNCTIONS WITH DEFAULT PARAMETERS")
print("-" * 40)

print("Default parameters make functions more flexible!")

def create_user_profile(name, age, city="Unknown", country="USA"):
    """Create a user profile with optional city and country"""
    profile = {
        'name': name,
        'age': age,
        'city': city,
        'country': country
    }
    return profile

def send_notification(message, urgency="normal", send_email=True):
    """Send a notification with configurable options"""
    print(f"[{urgency.upper()}] {message}")
    if send_email:
        print("📧 Email notification sent")
    else:
        print("📱 SMS notification sent")

def generate_password(length=12, include_symbols=True, include_numbers=True):
    """Generate a random password with options"""
    import random
    import string
    
    chars = string.ascii_letters  # Always include letters
    
    if include_numbers:
        chars += string.digits
    
    if include_symbols:
        chars += "!@#$%^&*"
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Test default parameters
print("\nTesting functions with default parameters:")

profile1 = create_user_profile("Alice", 25)
print(f"Profile 1: {profile1}")

profile2 = create_user_profile("Bob", 30, "New York")
print(f"Profile 2: {profile2}")

profile3 = create_user_profile("Charlie", 35, "London", "UK")
print(f"Profile 3: {profile3}")

print("\nNotification examples:")
send_notification("System update completed")
send_notification("Critical error detected!", "urgent")
send_notification("Reminder: Meeting in 10 minutes", send_email=False)

print("\nPassword generation:")
print(f"Default password: {generate_password()}")
print(f"Simple password: {generate_password(8, False, True)}")
print(f"Complex password: {generate_password(16, True, True)}")

# PART 7: ORGANIZING CODE WITH FUNCTIONS
print("\n\n7. ORGANIZING CODE WITH FUNCTIONS")
print("-" * 40)

print("Functions help organize complex programs!")
print("Let's build a mini calculator using functions:")

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def get_number_input(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def display_menu():
    """Display calculator menu"""
    print("\n🧮 CALCULATOR MENU")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

def calculator():
    """Main calculator function"""
    print("🧮 Welcome to the Function Calculator!")
    
    while True:
        display_menu()
        choice = input("\nChoose operation (1-5): ")
        
        if choice == '5':
            print("Thanks for using the calculator! 👋")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice! Please select 1-5.")
            continue
        
        # Get numbers (using our helper function!)
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        # Perform calculation
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        
        print(f"\nResult: {num1} {operation} {num2} = {result}")

print("Calculator functions defined!")
print("💡 Notice how each function has a single, clear purpose!")
# Uncomment to test the calculator:
# calculator()

# PART 8: ERROR HANDLING IN FUNCTIONS
print("\n\n8. ERROR HANDLING IN FUNCTIONS")
print("-" * 40)

print("Good functions handle errors gracefully!")

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        if b == 0:
            return None, "Cannot divide by zero"
        result = a / b
        return result, "Success"
    except TypeError:
        return None, "Invalid input types"

def read_file_safely(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content, True
    except FileNotFoundError:
        return f"File '{filename}' not found", False
    except PermissionError:
        return f"Permission denied to read '{filename}'", False
    except Exception as e:
        return f"Unexpected error: {e}", False

def validate_user_input(data, required_fields):
    """Validate user input against required fields"""
    errors = []
    
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
        elif not data[field] or str(data[field]).strip() == "":
            errors.append(f"Field '{field}' cannot be empty")
    
    if errors:
        return False, errors
    else:
        return True, "All fields valid"

# Test error handling functions
print("\nTesting error handling functions:")

# Test safe division
test_divisions = [(10, 2), (5, 0), (8, "invalid")]
for a, b in test_divisions:
    result, message = safe_divide(a, b)
    print(f"safe_divide({a}, {b}): {result} ({message})")

# Test input validation
user_data = {'name': 'Alice', 'email': '', 'age': 25}
required = ['name', 'email', 'age']
is_valid, validation_result = validate_user_input(user_data, required)
print(f"\nValidation result: {is_valid}")
if not is_valid:
    for error in validation_result:
        print(f"  ❌ {error}")

# PART 9: ADVANCED FUNCTION CONCEPTS
print("\n\n9. ADVANCED FUNCTION CONCEPTS")
print("-" * 40)

def flexible_greeting(*names, greeting="Hello", punctuation="!"):
    """Greet multiple people with flexible parameters"""
    if not names:
        return f"{greeting}, everyone{punctuation}"
    
    name_list = ", ".join(names)
    return f"{greeting}, {name_list}{punctuation}"

def create_report(**data):
    """Create a report from keyword arguments"""
    report = "📊 REPORT\n" + "=" * 20 + "\n"
    
    for key, value in data.items():
        formatted_key = key.replace('_', ' ').title()
        report += f"{formatted_key}: {value}\n"
    
    return report

def apply_operation(numbers, operation):
    """Apply an operation function to a list of numbers"""
    results = []
    for i in range(len(numbers) - 1):
        result = operation(numbers[i], numbers[i + 1])
        results.append(result)
    return results

# Test advanced concepts
print("\nTesting advanced function concepts:")

print("Flexible greetings:")
print(flexible_greeting())
print(flexible_greeting("Alice"))
print(flexible_greeting("Bob", "Charlie", "Diana"))
print(flexible_greeting("Eve", "Frank", greeting="Good morning", punctuation="."))

print("\nDynamic reports:")
sales_report = create_report(
    total_sales=15000,
    new_customers=25,
    revenue_growth="12%",
    top_product="Python Course"
)
print(sales_report)

print("Function operations:")
numbers = [10, 5, 8, 3, 12]
addition_results = apply_operation(numbers, add)
print(f"Sequential additions: {addition_results}")

# PART 10: BUILDING A COMPLETE SYSTEM WITH FUNCTIONS
print("\n\n10. BUILDING A COMPLETE SYSTEM")
print("-" * 40)

print("Let's build a student management system using functions!")

# Data storage (in a real app, this would be a database or file)
students_database = []

def add_student(name, age, grade, subjects=None):
    """Add a new student to the database"""
    if subjects is None:
        subjects = []
    
    student = {
        'id': len(students_database) + 1,
        'name': name,
        'age': age,
        'grade': grade,
        'subjects': subjects,
        'scores': {},
        'created_date': str(datetime.date.today())
    }
    
    students_database.append(student)
    return student['id']

def find_student(student_id):
    """Find a student by ID"""
    for student in students_database:
        if student['id'] == student_id:
            return student
    return None

def add_score(student_id, subject, score):
    """Add a test score for a student"""
    student = find_student(student_id)
    if not student:
        return False, "Student not found"
    
    if not (0 <= score <= 100):
        return False, "Score must be between 0 and 100"
    
    if subject not in student['scores']:
        student['scores'][subject] = []
    
    student['scores'][subject].append(score)
    return True, "Score added successfully"

def calculate_student_average(student_id):
    """Calculate a student's overall average"""
    student = find_student(student_id)
    if not student:
        return None
    
    all_scores = []
    for subject_scores in student['scores'].values():
        all_scores.extend(subject_scores)
    
    if not all_scores:
        return 0
    
    return sum(all_scores) / len(all_scores)

def generate_student_report(student_id):
    """Generate a comprehensive report for a student"""
    student = find_student(student_id)
    if not student:
        return "Student not found"
    
    average = calculate_student_average(student_id)
    grade_letter = calculate_grade(average) if average > 0 else "No scores"
    
    report = f"""
📚 STUDENT REPORT
================
Name: {student['name']}
Age: {student['age']}
Grade Level: {student['grade']}
Student ID: {student['id']}
Enrolled: {student['created_date']}

📊 ACADEMIC PERFORMANCE
=======================
Overall Average: {average:.1f}%
Letter Grade: {grade_letter}

📝 SUBJECT SCORES
================="""
    
    if student['scores']:
        for subject, scores in student['scores'].items():
            subject_avg = sum(scores) / len(scores)
            report += f"\n{subject}: {scores} (Avg: {subject_avg:.1f}%)"
    else:
        report += "\nNo scores recorded yet"
    
    return report

def list_all_students():
    """List all students with basic info"""
    if not students_database:
        return "No students in database"
    
    result = "👥 ALL STUDENTS\n" + "=" * 20 + "\n"
    
    for student in students_database:
        average = calculate_student_average(student['id'])
        result += f"ID: {student['id']}, Name: {student['name']}, "
        result += f"Grade: {student['grade']}, Average: {average:.1f}%\n"
    
    return result

# Demo the student management system
import datetime

print("Demonstrating Student Management System:")

# Add some students
print("\nAdding students...")
id1 = add_student("Alice Johnson", 16, "10th", ["Math", "Science", "English"])
id2 = add_student("Bob Smith", 15, "9th", ["Math", "History", "Art"])
id3 = add_student("Charlie Brown", 17, "11th", ["Science", "English", "PE"])

print(f"Added students with IDs: {id1}, {id2}, {id3}")

# Add some scores
print("\nAdding test scores...")
add_score(id1, "Math", 92)
add_score(id1, "Math", 88)
add_score(id1, "Science", 95)
add_score(id1, "English", 87)

add_score(id2, "Math", 78)
add_score(id2, "History", 85)
add_score(id2, "Art", 92)

add_score(id3, "Science", 91)
add_score(id3, "English", 89)

# Generate reports
print("\nStudent listings:")
print(list_all_students())

print("\nDetailed report for Alice:")
print(generate_student_report(id1))

print("\n" + "="*60)
print("🎉 CONGRATULATIONS!")
print("You've mastered functions - the building blocks of great programs!")
print("Key concepts you've learned:")
print("• Creating reusable functions with def")
print("• Parameters and return values")
print("• Error handling and validation")
print("• Code organization and structure")
print("• Building complex systems from simple functions")
print("You're now ready to build amazing applications! 🚀")
print("="*60)