# # 03_file_operations.py
# # This script shows basic file operations in Python

# # ===== CREATING AND WRITING TO A FILE =====
# # The open() function creates or opens a file
# # The "w" means "write mode" - this will create a new file or overwrite an existing one

# print("===== CREATING A TEXT FILE =====")

# # Method 1: open, write, close
# file = open("greeting.txt", "w")  # Open a file for writing
# file.write("Hello, world!\n")     # Write some text to the file
# file.write("Python is awesome!")   # Write more text
# file.close()                       # Always close the file when done

# print("Created greeting.txt")

# # Method 2: Using 'with' statement (recommended)
# # This automatically closes the file for us when the block ends
# with open("notes.txt", "w") as file:
#     file.write("This is line 1\n")
#     file.write("This is line 2\n")
#     file.write("This is line 3")

# print("Created notes.txt")

# # ===== READING FROM A FILE =====
# print("\n===== READING A TEXT FILE =====")

# # Reading the entire file at once
# with open("greeting.txt", "r") as file:  # "r" means "read mode"
#     contents = file.read()
#     print("Contents of greeting.txt:")
#     print(contents)

# # Reading a file line by line
# with open("notes.txt", "r") as file:
#     print("\nContents of notes.txt (line by line):")
#     for line in file:
#         print(f"  > {line.strip()}")  # strip() removes the newline character

# # ===== APPENDING TO A FILE =====
# print("\n===== APPENDING TO A FILE =====")

# # The "a" mode means "append" - add to the end without overwriting
# with open("greeting.txt", "a") as file:
#     file.write("\nThis line was appended later.")

# # Let's read the file again to see the changes
# with open("greeting.txt", "r") as file:
#     contents = file.read()
#     print("Updated contents of greeting.txt:")
#     print(contents)

# # ===== PRACTICAL EXAMPLE: SIMPLE LOG FILE =====
# print("\n===== CREATING A LOG FILE =====")

import datetime  # Import the datetime module to get current time

# Function to add an entry to our log file
def add_log_entry(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app_log.txt", "a") as log_file:
        log_file.write(f"[{current_time}] {message}\n")

# Let's add some log entries
add_log_entry("Application started")
add_log_entry("User logged in")
add_log_entry("Data processing completed")

print("Created app_log.txt")

# Read and display the log
with open("app_log.txt", "r") as file:
    log_contents = file.read()
    print("\nContents of app_log.txt:")
    print(log_contents)

# ===== CHALLENGE FOR STUDENTS =====
# Try creating a simple "diary" program that asks for an entry and adds it to a file!
