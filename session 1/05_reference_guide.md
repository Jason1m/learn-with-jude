# Session 1: Quick Reference Guide

## 📚 Python Basics Quick Reference

### The `print()` Function
**Purpose:** Display text or values on the screen

```python
# Basic usage
print("Hello, World!")
print(42)

# Multiple items
print("Name:", "Alice")
print("Score:", 95)

# Empty line
print()
```

**Key Points:**
- Text (strings) must be in quotes: `"hello"` or `'hello'`
- Numbers don't need quotes: `42`
- Each `print()` creates a new line

---

### The `input()` Function
**Purpose:** Get text input from the user

```python
# Basic usage
name = input("What's your name? ")
age = input("How old are you? ")

# Using the input
print("Hello, " + name + "!")
```

**Key Points:**
- Always returns text (string), even if user types numbers
- Store the result in a variable to use it later
- The text in parentheses is the prompt shown to user

---

### Variables
**Purpose:** Store information to use later

```python
# Creating variables
student_name = "Alice"
student_age = 16
favorite_color = "blue"

# Using variables
print("Hello, " + student_name)
print("You are " + str(student_age) + " years old")
```

**Naming Rules:**
- ✅ Use letters, numbers, underscore: `first_name`, `score2`
- ✅ Start with letter or underscore: `_private`, `name`
- ✅ Use descriptive names: `student_name` not `sn`
- ❌ No spaces: `first name` (wrong)
- ❌ No special characters: `first-name`, `first@name` (wrong)
- ❌ Don't start with numbers: `2students` (wrong)

---

### Working with Strings (Text)
**Purpose:** Handle text data

```python
# Creating strings
first_name = "John"
last_name = "Smith"

# Joining strings (concatenation)
full_name = first_name + " " + last_name
greeting = "Hello, " + first_name + "!"

# String methods
name = "alice"
print(name.upper())    # ALICE
print(name.lower())    # alice
print(len(name))       # 5 (length)
```

**Key Points:**
- Use `+` to join strings together
- Remember to add spaces: `"Hello" + " " + "World"`
- `.lower()` makes text lowercase
- `.upper()` makes text UPPERCASE

---

### Working with Numbers
**Purpose:** Handle numeric data and math

```python
# Creating number variables
score = 85
age = 16
year = 2024

# Math operations
total = score + 10
difference = 100 - score
doubled = score * 2
average = total / 2

# Converting between text and numbers
user_input = input("Enter a number: ")  # This is text!
number = int(user_input)                # Convert to integer
result = number * 2

# Converting numbers to text
age = 16
message = "I am " + str(age) + " years old"
```

**Math Operators:**
- `+` Addition
- `-` Subtraction  
- `*` Multiplication
- `/` Division

**Conversion Functions:**
- `int()` - Convert to whole number
- `str()` - Convert to text
- `float()` - Convert to decimal number

---

### Basic If Statements
**Purpose:** Make decisions in your program

```python
# Basic if statement
answer = input("What's 2 + 2? ")
if answer == "4":
    print("Correct!")
else:
    print("Try again!")

# Checking text (case-insensitive)
color = input("What's your favorite color? ")
if color.lower() == "blue":
    print("Blue is awesome!")
```

**Comparison Operators:**
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than

---

## 🛠️ Common Patterns

### Getting User Info
```python
name = input("What's your name? ")
age = input("How old are you? ")
print("Hello, " + name + "! You are " + age + " years old.")
```

### Simple Quiz Question
```python
score = 0
answer = input("What's the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score = score + 1
else:
    print("The answer is Paris")
print("Score:", score)
```

### Basic Calculator
```python
num1 = input("First number: ")
num2 = input("Second number: ")
result = int(num1) + int(num2)
print(num1 + " + " + num2 + " = " + str(result))
```

---

## ⚠️ Troubleshooting Guide

### Error: `SyntaxError: invalid syntax`
**Cause:** Missing quotes, parentheses, or colons

```python
# Wrong ❌
print(Hello World)

# Right ✅  
print("Hello World")
```

**Solutions:**
- Check for missing quotes around text
- Check for missing parentheses in functions
- Look at the line number in the error message

---

### Error: `NameError: name 'variable_name' is not defined`
**Cause:** Trying to use a variable that doesn't exist

```python
# Wrong ❌
print("Hello, " + name)  # name was never created

# Right ✅
name = input("What's your name? ")
print("Hello, " + name)
```

**Solutions:**
- Make sure you create the variable before using it
- Check spelling of variable names
- Variables are case-sensitive: `Name` ≠ `name`

---

### Error: `TypeError: can only concatenate str (not "int") to str`
**Cause:** Trying to join text and numbers

```python
# Wrong ❌
age = 16
print("I am " + age + " years old")

# Right ✅
age = 16
print("I am " + str(age) + " years old")
```

**Solutions:**
- Use `str()` to convert numbers to text
- Use `int()` to convert text to numbers

---

### Program Doesn't Wait for Input
**Cause:** Not using `input()` or not storing the result

```python
# Wrong ❌
print("What's your name?")  # Just prints, doesn't wait

# Right ✅
name = input("What's your name? ")
```

---

### Input Shows as Text When You Want Numbers
**Cause:** `input()` always returns text

```python
# Wrong ❌
num = input("Enter a number: ")
result = num + 5  # Error! Can't add text and number

# Right ✅
num = input("Enter a number: ")
number = int(num)  # Convert to integer
result = number + 5
```

---

## 🎯 Quick Checklist

Before moving to Session 2, make sure you can:

- [ ] Write a `print()` statement without looking
- [ ] Use `input()` to get information from a user
- [ ] Create variables with good names
- [ ] Join strings together with `+`
- [ ] Convert between text and numbers
- [ ] Write a simple if statement
- [ ] Build a basic interactive program
- [ ] Debug common syntax errors

---

## 💡 Pro Tips

### Make Your Code Readable
```python
# Good - easy to understand
student_name = input("What's your name? ")
student_grade = input("What grade are you in? ")
welcome_message = "Welcome, " + student_name + " from grade " + student_grade + "!"
print(welcome_message)

# Not as good - hard to understand
n = input("Name? ")
g = input("Grade? ")
print("Welcome, " + n + " from grade " + g + "!")
```

### Test Your Programs
- Try different inputs
- Test with empty inputs
- Try numbers and text
- Make sure error messages are helpful

### Keep Learning
- Experiment with the code examples
- Modify programs to do different things
- Ask "What if I tried...?" and test it
- Don't be afraid to make mistakes!

---

## 🔗 What's Next?

In Session 2, you'll learn:
- Lists and loops
- Making programs repeat actions
- Organizing data better
- Building more complex programs

Keep practicing these basics - they're the foundation of everything else in Python!

---

## 📞 Getting Help

When you're stuck:
1. Read the error message carefully
2. Check this reference guide
3. Try the troubleshooting section
4. Ask your instructor or a classmate
5. Remember: every programmer gets stuck sometimes!

**Happy coding! 🐍✨**