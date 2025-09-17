# Python Basics & Automation - Instructor Guide
# 60-minute Lesson Plan

## Learning Objectives
By the end of this session, students will:
1. Understand basic Python concepts (variables, input/output, conditionals, loops)
2. Create and run their first Python script
3. Understand file operations in Python
4. Run an automation script that organizes files

## Materials Provided
- `01_variables_and_input.py` - Demonstrates variables and user input
- `02_print_function.py` - Shows different ways to use print()
- `03_file_operations.py` - Covers basic file operations
- `04_loops.py` - Explains for and while loops
- `05_logic_and_conditionals.py` - Covers if statements and logic
- `file_generator.py` - Creates sample files for testing
- `organizer.py` - The main file organization script

## Detailed Lesson Plan

### 1. Introduction & Mindset (5 mins)
- Introduce yourself and the session topic
- Set expectations: "We're learning by doing. Today, you'll run a script that does something useful."
- Explain the hands-on approach: "In programming, we learn best by writing and running code"
- Ask students about their experience level with programming

### 2. The Big Picture (5 mins)
- Demo the file organizer running on your screen
  1. Run `python file_generator.py` to create sample files
  2. Show the "messy" folder with various files
  3. Run `python organizer.py` to organize the files
  4. Show the results: files sorted into folders by type
- Tell students: "This is what we're building today!"

### 3. Core Concept 1: Variables & input() (10 mins)
- Open and explain `01_variables_and_input.py`
- Key points to cover:
  - Variables are like labeled containers for data
  - Python has different data types (string, int, float)
  - Variables can change values during execution
  - `input()` collects data from the user
  - Converting between data types (str to int, etc.)
- Live coding: Have students create a simple script:
  ```python
  name = input("What is your name? ")
  age = int(input("How old are you? "))
  print(f"Hello, {name}! In 10 years you'll be {age + 10} years old.")
  ```
- Have students run the code and see the results

### 4. Core Concept 2: The print() Function (5 mins)
- Open and explain `02_print_function.py`
- Key points to cover:
  - Basic usage: `print("Hello")`
  - Printing variables: `print(name)`
  - Combining text and variables
  - Formatting output with f-strings
  - Special characters (\n, \t)
- Quick exercise: Have students create a "business card" print out using print()

### 5. Core Concept 3: Basic File Operations (10 mins)
- Open and explain `03_file_operations.py`
- Key points to cover:
  - Opening files: `open(filename, mode)`
  - Writing to files: `file.write()`
  - Reading from files: `file.read()`, reading line by line
  - Closing files: `file.close()` and using `with` statement
  - File modes: "w" (write), "r" (read), "a" (append)
- Live coding: Create a simple script to create a text file:
  ```python
  with open("greeting.txt", "w") as file:
      file.write("Hello, world!\n")
      file.write("This file was created by Python!")
  
  print("File created!")
  ```
- Extend the example to read back the file contents

### 6. Run the Full File Organizer (10 mins)
- Open the `organizer.py` script
- Walk through the main components:
  - Importing modules (`os` and `shutil`)
  - Defining the `organize_files()` function
  - Getting the current directory
  - Setting up file categories
  - Looping through files
  - Creating folders and moving files
- Have students run the script:
  1. First run `python file_generator.py` to create test files
  2. Then run `python organizer.py` to organize them
- Celebrate the success!

### 7. Additional Concepts & Preview (10 mins)
- Briefly introduce the other scripts:
  - `04_loops.py` - Show how loops work for repetitive tasks
  - `05_logic_and_conditionals.py` - Explain decision making
- Highlight key concepts they'll learn in future sessions:
  - Lists and dictionaries (data structures)
  - Functions and modules
  - More advanced automation projects
- Q&A: Answer student questions

### 8. Closing (5 mins)
- Recap what was covered
- Encourage students to experiment with the scripts
- Preview next session
- Assign a simple homework task (modify the organizer script)

## Teaching Tips

1. **Keep it interactive**: Ask questions and encourage students to follow along on their computers
2. **Troubleshoot common issues**:
   - File paths (use absolute paths if needed)
   - Indentation errors (Python is sensitive to whitespace)
   - Typos in variable names
3. **Use analogies**: Compare variables to labeled boxes, loops to repeating tasks
4. **Show real-world applications**: Emphasize how automation saves time
5. **Pace yourself**: It's better to cover core concepts well than rush through everything
6. **Celebrate small wins**: Programming can be frustrating for beginners

## Follow-up Activities

For students who finish early or want additional practice:
1. Modify the organizer script to include more file types
2. Create a "backup" script that copies important files to a backup folder
3. Build a simple "to-do list" program that saves items to a file

## Resources for Students

Recommend these resources for further learning:
- Python.org official tutorials
- Automate the Boring Stuff with Python (free online book)
- W3Schools Python Tutorial
- Codecademy Python course
