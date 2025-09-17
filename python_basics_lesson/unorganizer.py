# unorganizer.py
# This script reverses the organization of files, moving them back to the main directory

import os
import shutil

def unorganize_files(target_dir=None):
    """
    This function moves all files from category folders back to the main directory.
    If no directory is specified, it will use the "messy_folder_demo" directory.
    """
    
    # Get the current directory
    current_dir = os.getcwd()
    
    # If no target directory is specified, use the messy_folder_demo directory
    if target_dir is None:
        # Create path to the messy_folder_demo directory
        target_dir = os.path.join(current_dir, "messy_folder_demo")
        
    # Check if the target directory exists
    if not os.path.exists(target_dir):
        print(f"Error: The directory {target_dir} does not exist!")
        return
        
    print(f"Un-organizing files in: {target_dir}")
    
    # List of category folders we created with the organizer
    category_folders = ['Documents', 'Images', 'Audio', 'Video', 'Others']
    
    # Track how many files we move
    moved_count = 0
    
    # Go through each category folder
    for category in category_folders:
        category_path = os.path.join(target_dir, category)
        
        # Skip if this category folder doesn't exist
        if not os.path.exists(category_path):
            continue
            
        print(f"Looking in {category} folder...")
        
        # Get all files in this category folder
        try:
            files = os.listdir(category_path)
            
            # Move each file back to the main folder
            for filename in files:
                # Skip if it's another folder
                if os.path.isdir(os.path.join(category_path, filename)):
                    continue
                    
                # Source and destination paths
                source_path = os.path.join(category_path, filename)
                dest_path = os.path.join(target_dir, filename)
                
                # Move the file
                shutil.move(source_path, dest_path)
                print(f"Moved: {category}/{filename} -> main folder")
                moved_count += 1
                
            # After moving all files, try to remove the empty category folder
            if not os.listdir(category_path):
                os.rmdir(category_path)
                print(f"Removed empty folder: {category}")
                
        except Exception as e:
            print(f"Error while processing {category} folder: {e}")
    
    if moved_count > 0:
        print(f"\n✅ Successfully moved {moved_count} files back to the main folder!")
    else:
        print("\nNo files were moved. Folders may already be empty.")
    
    print("\nThe folder is now back to its 'messy' state, ready for demonstration!")

# This is where the script starts running
if __name__ == "__main__":
    print("🔄 Starting File Un-organizer...")
    unorganize_files()
