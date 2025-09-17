# Simple file organizer
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
