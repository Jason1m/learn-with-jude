# Session 8: Reference Guide - Functions

print("=" * 50)
print("SESSION 8: FUNCTIONS REFERENCE GUIDE")
print("=" * 50)

# TABLE OF CONTENTS
print("""
📚 COMPLETE FUNCTIONS REFERENCE

1. Function Basics
2. Parameters and Arguments
3. Return Values
4. Scope and Variables
5. Default Parameters
6. Error Handling in Functions
7. Advanced Function Concepts
8. Best Practices
9. Common Patterns
10. Debugging Functions
""")

# 1. FUNCTION BASICS
print("\n" + "="*40)
print("1. FUNCTION BASICS")
print("="*40)

print("""
📌 WHAT IS A FUNCTION?
A function is a reusable block of code that performs a specific task.
Functions help organize code, avoid repetition, and make programs easier to understand.

📌 FUNCTION SYNTAX:
def function_name(parameters):
    \"\"\"Optional docstring\"\"\"
    # Function body
    return value  # Optional

📌 FUNCTION PARTS:
• def - keyword to define a function
• function_name - what you call the function
• parameters - inputs to the function (optional)
• docstring - explains what the function does (optional but recommended)
• return - sends a value back (optional)
""")

# Basic function examples
def say_hello():
    """Simple function with no parameters"""
    print("Hello, World!")

def greet(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function with multiple parameters and return value"""
    result = a + b
    return result

print("Examples:")
print("say_hello() ->", end=" ")
say_hello()

print("greet('Python') ->", end=" ")
greet('Python')

print("add_numbers(5, 3) ->", add_numbers(5, 3))

# 2. PARAMETERS AND ARGUMENTS
print("\n" + "="*40)
print("2. PARAMETERS AND ARGUMENTS")
print("="*40)

print("""
📌 PARAMETERS vs ARGUMENTS:
• Parameters: Variables in the function definition
• Arguments: Actual values passed when calling the function

📌 TYPES OF PARAMETERS:
1. Positional parameters - order matters
2. Keyword parameters - order doesn't matter
3. Default parameters - have default values
4. Variable-length parameters - *args, **kwargs
""")

# Parameter examples
def create_person(name, age, city):
    """Function with positional parameters"""
    return f"{name} is {age} years old and lives in {city}"

def introduce(name, age=25, hobby="reading"):
    """Function with default parameters"""
    return f"Hi, I'm {name}, {age} years old, and I love {hobby}"

def flexible_function(*args, **kwargs):
    """Function with variable arguments"""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print("\nExamples:")
print("Positional arguments:")
print(create_person("Alice", 30, "New York"))

print("\nKeyword arguments:")
print(create_person(city="Boston", name="Bob", age=25))

print("\nDefault parameters:")
print(introduce("Charlie"))
print(introduce("Diana", 28))
print(introduce("Eve", 22, "painting"))

print("\nVariable arguments:")
flexible_function(1, 2, 3, name="Frank", age=35)

# 3. RETURN VALUES
print("\n" + "="*40)
print("3. RETURN VALUES")
print("="*40)

print("""
📌 RETURN STATEMENT:
• Functions can return values using the 'return' statement
• If no return statement, function returns None
• Can return any data type: numbers, strings, lists, dictionaries, etc.
• Can return multiple values (as a tuple)

📌 RETURN TYPES:
1. Single value
2. Multiple values (tuple)
3. Complex data structures
4. None (implicit or explicit)
""")

def calculate_circle(radius):
    """Return single value"""
    area = 3.14159 * radius ** 2
    return area

def calculate_rectangle(length, width):
    """Return multiple values"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def analyze_numbers(numbers):
    """Return complex data structure"""
    if not numbers:
        return None
    
    analysis = {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }
    return analysis

def print_message(text):
    """Function that returns None"""
    print(text)
    # No return statement = returns None

print("\nExamples:")
circle_area = calculate_circle(5)
print(f"Circle area: {circle_area}")

area, perimeter = calculate_rectangle(4, 6)
print(f"Rectangle - Area: {area}, Perimeter: {perimeter}")

numbers = [1, 5, 3, 9, 2, 8]
stats = analyze_numbers(numbers)
print(f"Number analysis: {stats}")

result = print_message("This function returns None")
print(f"Return value: {result}")

# 4. SCOPE AND VARIABLES
print("\n" + "="*40)
print("4. SCOPE AND VARIABLES")
print("="*40)

print("""
📌 VARIABLE SCOPE:
• Local scope - variables inside functions
• Global scope - variables outside functions
• Function parameters are local variables
• Use 'global' keyword to modify global variables

📌 SCOPE RULES:
1. Local variables are created when function is called
2. Local variables are destroyed when function ends
3. Functions can read global variables
4. Functions need 'global' keyword to modify global variables
""")

# Global variable
global_counter = 0

def local_example():
    """Demonstrate local variables"""
    local_variable = "I'm local!"
    print(f"Inside function: {local_variable}")
    return local_variable

def global_read_example():
    """Read global variable"""
    print(f"Reading global counter: {global_counter}")

def global_modify_example():
    """Modify global variable"""
    global global_counter
    global_counter += 1
    print(f"Modified global counter: {global_counter}")

def scope_example(parameter):
    """Demonstrate parameter scope"""
    parameter = "Modified inside function"
    local_var = "Local variable"
    print(f"Parameter: {parameter}")
    print(f"Local: {local_var}")

print("\nScope Examples:")
result = local_example()
# print(local_variable)  # This would cause an error!

global_read_example()
global_modify_example()
global_modify_example()

original = "Original value"
scope_example(original)
print(f"Outside function: {original}")  # Still original value

# 5. DEFAULT PARAMETERS
print("\n" + "="*40)
print("5. DEFAULT PARAMETERS")
print("="*40)

print("""
📌 DEFAULT PARAMETERS:
• Parameters can have default values
• Used when no argument is provided
• Must come after non-default parameters
• Evaluated once when function is defined

📌 BEST PRACTICES:
• Use immutable defaults (numbers, strings, None)
• Avoid mutable defaults (lists, dictionaries)
• Use None and create new objects inside function
""")

def greet_user(name, greeting="Hello", punctuation="!"):
    """Function with multiple default parameters"""
    return f"{greeting}, {name}{punctuation}"

def add_to_list(item, target_list=None):
    """Safe way to use mutable defaults"""
    if target_list is None:
        target_list = []
    
    target_list.append(item)
    return target_list

def create_config(debug=False, timeout=30, retries=3):
    """Configuration function with defaults"""
    config = {
        'debug': debug,
        'timeout': timeout,
        'retries': retries
    }
    return config

print("\nDefault Parameter Examples:")
print(greet_user("Alice"))
print(greet_user("Bob", "Hi"))
print(greet_user("Charlie", "Hey", "!!!"))

list1 = add_to_list("apple")
list2 = add_to_list("banana")
print(f"List 1: {list1}")
print(f"List 2: {list2}")

config1 = create_config()
config2 = create_config(debug=True, timeout=60)
print(f"Config 1: {config1}")
print(f"Config 2: {config2}")

# 6. ERROR HANDLING IN FUNCTIONS
print("\n" + "="*40)
print("6. ERROR HANDLING IN FUNCTIONS")
print("="*40)

print("""
📌 ERROR HANDLING:
• Use try/except blocks to handle errors gracefully
• Return error indicators (None, False, error messages)
• Validate input parameters
• Use meaningful error messages

📌 COMMON PATTERNS:
1. Return (result, error) tuple
2. Return None on error
3. Raise custom exceptions
4. Log errors for debugging
""")

def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return None, "Both inputs must be numbers"
        
        if b == 0:
            return None, "Cannot divide by zero"
        
        result = a / b
        return result, None
    
    except Exception as e:
        return None, f"Unexpected error: {e}"

def validate_email(email):
    """Simple email validation"""
    if not email or not isinstance(email, str):
        return False, "Email must be a non-empty string"
    
    if '@' not in email:
        return False, "Email must contain @"
    
    if '.' not in email.split('@')[1]:
        return False, "Email domain must contain ."
    
    return True, "Valid email"

def process_age(age_str):
    """Process age string with validation"""
    try:
        age = int(age_str)
        
        if age < 0:
            return None, "Age cannot be negative"
        
        if age > 150:
            return None, "Age seems unrealistic"
        
        return age, None
    
    except ValueError:
        return None, "Age must be a valid number"

print("\nError Handling Examples:")
result, error = safe_divide(10, 2)
print(f"10 ÷ 2: Result={result}, Error={error}")

result, error = safe_divide(10, 0)
print(f"10 ÷ 0: Result={result}, Error={error}")

result, error = safe_divide("10", 2)
print(f"'10' ÷ 2: Result={result}, Error={error}")

valid, message = validate_email("user@example.com")
print(f"Email validation: {valid}, {message}")

valid, message = validate_email("invalid-email")
print(f"Email validation: {valid}, {message}")

age, error = process_age("25")
print(f"Age '25': {age}, {error}")

age, error = process_age("abc")
print(f"Age 'abc': {age}, {error}")

# 7. ADVANCED FUNCTION CONCEPTS
print("\n" + "="*40)
print("7. ADVANCED FUNCTION CONCEPTS")
print("="*40)

print("""
📌 ADVANCED CONCEPTS:
1. Recursion - functions calling themselves
2. Higher-order functions - functions that take/return functions
3. Lambda functions - anonymous functions
4. Decorators - functions that modify other functions
5. Generators - functions that yield values

📌 WHEN TO USE:
• Recursion: Tree structures, mathematical sequences
• Higher-order: Functional programming, callbacks
• Lambda: Short, simple operations
• Decorators: Adding functionality to existing functions
• Generators: Large datasets, memory efficiency
""")

def factorial(n):
    """Recursive function example"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def apply_operation(numbers, operation_func):
    """Higher-order function example"""
    return [operation_func(x) for x in numbers]

def square(x):
    """Function to use with higher-order function"""
    return x ** 2

def create_multiplier(factor):
    """Function factory - returns a function"""
    def multiplier(x):
        return x * factor
    return multiplier

def simple_generator(n):
    """Generator function example"""
    for i in range(n):
        yield i ** 2

print("\nAdvanced Examples:")
print(f"Factorial of 5: {factorial(5)}")

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
print(f"Squared numbers: {squared}")

# Using lambda function
doubled = apply_operation(numbers, lambda x: x * 2)
print(f"Doubled numbers: {doubled}")

# Function factory
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"Double 7: {double(7)}")
print(f"Triple 7: {triple(7)}")

# Generator
squares = list(simple_generator(5))
print(f"First 5 squares: {squares}")

# 8. BEST PRACTICES
print("\n" + "="*40)
print("8. BEST PRACTICES")
print("="*40)

print("""
📌 FUNCTION DESIGN PRINCIPLES:

1. SINGLE RESPONSIBILITY
   • Each function should do one thing well
   • If you can't explain it in one sentence, it's too complex

2. MEANINGFUL NAMES
   • Use descriptive function names
   • Use verb phrases: calculate_total, validate_input
   • Avoid abbreviations: calc_tot → calculate_total

3. PARAMETER GUIDELINES
   • Keep parameter count low (max 3-4)
   • Use meaningful parameter names
   • Consider using dictionaries for many parameters

4. DOCUMENTATION
   • Always include docstrings
   • Explain what the function does
   • Document parameters and return values
   • Include examples if complex

5. ERROR HANDLING
   • Validate inputs
   • Handle edge cases
   • Return consistent error indicators
   • Don't let functions crash silently

6. TESTING
   • Test with normal inputs
   • Test edge cases (empty lists, zero values)
   • Test error conditions
   • Write unit tests
""")

# Good function example
def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculate monthly mortgage payment.
    
    Args:
        principal (float): Loan amount in dollars
        annual_rate (float): Annual interest rate (e.g., 0.05 for 5%)
        years (int): Loan term in years
    
    Returns:
        float: Monthly payment amount, or None if invalid input
        
    Example:
        >>> calculate_monthly_payment(200000, 0.05, 30)
        1073.64
    """
    # Validate inputs
    if principal <= 0 or annual_rate < 0 or years <= 0:
        return None
    
    # Handle zero interest rate
    if annual_rate == 0:
        return principal / (years * 12)
    
    # Calculate monthly payment
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return round(payment, 2)

print("\nBest Practice Example:")
payment = calculate_monthly_payment(200000, 0.05, 30)
print(f"Monthly payment: ${payment}")

# 9. COMMON PATTERNS
print("\n" + "="*40)
print("9. COMMON PATTERNS")
print("="*40)

print("""
📌 USEFUL FUNCTION PATTERNS:

1. VALIDATOR PATTERN
   • Return (is_valid, error_message)
   • Consistent error handling

2. PROCESSOR PATTERN
   • Return (result, error)
   • None result indicates error

3. BUILDER PATTERN
   • Functions that create complex objects
   • Step-by-step construction

4. FACTORY PATTERN
   • Functions that create other functions
   • Customizable behavior

5. CONVERTER PATTERN
   • Transform data from one format to another
   • Input validation and error handling
""")

# Validator pattern
def validate_password(password):
    """Validate password strength"""
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    if not any(c.isupper() for c in password):
        errors.append("Password must contain uppercase letter")
    
    if not any(c.islower() for c in password):
        errors.append("Password must contain lowercase letter")
    
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain a number")
    
    is_valid = len(errors) == 0
    return is_valid, errors

# Processor pattern
def process_grade(score):
    """Convert numeric score to letter grade"""
    try:
        score = float(score)
        
        if score < 0 or score > 100:
            return None, "Score must be between 0 and 100"
        
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        
        return grade, None
        
    except ValueError:
        return None, "Score must be a number"

# Builder pattern
def build_student_record():
    """Build a complete student record step by step"""
    student = {}
    
    # Get basic info
    student['name'] = input("Student name: ").strip()
    student['id'] = input("Student ID: ").strip()
    student['email'] = input("Email: ").strip()
    
    # Initialize collections
    student['courses'] = []
    student['grades'] = {}
    
    # Add metadata
    student['created_date'] = "2024-01-01"  # In real app, use datetime
    student['status'] = "active"
    
    return student

print("\nPattern Examples:")
valid, errors = validate_password("MyPass123")
print(f"Password valid: {valid}")
if errors:
    print("Errors:", errors)

grade, error = process_grade("85")
print(f"Grade: {grade}, Error: {error}")

grade, error = process_grade("150")
print(f"Grade: {grade}, Error: {error}")

# 10. DEBUGGING FUNCTIONS
print("\n" + "="*40)
print("10. DEBUGGING FUNCTIONS")
print("="*40)

print("""
📌 DEBUGGING TECHNIQUES:

1. PRINT DEBUGGING
   • Add print statements to see variable values
   • Print at function entry and exit
   • Print intermediate calculations

2. RETURN VALUE CHECKING
   • Always check what your functions return
   • Use type() to verify return types
   • Test with different inputs

3. PARAMETER VALIDATION
   • Print parameter values at start of function
   • Check parameter types and ranges
   • Test edge cases

4. STEP-BY-STEP TESTING
   • Test functions individually
   • Build complex functions from simple ones
   • Use temporary variables to break down calculations

5. COMMON ISSUES
   • Wrong indentation
   • Missing return statements
   • Incorrect parameter order
   • Variable scope problems
   • Mutable default parameters
""")

def debug_example(numbers):
    """Example function with debugging statements"""
    print(f"DEBUG: Function called with {numbers}")
    print(f"DEBUG: Type of input: {type(numbers)}")
    
    if not numbers:
        print("DEBUG: Empty list detected")
        return 0
    
    total = 0
    for i, num in enumerate(numbers):
        print(f"DEBUG: Processing item {i}: {num}")
        total += num
        print(f"DEBUG: Running total: {total}")
    
    print(f"DEBUG: Final result: {total}")
    return total

def test_function():
    """Function to test our debug example"""
    test_cases = [
        [1, 2, 3, 4, 5],
        [],
        [10],
        [-1, -2, -3]
    ]
    
    for case in test_cases:
        print(f"\nTesting with: {case}")
        result = debug_example(case)
        print(f"Result: {result}")

print("\nDebugging Example:")
print("(Comment out debug prints in production!)")
result = debug_example([1, 2, 3])

# QUICK REFERENCE
print("\n" + "="*50)
print("📋 QUICK REFERENCE CARD")
print("="*50)

print("""
FUNCTION SYNTAX:
def function_name(param1, param2=default):
    \"\"\"Docstring explaining the function\"\"\"
    # Function body
    return result

CALLING FUNCTIONS:
result = function_name(arg1, arg2)
result = function_name(arg1, param2=arg2)

COMMON PATTERNS:
• Input validation: if not valid_input: return None
• Error handling: try/except with meaningful messages
• Multiple returns: return value, error
• Default parameters: param=None, then check inside function

DEBUGGING CHECKLIST:
□ Function has correct indentation
□ Return statement present (if needed)
□ Parameters in correct order
□ Variables in correct scope
□ Default parameters are immutable
□ Error cases handled
□ Function does one thing well
□ Meaningful names used
□ Docstring explains purpose
""")

print("\n" + "="*50)
print("🎯 FUNCTIONS MASTERY COMPLETE!")
print("You now know everything about Python functions!")
print("Keep practicing and building amazing things! 🚀")
print("="*50)