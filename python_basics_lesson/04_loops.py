# # 04_loops.py
# # This script shows how loops work in Python

# # ===== FOR LOOPS =====
# # For loops let you run code a specific number of times or for each item in a collection

# # print("===== BASIC FOR LOOP =====")
# # # Loop through a range of numbers (0 to 4)
# # print("Counting from 0 to 4:")
# # for i in range(5):
# #     print(i)
# #
# # # Loop through a range with a start, stop (exclusive), and step
# # print("\nCounting from 1 to 10 by 2s:")
# # for i in range(1, 11, 2):
# #     print(i)

# # # ===== LOOPING THROUGH COLLECTIONS =====
# # print("\n===== LOOPING THROUGH LISTS =====")

# # Loop through a list of items
# fruits = ["apple", "banana", "cherry", "dragon fruit"]
# print("Fruits in the list:")
# for fruit in fruits:
#     print(f"- {fruit}")

# # # # Loop with both index and value using enumerate()
# # # print("\nFruits with index:")
# # # for index, fruit in enumerate(fruits):
# # #     print(f"{index}: {fruit}")

# # # ===== LOOPING THROUGH DICTIONARIES =====
# # print("\n===== LOOPING THROUGH DICTIONARIES =====")

# # A dictionary is a collection of key-value pairs
# # person = {
# #     "name": "Jude",
# #     "age": 25,
# #     "city": "New York"
# # }

# # # Loop through keys
# # print("Keys in the dictionary:")
# # for key in person:
# #     print(key)

# # # Loop through values
# # print("\nValues in the dictionary:")
# # for value in person.values():
# #     print(value)

# # # Loop through both keys and values
# # print("\nKeys and values:")
# # for key, value in person.items():
# #     print(f"{key}: {value}")

# # ===== WHILE LOOPS =====
# print("\n===== WHILE LOOP =====")
# # While loops run as long as a condition is true

# # # Countdown example
# # count = 5
# # print("Countdown:")
# # while count > 0:
# #     print(count)
# #     count -= 1  # This is the same as: count = count - 1
# # print("Blast off!")

# # ===== LOOP CONTROL =====
# print("\n===== LOOP CONTROL =====")

# # Using break to exit a loop early
# print("Finding a specific fruit (with break):")
# for fruit in fruits:
#     print(f"Checking: {fruit}")
#     if fruit == "cherry":
#         print("Found cherry! Exiting loop.")
#         break  # Exit the loop immediately

# # Using continue to skip iterations
# print("\nSkipping even numbers (with continue):")
# for i in range(1, 10):
#     if i % 2 == 0:  # If i is even
#         continue  # Skip to the next iteration
#     print(i)

# # ===== NESTED LOOPS =====
# print("\n===== NESTED LOOPS =====")
# # A loop inside another loop

# print("Multiplication table (1-3):")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} × {j} = {i*j}")
#     print()  # Empty line after each row

# ===== PRACTICAL EXAMPLE =====
print("\n===== PRACTICAL EXAMPLE =====")

# Let's simulate processing a list of files
files = ["document.txt", "image.jpg", "data.csv", "presentation.pptx", "code.py"]
print("Processing files:")

for index, filename in enumerate(files):
    print(f"Processing file {index+1}/{len(files)}: {filename}")
    
    # Get the file extension
    extension = filename.split(".")[-1]
    
    # Different handling based on file type
    if extension == "txt":
        print("  Text file: Checking spelling...")
    elif extension in ["jpg", "png"]:
        print("  Image file: Compressing...")
    elif extension == "py":
        print("  Python file: Running tests...")
    else:
        print("  Unknown type: Skipping...")

# ===== CHALLENGE FOR STUDENTS =====
# Try creating a simple "guessing game" using a while loop!
# Make the computer pick a random number and give hints (higher/lower)
