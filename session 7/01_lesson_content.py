# Session 7: File Power (Reading/Writing Files)
# Detailed Explanation and Examples

print("=" * 60)
print("SESSION 7: FILE POWER (READING/WRITING FILES)")
print("=" * 60)

# PART 1: INTRODUCTION TO FILES
print("\n1. INTRODUCTION TO FILES")
print("-" * 40)

print("Why do we need files?")
print("• Save data permanently (survives program restart)")
print("• Share data between programs")
print("• Store user preferences and settings")
print("• Keep logs and records")
print("• Import/export data")

print("\nReal-world examples:")
print("• 💾 Saving your game progress")
print("• 📝 Writing documents and notes")
print("• 📊 Storing spreadsheet data")
print("• 🔧 Configuration files")
print("• 📜 Log files for debugging")

print("\nWithout files: Data disappears when program ends!")
print("With files: Data persists forever! 🎉")

# PART 2: BASIC FILE OPERATIONS
print("\n\n2. BASIC FILE OPERATIONS")
print("-" * 40)

print("File operations in Python:")
print("1. Open a file")
print("2. Read from or write to the file")
print("3. Close the file")

print("\nThe 'with' statement does this automatically!")
print("with open('filename.txt', 'mode') as file:")
print("    # work with file")
print("# file automatically closed here")

# Example: Writing to a file
print("\nLet's create our first file:")

# Create a simple text file
with open('my_first_file.txt', 'w') as file:
    file.write("Hello, File World!\n")
    file.write("This is my first Python file.\n")
    file.write("Python makes file handling easy!")

print("✅ Created 'my_first_file.txt'")

# Example: Reading from a file
print("\nNow let's read it back:")

try:
    with open('my_first_file.txt', 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("❌ File not found!")

# PART 3: FILE MODES
print("\n\n3. FILE MODES")
print("-" * 40)

print("Different ways to open files:")
print("'r'  - Read only (default)")
print("'w'  - Write (overwrites existing file)")
print("'a'  - Append (adds to end of file)")
print("'r+' - Read and write")

print("\nLet's see each mode in action:")

# Write mode (overwrites)
print("\n1. Write mode ('w') - creates new or overwrites:")
with open('demo_file.txt', 'w') as file:
    file.write("This is the first line.\n")
    file.write("This overwrites any existing content.\n")

# Read mode
print("\n2. Read mode ('r') - read the content:")
with open('demo_file.txt', 'r') as file:
    content = file.read()
    print("Content after writing:")
    print(content)

# Append mode
print("\n3. Append mode ('a') - adds to the end:")
with open('demo_file.txt', 'a') as file:
    file.write("This line is appended.\n")
    file.write("Previous content is preserved.\n")

# Read again to see the difference
with open('demo_file.txt', 'r') as file:
    content = file.read()
    print("Content after appending:")
    print(content)

# PART 4: DIFFERENT WAYS TO READ FILES
print("\n\n4. DIFFERENT WAYS TO READ FILES")
print("-" * 40)

# Create a sample file for reading demos
sample_content = """Line 1: Introduction
Line 2: This is a sample file
Line 3: For demonstrating reading methods
Line 4: Each line has different content
Line 5: The end"""

with open('reading_demo.txt', 'w') as file:
    file.write(sample_content)

print("Created sample file. Now demonstrating reading methods:")

print("\n1. read() - Read entire file as one string:")
with open('reading_demo.txt', 'r') as file:
    entire_content = file.read()
    print(repr(entire_content))  # repr shows \n characters

print("\n2. readline() - Read one line at a time:")
with open('reading_demo.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

print("\n3. readlines() - Read all lines into a list:")
with open('reading_demo.txt', 'r') as file:
    all_lines = file.readlines()
    print(f"Total lines: {len(all_lines)}")
    for i, line in enumerate(all_lines, 1):
        print(f"  Line {i}: {line.strip()}")

print("\n4. Iterate through file (memory efficient):")
with open('reading_demo.txt', 'r') as file:
    for line_number, line in enumerate(file, 1):
        print(f"  {line_number}: {line.strip()}")

# PART 5: ERROR HANDLING WITH FILES
print("\n\n5. ERROR HANDLING WITH FILES")
print("-" * 40)

print("Files can cause errors! Always handle them gracefully.")

# Common file errors
def demonstrate_file_errors():
    print("\n1. FileNotFoundError:")
    try:
        with open('nonexistent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("❌ File doesn't exist!")
    
    print("\n2. PermissionError (simulated):")
    try:
        # This might cause permission error on some systems
        with open('/root/protected_file.txt', 'w') as file:
            file.write("test")
    except PermissionError:
        print("❌ No permission to write here!")
    except:
        print("❌ Some other error occurred!")
    
    print("\n3. Safe file reading with error handling:")
    filename = 'maybe_exists.txt'
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"✅ Successfully read {len(content)} characters")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
        # Could create the file here if needed
        with open(filename, 'w') as file:
            file.write("Default content\n")
        print(f"✅ Created '{filename}' with default content")

demonstrate_file_errors()

# PART 6: BUILDING A SIMPLE JOURNAL
print("\n\n6. BUILDING A SIMPLE JOURNAL")
print("-" * 40)

import datetime

def simple_journal_demo():
    """Demonstrate a simple journal application"""
    
    print("📓 SIMPLE JOURNAL APPLICATION")
    print("=" * 35)
    
    journal_file = 'my_journal.txt'
    
    def add_entry(entry_text):
        """Add a new journal entry"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(journal_file, 'a') as file:
            file.write(f"\n--- Entry: {timestamp} ---\n")
            file.write(entry_text + "\n")
            file.write("-" * 40 + "\n")
        
        print(f"✅ Entry added to {journal_file}")
    
    def read_journal():
        """Read and display all journal entries"""
        try:
            with open(journal_file, 'r') as file:
                content = file.read()
                if content.strip():
                    print("\n📖 YOUR JOURNAL ENTRIES:")
                    print(content)
                else:
                    print("📖 Journal is empty. Add your first entry!")
        except FileNotFoundError:
            print("📖 No journal found. Start writing to create one!")
    
    def count_entries():
        """Count total journal entries"""
        try:
            with open(journal_file, 'r') as file:
                content = file.read()
                entry_count = content.count("--- Entry:")
                return entry_count
        except FileNotFoundError:
            return 0
    
    # Demo the journal
    print("Adding sample entries...")
    add_entry("Today I learned about file handling in Python! It's amazing how easy it is to save data permanently.")
    add_entry("I built my first journal application. Next, I want to add search functionality.")
    add_entry("Python's 'with open()' statement makes file handling so much safer than manual open/close.")
    
    print(f"\nJournal now has {count_entries()} entries.")
    read_journal()

simple_journal_demo()

# PART 7: PROCESSING STRUCTURED DATA
print("\n\n7. PROCESSING STRUCTURED DATA")
print("-" * 40)

def csv_processing_demo():
    """Demonstrate processing CSV-like data"""
    
    print("📊 PROCESSING STRUCTURED DATA")
    print("=" * 35)
    
    # Create sample CSV data
    csv_data = """Name,Age,City,Occupation
Alice Johnson,28,New York,Engineer
Bob Smith,34,Los Angeles,Designer
Charlie Brown,22,Chicago,Student
Diana Prince,31,Miami,Teacher
Eve Wilson,29,Seattle,Developer"""
    
    with open('people_data.csv', 'w') as file:
        file.write(csv_data)
    
    print("Created sample data file: people_data.csv")
    
    # Read and process the CSV
    print("\nProcessing the data:")
    
    people = []
    
    with open('people_data.csv', 'r') as file:
        lines = file.readlines()
        
        # First line is header
        header = lines[0].strip().split(',')
        print(f"Columns: {header}")
        
        # Process each person
        for line in lines[1:]:  # Skip header
            data = line.strip().split(',')
            person = {
                'name': data[0],
                'age': int(data[1]),
                'city': data[2],
                'occupation': data[3]
            }
            people.append(person)
    
    print(f"\nLoaded {len(people)} people:")
    for person in people:
        print(f"  {person['name']}, {person['age']}, {person['city']}, {person['occupation']}")
    
    # Analyze the data
    print(f"\n📈 DATA ANALYSIS:")
    
    total_age = sum(person['age'] for person in people)
    average_age = total_age / len(people)
    print(f"Average age: {average_age:.1f}")
    
    cities = [person['city'] for person in people]
    unique_cities = list(set(cities))
    print(f"Cities represented: {', '.join(unique_cities)}")
    
    occupations = [person['occupation'] for person in people]
    occupation_counts = {}
    for occ in occupations:
        occupation_counts[occ] = occupation_counts.get(occ, 0) + 1
    
    print(f"Occupation distribution:")
    for occ, count in occupation_counts.items():
        print(f"  {occ}: {count}")

csv_processing_demo()

# PART 8: ADVANCED FILE OPERATIONS
print("\n\n8. ADVANCED FILE OPERATIONS")
print("-" * 40)

def advanced_file_operations():
    """Demonstrate advanced file handling techniques"""
    
    print("🔧 ADVANCED FILE OPERATIONS")
    print("=" * 30)
    
    # Working with file information
    import os
    
    filename = 'my_journal.txt'
    
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"File '{filename}' exists")
        print(f"Size: {file_size} bytes")
        
        # Get file modification time
        import time
        mod_time = os.path.getmtime(filename)
        readable_time = time.ctime(mod_time)
        print(f"Last modified: {readable_time}")
    else:
        print(f"File '{filename}' does not exist")
    
    # Reading file in chunks (for large files)
    print(f"\nReading file in chunks:")
    try:
        with open(filename, 'r') as file:
            chunk_size = 50  # Read 50 characters at a time
            chunk_num = 1
            
            while True:
                chunk = file.read(chunk_size)
                if not chunk:  # End of file
                    break
                print(f"Chunk {chunk_num}: {len(chunk)} characters")
                chunk_num += 1
    except FileNotFoundError:
        print("No file to read in chunks")
    
    # Creating backup files
    print(f"\nCreating backup:")
    backup_filename = f"{filename}.backup"
    
    try:
        with open(filename, 'r') as original:
            with open(backup_filename, 'w') as backup:
                content = original.read()
                backup.write(content)
        print(f"✅ Backup created: {backup_filename}")
    except FileNotFoundError:
        print("No original file to backup")

advanced_file_operations()

# PART 9: BUILDING A COMPLETE JOURNAL APPLICATION
print("\n\n9. COMPLETE JOURNAL APPLICATION")
print("-" * 40)

class PersonalJournal:
    """Complete journal application with file persistence"""
    
    def __init__(self, filename='personal_journal.txt'):
        self.filename = filename
        self.entries = []
        self.load_entries()
    
    def load_entries(self):
        """Load existing entries from file"""
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                
                # Simple parsing - in real app would use better format
                if content.strip():
                    # Split entries by separator line
                    entry_blocks = content.split("-" * 40)
                    for block in entry_blocks:
                        if "--- Entry:" in block:
                            lines = block.strip().split('\n')
                            if len(lines) >= 2:
                                # Extract timestamp and content
                                header = lines[0]
                                content_lines = lines[1:]
                                entry_content = '\n'.join(content_lines)
                                
                                if entry_content.strip():
                                    self.entries.append({
                                        'header': header,
                                        'content': entry_content.strip()
                                    })
            
            print(f"📖 Loaded {len(self.entries)} existing entries")
            
        except FileNotFoundError:
            print(f"📖 Starting fresh journal: {self.filename}")
    
    def add_entry(self, content):
        """Add a new entry"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"--- Entry: {timestamp} ---"
        
        entry = {
            'header': header,
            'content': content
        }
        
        self.entries.append(entry)
        self.save_entries()
        print(f"✅ Added entry #{len(self.entries)}")
    
    def save_entries(self):
        """Save all entries to file"""
        with open(self.filename, 'w') as file:
            for entry in self.entries:
                file.write(f"\n{entry['header']}\n")
                file.write(f"{entry['content']}\n")
                file.write("-" * 40 + "\n")
    
    def display_entries(self, limit=None):
        """Display entries (with optional limit)"""
        if not self.entries:
            print("📖 No entries yet. Add your first entry!")
            return
        
        entries_to_show = self.entries[-limit:] if limit else self.entries
        
        print(f"\n📖 JOURNAL ENTRIES (showing {len(entries_to_show)} of {len(self.entries)}):")
        print("=" * 50)
        
        for i, entry in enumerate(entries_to_show, 1):
            print(f"{entry['header']}")
            print(f"{entry['content']}")
            print("-" * 40)
    
    def search_entries(self, search_term):
        """Search for entries containing specific text"""
        search_term = search_term.lower()
        matches = []
        
        for i, entry in enumerate(self.entries):
            if search_term in entry['content'].lower():
                matches.append((i + 1, entry))
        
        if matches:
            print(f"\n🔍 Found {len(matches)} entries matching '{search_term}':")
            for entry_num, entry in matches:
                print(f"\nEntry #{entry_num}:")
                print(f"{entry['header']}")
                print(f"{entry['content']}")
                print("-" * 30)
        else:
            print(f"🔍 No entries found matching '{search_term}'")
    
    def get_stats(self):
        """Get journal statistics"""
        if not self.entries:
            return "No entries to analyze"
        
        total_entries = len(self.entries)
        total_words = sum(len(entry['content'].split()) for entry in self.entries)
        average_words = total_words / total_entries
        
        # Find longest entry
        longest_entry = max(self.entries, key=lambda e: len(e['content']))
        longest_words = len(longest_entry['content'].split())
        
        return f"""📊 JOURNAL STATISTICS:
Total entries: {total_entries}
Total words: {total_words}
Average words per entry: {average_words:.1f}
Longest entry: {longest_words} words"""

# Demo the complete journal
def demo_complete_journal():
    """Demonstrate the complete journal application"""
    
    print("📓 COMPLETE JOURNAL APPLICATION DEMO")
    print("=" * 40)
    
    journal = PersonalJournal('demo_journal.txt')
    
    # Add some sample entries
    journal.add_entry("Today I learned about Python file handling. The 'with open()' statement is so elegant and safe!")
    
    journal.add_entry("I'm building a personal journal application. It's amazing how much you can accomplish with just basic file operations.")
    
    journal.add_entry("Python makes it easy to persist data. I can save my thoughts and they'll be there tomorrow!")
    
    # Display entries
    journal.display_entries(limit=2)  # Show last 2 entries
    
    # Show statistics
    print("\n" + journal.get_stats())
    
    # Search functionality
    journal.search_entries("python")
    
    print("\n💡 This journal persists between program runs!")
    print("Your entries are safely saved in 'demo_journal.txt'")

demo_complete_journal()

# PART 10: BEST PRACTICES AND TIPS
print("\n\n10. BEST PRACTICES AND TIPS")
print("-" * 40)

print("✅ File Handling Best Practices:")
print("1. Always use 'with open()' - automatic cleanup")
print("2. Handle exceptions (FileNotFoundError, PermissionError)")
print("3. Use appropriate file modes ('r', 'w', 'a')")
print("4. Be careful with file paths (use os.path.join for cross-platform)")
print("5. Consider file encoding (utf-8 for international text)")
print("6. Don't keep files open longer than necessary")
print("7. Make backups before overwriting important files")

print("\n❌ Common mistakes to avoid:")
print("• Forgetting to close files (use 'with')")
print("• Using 'w' mode and accidentally overwriting files")
print("• Not handling file errors gracefully")
print("• Hard-coding file paths that don't work on other systems")
print("• Reading huge files into memory all at once")

print("\n🔧 Advanced topics for later:")
print("• JSON files for structured data")
print("• Binary file operations")
print("• File compression and archiving")
print("• Network file operations")
print("• Database alternatives to files")

print("\n" + "="*60)
print("🎉 CONGRATULATIONS!")
print("You now have the power to make your programs remember!")
print("Key concepts mastered:")
print("• File reading and writing")
print("• Safe file handling with 'with' statements")
print("• Error handling for file operations")
print("• Building persistent applications")
print("• Data processing and analysis")
print("Your programs can now save data permanently! 💾")
print("="*60)