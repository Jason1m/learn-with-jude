# file_generator.py
# This script creates a bunch of sample files for our file organizer demo
# BEGINNER-FRIENDLY VERSION

# First, we need to import some tools that Python provides
import os       # This lets us work with folders and files
import shutil   # This helps us copy and move files

# This is a function - it's a reusable block of code
# We'll use it to create each of our sample files
def create_sample_file(folder_path, filename, content="Sample content"):
    """
    Creates a file with the given name and content.
    
    folder_path: Where to create the file
    filename: What to name the file
    content: What to put in the file
    """
    # Join the folder path and filename to get the complete file location
    file_path = os.path.join(folder_path, filename)
    
    # Open the file, write the content, and close it automatically
    with open(file_path, "w") as file:
        file.write(content)
        
    # Let the user know we created a file
    print(f"Created: {filename}")

# This is our main function that will create all the sample files
def generate_sample_files():
    """
    Creates a folder called 'messy_folder' and fills it with different types of files.
    This gives us a messy folder that needs organizing!
    """
    print("🚀 Starting the File Generator...")
    print("This script will create a folder with several different types of files.")
    print("You'll use these files to test the file organizer script.")
    
    # Step 1: Create a folder named "messy_folder" in the current location
    # os.getcwd() gets the current working directory (where the script is running)
    messy_folder = os.path.join(os.getcwd(), "messy_folder")
    
    # Step 2: If the folder already exists from a previous run, remove it
    # This ensures we start fresh each time
    if os.path.exists(messy_folder):
        shutil.rmtree(messy_folder)
        print("Removed existing messy_folder to start fresh")
        
    # Step 3: Create the new empty folder
    os.makedirs(messy_folder)
    print("Created a new messy_folder for our files")
    print("\nNow creating sample files...")
    
    # Step 4: Create different types of files in our messy folder
    
    print("\n--- Creating document files ---")
    # Text files, Word documents, spreadsheets, PDFs
    create_sample_file(messy_folder, "notes.txt", "These are some important notes for class.")
    create_sample_file(messy_folder, "report.docx", "This simulates a Word document.")
    create_sample_file(messy_folder, "data.xlsx", "This simulates an Excel spreadsheet.")
    create_sample_file(messy_folder, "presentation.pdf", "This simulates a PDF document.")
    
    print("\n--- Creating image files ---")
    # JPG, PNG, and GIF images
    create_sample_file(messy_folder, "photo1.jpg", "This simulates a JPG photo.")
    create_sample_file(messy_folder, "logo.png", "This simulates a PNG image.")
    create_sample_file(messy_folder, "banner.gif", "This simulates a GIF image.")
    
    print("\n--- Creating media files ---")
    # Music and video files
    create_sample_file(messy_folder, "song.mp3", "This simulates an MP3 music file.")
    create_sample_file(messy_folder, "movie.mp4", "This simulates an MP4 video file.")
    
    print("\n--- Creating code files ---")
    # Programming and web files
    create_sample_file(messy_folder, "script.py", "# This is a Python script\nprint('Hello, world!')")
    create_sample_file(messy_folder, "webpage.html", "<html><body><h1>Hello World</h1></body></html>")
    create_sample_file(messy_folder, "styles.css", "body { font-family: Arial; }")
    
    print("\n--- Creating other files ---")
    # Other miscellaneous files
    create_sample_file(messy_folder, "archive.zip", "This simulates a ZIP archive.")
    
    # Step 5: Add the file organizer script to the messy folder
    print("\n--- Adding the organizer script ---")
    organizer_script = "organizer.py"
    
    # Check if the organizer.py file exists in the current folder
    if os.path.exists(organizer_script):
        # If it exists, copy it to our messy folder
        organizer_dest = os.path.join(messy_folder, organizer_script)
        shutil.copy2(organizer_script, organizer_dest)
        print(f"Copied {organizer_script} to the messy folder")
    else:
        # If it doesn't exist, create a simple version
        print("Creating a simple organizer.py in the messy folder")
        
        # This is the content of our simple organizer script
        simple_organizer = """# Simple file organizer
# This script will organize your messy files into folders based on file type

import os
import shutil

def organize_files():
    # Get the current folder location
    current_dir = os.getcwd()
    print(f"Organizing files in: {current_dir}")
    
    # Define categories and what file types go in each
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Audio': ['.mp3', '.wav'],
        'Video': ['.mp4', '.mov', '.avi'],
    }
    
    # Look at each file in the folder
    for filename in os.listdir(current_dir):
        # Skip the organizer script itself and any folders
        if filename == "organizer.py" or os.path.isdir(os.path.join(current_dir, filename)):
            continue
        
        # Get the file extension (like .txt or .jpg)    
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()
        
        # Find which category this file belongs to
        found_category = 'Others'  # Default category
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                found_category = category
                break

        # Create the category folder if it doesn't exist
        category_path = os.path.join(current_dir, found_category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created new folder: {found_category}")

        # Move the file to its category folder
        old_path = os.path.join(current_dir, filename)
        new_path = os.path.join(category_path, filename)
        shutil.move(old_path, new_path)
        print(f"Moved: {filename} -> {found_category}/")

# This is where the script starts running
if __name__ == "__main__":
    print("🚀 Starting File Organizer...")
    organize_files()
"""
        # Create the organizer script file
        create_sample_file(messy_folder, "organizer.py", simple_organizer)
        print("Created organizer.py file in the messy folder")

    # Step 6: Print completion message with instructions
    print("\n✅ Success! All sample files were created in the 'messy_folder'!")
    print("\n" + "-" * 60)
    print("HOW TO RUN THE FILE ORGANIZER:")
    print("-" * 60)
    print("1. Open a terminal/command prompt")
    print(f"2. Type this command to go to the messy folder: cd {os.path.basename(messy_folder)}")
    print("3. Type this command to run the organizer: python organizer.py")
    print("-" * 60)
    print("After running the organizer, you'll see your files sorted into folders!")
    print("-" * 60)

# This special code block runs our function when the script is run directly
# (This is the starting point of our program)
if __name__ == "__main__":
    print("=" * 70)
    print("WELCOME TO THE PYTHON FILE ORGANIZER DEMO - FILE GENERATOR".center(70))
    print("=" * 70)
    
    # Call our function to generate all the sample files
    generate_sample_files()
    
    # Final message
    print("\nThat's it! You're ready to try the file organizer.".center(70))
    print("=" * 70)
