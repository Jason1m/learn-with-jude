# Python Basics & Automation
## Student Handout

### Key Concepts

#### 1. Variables
- A variable is a container for storing data values
- Create variables using the assignment operator (`=`)
- Python has different data types: strings, integers, floats, booleans, etc.

```python
name = "Alex"           # String (text)
age = 25                # Integer (whole number)
height = 1.75           # Float (decimal number)
is_student = True       # Boolean (True/False)
```

#### 2. Input and Output
- `input()` gets text from the user
- `print()` displays information to the user

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

#### 3. File Operations
- Open files with `open(filename, mode)`
- Common modes: "w" (write), "r" (read), "a" (append)
- Always close files when done or use `with` statement

```python
# Writing to a file
with open("notes.txt", "w") as file:
    file.write("This is a note.\n")
    file.write("Python is awesome!")

# Reading from a file
with open("notes.txt", "r") as file:
    contents = file.read()
    print(contents)
```

#### 4. Conditionals
- `if`, `elif`, and `else` statements let your program make decisions
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`

```python
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

#### 5. Loops
- `for` loops repeat code for each item in a sequence
- `while` loops repeat code as long as a condition is true

```python
# For loop
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# While loop
count = 5
while count > 0:
    print(count)
    count -= 1
```

### Practice Exercises

#### Exercise 1: Hello, User!
Write a script that asks for the user's name, age, and favorite color, then prints a personalized message.

#### Exercise 2: Number Guessing Game
Create a simple number guessing game where the computer picks a random number between 1 and 10, and the user has to guess it.

Hint: Use `import random` and `random.randint(1, 10)` to generate a random number.

#### Exercise 3: Simple To-Do List
Create a script that lets users add items to a to-do list stored in a text file.

#### Exercise 4: Custom File Organizer
Modify the file organizer script to add a new category for your own file types.

### The File Organizer Script

Here's what the file organizer script does:

1. Gets a list of all files in the current directory
2. For each file, checks its extension (like .txt or .jpg)
3. Creates folders for different file categories if they don't exist
4. Moves each file to the appropriate folder based on its type

Try running these commands:
```
python file_generator.py   # Creates sample files
python organizer.py        # Organizes the files into folders
```

### Key Python Terms

- **Variable**: A container for storing data values
- **Function**: A block of code that performs a specific task
- **Parameter**: Information passed to a function
- **String**: A sequence of characters (text)
- **Integer**: A whole number
- **Float**: A number with a decimal point
- **Boolean**: A True or False value
- **List**: An ordered collection of items
- **Dictionary**: A collection of key-value pairs
- **Loop**: Code that repeats multiple times
- **Conditional**: Code that makes decisions based on conditions
- **Module**: A Python file with functions and variables you can use in other files

### Tips for Beginners

1. **Check your indentation**: Python uses indentation to define code blocks
2. **Be precise with syntax**: Spelling, capitalization, and punctuation matter
3. **Read error messages**: They often tell you exactly what's wrong
4. **Start simple**: Build small working pieces before tackling complex projects
5. **Practice regularly**: Coding is a skill that improves with practice

### Next Steps in Your Python Journey

After mastering these basics, you can explore:
- Lists and dictionaries for storing collections of data
- Functions for organizing and reusing your code
- Modules and packages for extending Python's capabilities
- Object-oriented programming for building complex applications
- Web scraping, data analysis, and more advanced automation
