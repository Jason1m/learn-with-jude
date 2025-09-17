# setup_demo.py
# This script copies the organizer.py file to the messy_folder_demo directory
# Run this script before starting your lesson

import shutil
import os

def setup_demo():
    """Prepares the messy folder demo by copying the organizer script into it"""
    
    source_file = "organizer.py"
    target_dir = "messy_folder_demo"
    target_file = os.path.join(target_dir, source_file)
    
    # Check if source file exists
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found!")
        return
    
    # Check if target directory exists
    if not os.path.exists(target_dir):
        print(f"Error: {target_dir} directory not found!")
        return
    
    # Copy the file
    try:
        shutil.copy2(source_file, target_file)
        print(f"✅ Successfully copied {source_file} to {target_file}")
        print("The demo is now ready! Navigate to the messy_folder_demo directory")
        print("and run 'python organizer.py' to demonstrate the file organizer.")
    except Exception as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    print("Setting up the messy folder demo...")
    setup_demo()
