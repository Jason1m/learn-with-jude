# Session 4: Making Decisions (if, else) - Reference Guide

## Quick Reference: If/Else Statements

### Basic Syntax
```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if no conditions are True
```

### Comparison Operators
| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `name != "John"` |
| `>` | Greater than | `score > 90` |
| `<` | Less than | `temperature < 32` |
| `>=` | Greater than or equal | `age >= 21` |
| `<=` | Less than or equal | `grade <= 100` |

### Logical Operators
| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both conditions true | `age >= 18 and has_license` |
| `or` | At least one condition true | `day == "Saturday" or day == "Sunday"` |
| `not` | Reverses condition | `not is_raining` |

### Common Patterns

#### Simple If Statement
```python
if age >= 18:
    print("You are an adult")
```

#### If-Else Statement
```python
if temperature > 75:
    print("It's warm outside")
else:
    print("It's cool outside")
```

#### If-Elif-Else Chain
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

#### Multiple Conditions with AND
```python
if age >= 16 and has_permit:
    print("You can drive!")
```

#### Multiple Conditions with OR
```python
if weather == "rain" or weather == "snow":
    print("Take an umbrella!")
```

#### Nested If Statements
```python
if weather == "sunny":
    if temperature > 80:
        print("Perfect beach weather!")
    else:
        print("Nice day for a walk!")
```

### Data Type Specific Conditions

#### String Comparisons
```python
# Case sensitive
if name == "Alice":
    print("Hello Alice!")

# Case insensitive
if name.lower() == "alice":
    print("Hello Alice!")

# Check if string contains something
if "python" in message.lower():
    print("This is about Python!")
```

#### Number Ranges
```python
# Check if number is in range
if 18 <= age <= 65:
    print("Working age")

# Multiple range checks
if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
```

#### List/Collection Checks
```python
# Check if item is in list
if "apple" in fruits:
    print("We have apples!")

# Check if list is empty
if not shopping_list:
    print("Shopping list is empty")

# Check list length
if len(students) > 20:
    print("Large class size")
```

### Input Validation Patterns

#### Validate Numbers
```python
try:
    age = int(input("Enter age: "))
    if age < 0:
        print("Age cannot be negative")
    elif age > 150:
        print("Please enter a realistic age")
    else:
        print(f"Age: {age}")
except ValueError:
    print("Please enter a valid number")
```

#### Validate String Input
```python
choice = input("Enter choice (y/n): ").lower()
if choice in ["y", "yes"]:
    print("You chose yes")
elif choice in ["n", "no"]:
    print("You chose no")
else:
    print("Invalid choice")
```

### Common Mistakes to Avoid

#### 1. Using = instead of ==
```python
# WRONG
if age = 18:  # This assigns, doesn't compare!

# CORRECT
if age == 18:  # This compares
```

#### 2. Forgetting the colon
```python
# WRONG
if age >= 18
    print("Adult")

# CORRECT
if age >= 18:
    print("Adult")
```

#### 3. Incorrect indentation
```python
# WRONG
if age >= 18:
print("Adult")  # Not indented!

# CORRECT
if age >= 18:
    print("Adult")  # Properly indented
```

#### 4. Operator precedence confusion
```python
# Be careful with complex conditions
if age > 18 and score > 80 or grade == "A":
    # This might not work as expected

# Use parentheses for clarity
if (age > 18 and score > 80) or grade == "A":
    # Much clearer
```

### Useful Built-in Functions for Conditions

#### String Methods
```python
text = "Hello World"
if text.isdigit():      # Check if all digits
if text.isalpha():      # Check if all letters
if text.startswith("H"): # Check if starts with
if text.endswith("d"):   # Check if ends with
```

#### Type Checking
```python
if isinstance(value, int):    # Check if integer
if isinstance(value, str):    # Check if string
if isinstance(value, list):   # Check if list
```

### Performance Tips

#### Use elif instead of multiple ifs
```python
# LESS EFFICIENT - checks all conditions
if score >= 90:
    grade = "A"
if score >= 80 and score < 90:
    grade = "B"
if score >= 70 and score < 80:
    grade = "C"

# MORE EFFICIENT - stops at first match
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
```

#### Order conditions by likelihood
```python
# Put most common conditions first
if weather == "sunny":      # Most common
    # handle sunny
elif weather == "cloudy":   # Less common
    # handle cloudy
elif weather == "hurricane": # Very rare
    # handle hurricane
```

### Real-World Examples

#### User Authentication
```python
def authenticate_user(username, password):
    if not username or not password:
        return "Username and password required"
    elif len(password) < 8:
        return "Password too short"
    elif username == "admin" and password == "secret123":
        return "Login successful"
    else:
        return "Invalid credentials"
```

#### Grade Calculator
```python
def calculate_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid score type"
    elif score < 0 or score > 100:
        return "Score must be between 0-100"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

#### Shopping Cart Discount
```python
def calculate_discount(total, is_member, coupon_code):
    discount = 0
    
    if is_member:
        discount += 0.10  # 10% member discount
    
    if coupon_code == "SAVE20":
        discount += 0.20  # 20% coupon discount
    elif coupon_code == "SAVE10":
        discount += 0.10  # 10% coupon discount
    
    if total > 100:
        discount += 0.05  # 5% bulk discount
    
    # Cap maximum discount at 50%
    if discount > 0.50:
        discount = 0.50
    
    return total * (1 - discount)
```

## Practice Exercises Summary

From this session, you should be able to:
- [ ] Write basic if statements
- [ ] Use comparison operators correctly
- [ ] Chain conditions with elif and else
- [ ] Combine conditions with and, or, not
- [ ] Validate user input
- [ ] Handle different data types in conditions
- [ ] Avoid common syntax errors
- [ ] Write clean, readable conditional logic

## Next Steps
- Practice with the provided exercises
- Try building your own decision-making programs
- Experiment with nested conditions
- Learn about loops (coming in the next session!)

Remember: Good conditional logic makes programs smart and user-friendly!