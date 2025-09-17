# organizer.py
# This is a script to organize your files by their type (like .txt, .jpg, .pdf)

# We use the 'os' and 'shutil' tools that come with Python
# 'os' lets us work with files and folders
# 'shutil' gives us more advanced file operations like moving files
import os
import shutil

# This is the main function. A function is a block of code we can run.
def organize_files(target_dir=None):
    """
    This function organizes files in the specified directory.
    If no directory is specified, it will use the "messy_folder_demo" directory.
    It will create folders for Images, Documents, and Others.
    """
    
    # Get the current directory (the folder where this script is saved)
    # os.getcwd() means "get current working directory"
    current_dir = os.getcwd()
    
    # If no target directory is specified, use the messy_folder_demo directory
    if target_dir is None:
        # Create path to the messy_folder_demo directory
        target_dir = os.path.join(current_dir, "messy_folder_demo")
        
    # Check if the target directory exists
    if not os.path.exists(target_dir):
        print(f"Error: The directory {target_dir} does not exist!")
        return
        
    print(f"Organizing files in: {target_dir}")
    
    # Define what files go where using a DICTIONARY (a list of key:value pairs)
    # This is like a lookup table: category name → list of file extensions
    # We will learn more about dictionaries later!
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.rtf', '.md'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    }

    # Get a list of all files in the target directory
    all_files = os.listdir(target_dir)
    
    # Loop through each file and organize it
    # This is a "for loop" - it repeats code for each item in a collection
    for filename in all_files:
        # Skip this script itself and any folders
        # The 'if' statement is a conditional - it makes decisions
        if filename == "organizer.py" or os.path.isdir(os.path.join(target_dir, filename)):
            continue  # 'continue' means "skip to the next item in the loop"
            
        # Get the file extension (like .txt or .jpg)
        # os.path.splitext() splits a filename into name and extension
        # The _ means "we don't care about this part right now"
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()  # Make it lowercase for consistency

        # Find which category this file belongs to
        # We start with a default category
        found_category = 'Others'  # Default category
        
        # This is another loop that checks each category
        for category, extensions in file_categories.items():
            # The 'if' statement checks if this file belongs in this category
            if file_extension in extensions:
                found_category = category
                break  # 'break' means "exit this loop early"

        # Create the category folder if it doesn't exist
        # os.path.join() creates a proper file path for any operating system
        category_path = os.path.join(target_dir, found_category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created new folder: {found_category}")

        # Move the file to its new folder
        old_path = os.path.join(target_dir, filename)
        new_path = os.path.join(category_path, filename)
        
        # shutil.move() moves a file from one location to another
        shutil.move(old_path, new_path)
        print(f"Moved: {filename} -> {found_category}/")

    print("✅ All files organized!")

# This is where the script starts running
# The special if __name__ == "__main__": line means:
# "Only run this code if this file is being run directly (not imported by another script)"
if __name__ == "__main__":
    print("🚀 Starting File Organizer...")
    
    # Get the absolute path to the messy_folder_demo directory
    current_dir = os.getcwd()
    messy_folder = os.path.join(current_dir, "messy_folder_demo")
    
    # Check if we're running the script from inside the messy folder
    if os.path.basename(current_dir) == "messy_folder_demo":
        # If we're already in the messy folder, organize files in the current directory
        organize_files(current_dir)
    else:
        # Otherwise, target the messy_folder_demo directory
        organize_files(messy_folder)
