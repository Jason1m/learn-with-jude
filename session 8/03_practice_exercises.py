# Session 8: Practice Exercises - Functions

print("=" * 50)
print("SESSION 8: PRACTICE EXERCISES - FUNCTIONS")
print("=" * 50)

print("Let's practice everything we've learned about functions!")

# EXERCISE 1: Basic Function Creation
print("\n" + "="*30)
print("EXERCISE 1: BASIC FUNCTIONS")
print("="*30)

def greet_user(name):
    """Return a personalized greeting"""
    return f"Hello, {name}! Welcome to Python functions!"

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def get_grade(score):
    """Convert numeric score to letter grade"""
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

# Test the basic functions
print("Testing basic functions:")
print("Greeting:", greet_user("Student"))
print("Area of 5x3 rectangle:", calculate_area(5, 3))
print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))
print("Grade for 85:", get_grade(85))

# EXERCISE 2: Functions with Default Parameters
print("\n" + "="*40)
print("EXERCISE 2: DEFAULT PARAMETERS")
print("="*40)

def create_profile(name, age=18, city="Unknown", hobby="Reading"):
    """Create a user profile with default values"""
    profile = {
        'name': name,
        'age': age,
        'city': city,
        'hobby': hobby
    }
    return profile

def calculate_total(price, tax_rate=0.08, tip_rate=0.15):
    """Calculate total with tax and tip"""
    tax = price * tax_rate
    tip = price * tip_rate
    total = price + tax + tip
    return {
        'subtotal': price,
        'tax': tax,
        'tip': tip,
        'total': total
    }

def format_name(first, last, middle=""):
    """Format a person's full name"""
    if middle:
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"

# Test default parameters
print("Testing default parameters:")
print("Profile 1:", create_profile("Alice"))
print("Profile 2:", create_profile("Bob", 25, "New York"))
print("Profile 3:", create_profile("Charlie", 30, "Boston", "Gaming"))

bill = calculate_total(50.00)
print(f"Bill total: ${bill['total']:.2f}")

print("Name 1:", format_name("John", "Doe"))
print("Name 2:", format_name("Jane", "Smith", "Marie"))

# EXERCISE 3: Functions with Lists and Dictionaries
print("\n" + "="*40)
print("EXERCISE 3: LISTS AND DICTIONARIES")
print("="*40)

def find_maximum(numbers):
    """Find the maximum number in a list"""
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def count_words(text):
    """Count words in a text string"""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        # Remove punctuation
        clean_word = ''.join(char for char in word if char.isalpha())
        if clean_word:
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1
    
    return word_count

def filter_students(students, min_grade=70):
    """Filter students by minimum grade"""
    passing_students = []
    
    for student in students:
        if student['grade'] >= min_grade:
            passing_students.append(student)
    
    return passing_students

def average_score(scores):
    """Calculate average of a list of scores"""
    if not scores:
        return 0
    
    total = sum(scores)
    return total / len(scores)

# Test list and dictionary functions
print("Testing list and dictionary functions:")

numbers = [3, 7, 2, 9, 1, 8, 5]
print("Numbers:", numbers)
print("Maximum:", find_maximum(numbers))

text = "The quick brown fox jumps over the lazy dog. The dog was sleeping."
word_counts = count_words(text)
print("Word counts:", word_counts)

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 67},
    {'name': 'Diana', 'grade': 78},
    {'name': 'Eve', 'grade': 94}
]

passing = filter_students(students, 75)
print("Students with grade >= 75:", [s['name'] for s in passing])

scores = [85, 92, 78, 96, 88]
print("Scores:", scores)
print("Average:", average_score(scores))

# EXERCISE 4: Error Handling in Functions
print("\n" + "="*35)
print("EXERCISE 4: ERROR HANDLING")
print("="*35)

def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result, None
    except ZeroDivisionError:
        return None, "Cannot divide by zero"
    except TypeError:
        return None, "Both inputs must be numbers"

def safe_list_access(lst, index):
    """Safely access a list element"""
    try:
        return lst[index], None
    except IndexError:
        return None, f"Index {index} is out of range"
    except TypeError:
        return None, "Invalid index type"

def parse_number(text):
    """Try to convert text to a number"""
    try:
        # Try integer first
        if '.' not in text:
            return int(text), "integer"
        else:
            return float(text), "float"
    except ValueError:
        return None, "Not a valid number"

# Test error handling
print("Testing error handling:")

result, error = safe_divide(10, 2)
print(f"10 ÷ 2 = {result}, error: {error}")

result, error = safe_divide(10, 0)
print(f"10 ÷ 0 = {result}, error: {error}")

my_list = [1, 2, 3, 4, 5]
result, error = safe_list_access(my_list, 2)
print(f"List[2] = {result}, error: {error}")

result, error = safe_list_access(my_list, 10)
print(f"List[10] = {result}, error: {error}")

num, num_type = parse_number("42")
print(f"Parse '42': {num} ({num_type})")

num, num_type = parse_number("3.14")
print(f"Parse '3.14': {num} ({num_type})")

num, num_type = parse_number("hello")
print(f"Parse 'hello': {num} ({num_type})")

# EXERCISE 5: Advanced Function Concepts
print("\n" + "="*35)
print("EXERCISE 5: ADVANCED CONCEPTS")
print("="*35)

def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list"""
    result = []
    for num in numbers:
        if operation == "square":
            result.append(num ** 2)
        elif operation == "double":
            result.append(num * 2)
        elif operation == "half":
            result.append(num / 2)
        else:
            result.append(num)
    return result

def create_multiplier(factor):
    """Create a function that multiplies by a specific factor"""
    def multiply(x):
        return x * factor
    return multiply

# Test advanced concepts
print("Testing advanced concepts:")

print("Fibonacci sequence (first 8 numbers):")
for i in range(8):
    print(f"F({i}) = {fibonacci(i)}")

print(f"\nFactorial of 5: {factorial(5)}")
print(f"Factorial of 6: {factorial(6)}")

numbers = [1, 2, 3, 4, 5]
print(f"\nOriginal numbers: {numbers}")
print(f"Squared: {apply_operation(numbers, 'square')}")
print(f"Doubled: {apply_operation(numbers, 'double')}")
print(f"Halved: {apply_operation(numbers, 'half')}")

# Function factory example
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"\nUsing function factory:")
print(f"Double 7: {double(7)}")
print(f"Triple 7: {triple(7)}")

# EXERCISE 6: Building a Mini Calculator
print("\n" + "="*40)
print("EXERCISE 6: MINI CALCULATOR")
print("="*40)

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def calculator(operation, num1, num2):
    """Perform a calculation based on operation"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power
    }
    
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        return "Error: Unknown operation"

def advanced_calculator():
    """Interactive calculator function"""
    print("🧮 Advanced Calculator")
    print("Available operations: +, -, *, /, **")
    print("Type 'quit' to exit")
    
    while True:
        try:
            expression = input("\nEnter calculation (e.g., 5 + 3): ").strip()
            
            if expression.lower() == 'quit':
                print("Calculator closed. Goodbye!")
                break
            
            # Parse the expression
            parts = expression.split()
            if len(parts) != 3:
                print("Format: number operator number")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            result = calculator(operator, num1, num2)
            print(f"Result: {result}")
            
        except ValueError:
            print("Error: Please use valid numbers")
        except Exception as e:
            print(f"Error: {e}")

# Test the calculator
print("Testing calculator functions:")
print(f"5 + 3 = {calculator('+', 5, 3)}")
print(f"10 - 4 = {calculator('-', 10, 4)}")
print(f"6 * 7 = {calculator('*', 6, 7)}")
print(f"15 / 3 = {calculator('/', 15, 3)}")
print(f"2 ** 8 = {calculator('**', 2, 8)}")
print(f"10 / 0 = {calculator('/', 10, 0)}")

print("\n💡 Uncomment the line below to try the interactive calculator:")
print("# advanced_calculator()")

# EXERCISE 7: Student Information System
print("\n" + "="*45)
print("EXERCISE 7: STUDENT INFORMATION SYSTEM")
print("="*45)

def create_student(name, age, grade_level):
    """Create a new student record"""
    return {
        'name': name,
        'age': age,
        'grade_level': grade_level,
        'courses': [],
        'grades': {}
    }

def add_course(student, course_name):
    """Add a course to a student's schedule"""
    if course_name not in student['courses']:
        student['courses'].append(course_name)
        student['grades'][course_name] = []
        return f"Added {course_name} to {student['name']}'s schedule"
    else:
        return f"{student['name']} is already enrolled in {course_name}"

def add_grade(student, course_name, grade):
    """Add a grade for a specific course"""
    if course_name in student['courses']:
        student['grades'][course_name].append(grade)
        return f"Added grade {grade} for {course_name}"
    else:
        return f"{student['name']} is not enrolled in {course_name}"

def calculate_course_average(student, course_name):
    """Calculate average grade for a specific course"""
    if course_name not in student['grades']:
        return None
    
    grades = student['grades'][course_name]
    if not grades:
        return None
    
    return sum(grades) / len(grades)

def calculate_gpa(student):
    """Calculate overall GPA"""
    total_points = 0
    total_courses = 0
    
    for course, grades in student['grades'].items():
        if grades:
            avg = sum(grades) / len(grades)
            total_points += avg
            total_courses += 1
    
    if total_courses == 0:
        return 0
    
    return total_points / total_courses

def get_student_report(student):
    """Generate a comprehensive student report"""
    report = f"\n📊 STUDENT REPORT: {student['name']}\n"
    report += "=" * 40 + "\n"
    report += f"Age: {student['age']}\n"
    report += f"Grade Level: {student['grade_level']}\n"
    report += f"Courses Enrolled: {len(student['courses'])}\n\n"
    
    if student['courses']:
        report += "COURSE DETAILS:\n"
        for course in student['courses']:
            grades = student['grades'][course]
            if grades:
                avg = calculate_course_average(student, course)
                report += f"• {course}: {grades} (Average: {avg:.1f})\n"
            else:
                report += f"• {course}: No grades yet\n"
        
        gpa = calculate_gpa(student)
        report += f"\nOverall GPA: {gpa:.2f}\n"
    else:
        report += "No courses enrolled yet.\n"
    
    return report

# Test the student system
print("Testing student information system:")

# Create a student
alice = create_student("Alice Johnson", 16, "10th Grade")
print(f"Created student: {alice['name']}")

# Add courses
print(add_course(alice, "Mathematics"))
print(add_course(alice, "English"))
print(add_course(alice, "Science"))

# Add grades
print(add_grade(alice, "Mathematics", 85))
print(add_grade(alice, "Mathematics", 92))
print(add_grade(alice, "Mathematics", 88))

print(add_grade(alice, "English", 78))
print(add_grade(alice, "English", 82))

print(add_grade(alice, "Science", 95))
print(add_grade(alice, "Science", 89))
print(add_grade(alice, "Science", 92))

# Generate report
print(get_student_report(alice))

# PRACTICE CHALLENGES
print("\n" + "="*50)
print("🎯 PRACTICE CHALLENGES FOR YOU!")
print("="*50)

print("""
Try these challenges to master functions:

CHALLENGE 1: Password Validator
Create a function that validates passwords with these rules:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Returns True/False and a list of any issues

CHALLENGE 2: Text Analyzer
Create functions to analyze text:
- Count sentences (periods, exclamation marks, question marks)
- Find the longest word
- Calculate reading time (assume 200 words per minute)
- Identify the most common word

CHALLENGE 3: Shopping Cart System
Build functions for an online shopping cart:
- add_item(cart, item_name, price, quantity)
- remove_item(cart, item_name)
- calculate_total(cart, tax_rate)
- apply_discount(cart, discount_percent)
- generate_receipt(cart)

CHALLENGE 4: Number Game
Create a guessing game with functions:
- generate_random_number(min, max)
- check_guess(guess, target)
- play_game() - main game loop
- get_difficulty_level() - easy/medium/hard

CHALLENGE 5: Data Analysis
Create functions to analyze a list of dictionaries:
- find_oldest_person(people)
- group_by_age_range(people)
- calculate_statistics(numbers)
- find_duplicates(items)

Remember:
• Start small and build up
• Test each function individually
• Use meaningful function and parameter names
• Add docstrings to explain what each function does
• Handle edge cases and errors gracefully

Happy coding! 🚀
""")

print("\n" + "="*50)
print("✅ EXERCISES COMPLETE!")
print("You've practiced:")
print("• Creating and calling functions")
print("• Using parameters and return values")
print("• Default parameters")
print("• Working with lists and dictionaries")
print("• Error handling")
print("• Advanced function concepts")
print("• Building real applications")
print("")
print("Keep practicing and you'll be a function master! 🎉")
print("="*50)