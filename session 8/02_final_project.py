# Session 8: Final Project - Personal Productivity Suite

print("=" * 60)
print("FINAL PROJECT: PERSONAL PRODUCTIVITY SUITE")
print("=" * 60)

print("Let's build a comprehensive application using everything we've learned!")
print("This will combine variables, lists, dictionaries, conditionals,")
print("loops, file handling, and functions into one powerful system!")

import datetime
import json
import os

# PART 1: Core Data Management Functions
print("\n" + "="*50)
print("PART 1: CORE DATA MANAGEMENT FUNCTIONS")
print("="*50)

def load_data(filename):
    """Load data from JSON file safely"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"📁 Creating new data file: {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"⚠️  Warning: {filename} corrupted, starting fresh")
        return {}

def save_data(data, filename):
    """Save data to JSON file safely"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error saving data: {e}")
        return False

def get_current_timestamp():
    """Get current timestamp in ISO format"""
    return datetime.datetime.now().isoformat()

def get_current_date():
    """Get current date in YYYY-MM-DD format"""
    return datetime.date.today().isoformat()

def format_date(date_string):
    """Format ISO date string to readable format"""
    try:
        date_obj = datetime.datetime.fromisoformat(date_string)
        return date_obj.strftime("%B %d, %Y")
    except:
        return date_string

def generate_id(existing_items):
    """Generate a new unique ID"""
    if not existing_items:
        return 1
    return max(item.get('id', 0) for item in existing_items) + 1

# PART 2: Task Management System
print("\n" + "="*50)
print("PART 2: TASK MANAGEMENT SYSTEM")
print("="*50)

class TaskManager:
    """Complete task management system"""
    
    def __init__(self, data_file='tasks.json'):
        self.data_file = data_file
        self.tasks = load_data(data_file).get('tasks', [])
    
    def save_tasks(self):
        """Save tasks to file"""
        data = {
            'last_updated': get_current_timestamp(),
            'total_tasks': len(self.tasks),
            'tasks': self.tasks
        }
        return save_data(data, self.data_file)
    
    def add_task(self, title, description="", priority="medium", due_date=None):
        """Add a new task"""
        if not title.strip():
            return False, "Task title cannot be empty"
        
        task = {
            'id': generate_id(self.tasks),
            'title': title.strip(),
            'description': description.strip(),
            'priority': priority.lower(),
            'due_date': due_date,
            'completed': False,
            'created_date': get_current_date(),
            'created_time': get_current_timestamp(),
            'completed_date': None
        }
        
        self.tasks.append(task)
        self.save_tasks()
        return True, f"Task '{title}' added successfully"
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        task = self.find_task(task_id)
        if not task:
            return False, "Task not found"
        
        if task['completed']:
            return False, "Task already completed"
        
        task['completed'] = True
        task['completed_date'] = get_current_date()
        self.save_tasks()
        return True, f"Task '{task['title']}' marked as completed"
    
    def find_task(self, task_id):
        """Find a task by ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def delete_task(self, task_id):
        """Delete a task"""
        task = self.find_task(task_id)
        if not task:
            return False, "Task not found"
        
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_tasks()
        return True, f"Task '{task['title']}' deleted"
    
    def list_tasks(self, show_completed=False, priority_filter=None):
        """List tasks with optional filters"""
        filtered_tasks = self.tasks
        
        if not show_completed:
            filtered_tasks = [t for t in filtered_tasks if not t['completed']]
        
        if priority_filter:
            filtered_tasks = [t for t in filtered_tasks if t['priority'] == priority_filter.lower()]
        
        if not filtered_tasks:
            return "No tasks found with the specified criteria"
        
        # Sort by priority and due date
        priority_order = {'high': 1, 'medium': 2, 'low': 3}
        filtered_tasks.sort(key=lambda t: (
            priority_order.get(t['priority'], 4),
            t['due_date'] or '9999-12-31',
            t['created_date']
        ))
        
        result = f"📋 TASK LIST ({len(filtered_tasks)} tasks)\n"
        result += "=" * 40 + "\n"
        
        for task in filtered_tasks:
            status = "✅" if task['completed'] else "⭕"
            priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task['priority'], "⚪")
            
            result += f"\n{status} [{task['id']}] {task['title']} {priority_emoji}\n"
            
            if task['description']:
                result += f"   📝 {task['description']}\n"
            
            if task['due_date']:
                due_formatted = format_date(task['due_date'])
                result += f"   📅 Due: {due_formatted}\n"
            
            if task['completed']:
                completed_formatted = format_date(task['completed_date'])
                result += f"   ✅ Completed: {completed_formatted}\n"
        
        return result
    
    def get_statistics(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t['completed']])
        pending = total - completed
        
        high_priority = len([t for t in self.tasks if t['priority'] == 'high' and not t['completed']])
        overdue = 0
        
        today = get_current_date()
        for task in self.tasks:
            if not task['completed'] and task['due_date'] and task['due_date'] < today:
                overdue += 1
        
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        return f"""📊 TASK STATISTICS
==================
Total tasks: {total}
Completed: {completed}
Pending: {pending}
High priority pending: {high_priority}
Overdue: {overdue}
Completion rate: {completion_rate:.1f}%"""

# PART 3: Note-Taking System
print("\n" + "="*50)
print("PART 3: NOTE-TAKING SYSTEM")
print("="*50)

class NoteManager:
    """Simple note-taking system"""
    
    def __init__(self, data_file='notes.json'):
        self.data_file = data_file
        self.notes = load_data(data_file).get('notes', [])
    
    def save_notes(self):
        """Save notes to file"""
        data = {
            'last_updated': get_current_timestamp(),
            'total_notes': len(self.notes),
            'notes': self.notes
        }
        return save_data(data, self.data_file)
    
    def add_note(self, title, content, tags=None):
        """Add a new note"""
        if not title.strip() or not content.strip():
            return False, "Title and content cannot be empty"
        
        note = {
            'id': generate_id(self.notes),
            'title': title.strip(),
            'content': content.strip(),
            'tags': tags or [],
            'created_date': get_current_date(),
            'created_time': get_current_timestamp(),
            'modified_time': get_current_timestamp(),
            'word_count': len(content.split())
        }
        
        self.notes.append(note)
        self.save_notes()
        return True, f"Note '{title}' added successfully"
    
    def find_note(self, note_id):
        """Find a note by ID"""
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None
    
    def search_notes(self, search_term):
        """Search notes by title, content, or tags"""
        search_term = search_term.lower()
        matches = []
        
        for note in self.notes:
            if (search_term in note['title'].lower() or 
                search_term in note['content'].lower() or
                any(search_term in tag.lower() for tag in note.get('tags', []))):
                matches.append(note)
        
        return matches
    
    def list_notes(self, limit=None):
        """List all notes"""
        if not self.notes:
            return "No notes found"
        
        # Sort by most recent first
        sorted_notes = sorted(self.notes, key=lambda n: n['modified_time'], reverse=True)
        
        if limit:
            sorted_notes = sorted_notes[:limit]
        
        result = f"📝 NOTES ({len(sorted_notes)} of {len(self.notes)})\n"
        result += "=" * 30 + "\n"
        
        for note in sorted_notes:
            created_date = format_date(note['created_date'])
            result += f"\n📄 [{note['id']}] {note['title']}\n"
            result += f"   📅 {created_date} | {note['word_count']} words\n"
            
            if note.get('tags'):
                result += f"   🏷️  {', '.join(note['tags'])}\n"
            
            # Show preview of content
            preview = note['content'][:100]
            if len(note['content']) > 100:
                preview += "..."
            result += f"   💬 {preview}\n"
        
        return result

# PART 4: Contact Management System
print("\n" + "="*50)
print("PART 4: CONTACT MANAGEMENT SYSTEM")
print("="*50)

class ContactManager:
    """Simple contact management system"""
    
    def __init__(self, data_file='contacts.json'):
        self.data_file = data_file
        self.contacts = load_data(data_file).get('contacts', [])
    
    def save_contacts(self):
        """Save contacts to file"""
        data = {
            'last_updated': get_current_timestamp(),
            'total_contacts': len(self.contacts),
            'contacts': self.contacts
        }
        return save_data(data, self.data_file)
    
    def add_contact(self, name, email=None, phone=None, notes=None):
        """Add a new contact"""
        if not name.strip():
            return False, "Name cannot be empty"
        
        # Check for duplicate names
        if any(c['name'].lower() == name.lower() for c in self.contacts):
            return False, "Contact with this name already exists"
        
        contact = {
            'id': generate_id(self.contacts),
            'name': name.strip(),
            'email': email.strip() if email else None,
            'phone': phone.strip() if phone else None,
            'notes': notes.strip() if notes else None,
            'created_date': get_current_date(),
            'created_time': get_current_timestamp()
        }
        
        self.contacts.append(contact)
        self.save_contacts()
        return True, f"Contact '{name}' added successfully"
    
    def find_contact(self, contact_id):
        """Find a contact by ID"""
        for contact in self.contacts:
            if contact['id'] == contact_id:
                return contact
        return None
    
    def search_contacts(self, search_term):
        """Search contacts by name, email, or phone"""
        search_term = search_term.lower()
        matches = []
        
        for contact in self.contacts:
            if (search_term in contact['name'].lower() or
                (contact.get('email') and search_term in contact['email'].lower()) or
                (contact.get('phone') and search_term in contact['phone'])):
                matches.append(contact)
        
        return matches
    
    def list_contacts(self):
        """List all contacts"""
        if not self.contacts:
            return "No contacts found"
        
        # Sort alphabetically by name
        sorted_contacts = sorted(self.contacts, key=lambda c: c['name'].lower())
        
        result = f"👥 CONTACTS ({len(sorted_contacts)})\n"
        result += "=" * 25 + "\n"
        
        for contact in sorted_contacts:
            result += f"\n👤 [{contact['id']}] {contact['name']}\n"
            
            if contact.get('email'):
                result += f"   📧 {contact['email']}\n"
            
            if contact.get('phone'):
                result += f"   📱 {contact['phone']}\n"
            
            if contact.get('notes'):
                result += f"   📝 {contact['notes']}\n"
        
        return result

# PART 5: Main Application Controller
print("\n" + "="*50)
print("PART 5: MAIN APPLICATION CONTROLLER")
print("="*50)

class ProductivitySuite:
    """Main application that coordinates all modules"""
    
    def __init__(self):
        print("🚀 Initializing Personal Productivity Suite...")
        self.task_manager = TaskManager()
        self.note_manager = NoteManager()
        self.contact_manager = ContactManager()
        print("✅ All systems ready!")
    
    def display_main_menu(self):
        """Display the main application menu"""
        print(f"\n📋 PERSONAL PRODUCTIVITY SUITE")
        print("=" * 40)
        print("1. 📝 Task Management")
        print("2. 📄 Notes")
        print("3. 👥 Contacts")
        print("4. 📊 Dashboard")
        print("5. 🔧 Settings")
        print("6. 🚪 Exit")
    
    def task_menu(self):
        """Task management submenu"""
        while True:
            print(f"\n📝 TASK MANAGEMENT")
            print("=" * 25)
            print("1. Add task")
            print("2. List tasks")
            print("3. Complete task")
            print("4. Delete task")
            print("5. Task statistics")
            print("6. Back to main menu")
            
            choice = input("\nChoose option (1-6): ").strip()
            
            if choice == '1':
                title = input("Task title: ").strip()
                description = input("Description (optional): ").strip()
                
                print("Priority: 1=High, 2=Medium, 3=Low")
                priority_choice = input("Priority (1-3, default=2): ").strip()
                priority_map = {'1': 'high', '2': 'medium', '3': 'low'}
                priority = priority_map.get(priority_choice, 'medium')
                
                due_date = input("Due date (YYYY-MM-DD, optional): ").strip()
                if due_date and len(due_date) != 10:
                    due_date = None
                
                success, message = self.task_manager.add_task(title, description, priority, due_date)
                print(f"{'✅' if success else '❌'} {message}")
            
            elif choice == '2':
                show_completed = input("Show completed tasks? (y/n): ").lower() == 'y'
                priority_filter = input("Filter by priority (high/medium/low, or Enter for all): ").strip()
                if not priority_filter:
                    priority_filter = None
                
                print(self.task_manager.list_tasks(show_completed, priority_filter))
            
            elif choice == '3':
                try:
                    task_id = int(input("Enter task ID to complete: "))
                    success, message = self.task_manager.complete_task(task_id)
                    print(f"{'✅' if success else '❌'} {message}")
                except ValueError:
                    print("❌ Please enter a valid task ID")
            
            elif choice == '4':
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    confirm = input("Are you sure? (y/n): ").lower()
                    if confirm == 'y':
                        success, message = self.task_manager.delete_task(task_id)
                        print(f"{'✅' if success else '❌'} {message}")
                    else:
                        print("❌ Delete cancelled")
                except ValueError:
                    print("❌ Please enter a valid task ID")
            
            elif choice == '5':
                print(self.task_manager.get_statistics())
            
            elif choice == '6':
                break
            
            else:
                print("❌ Invalid choice! Please select 1-6.")
    
    def note_menu(self):
        """Note management submenu"""
        while True:
            print(f"\n📄 NOTES")
            print("=" * 15)
            print("1. Add note")
            print("2. List notes")
            print("3. Search notes")
            print("4. Back to main menu")
            
            choice = input("\nChoose option (1-4): ").strip()
            
            if choice == '1':
                title = input("Note title: ").strip()
                print("Enter note content (press Enter twice to finish):")
                content_lines = []
                while True:
                    line = input()
                    if line == "" and content_lines and content_lines[-1] == "":
                        break
                    content_lines.append(line)
                
                content = '\n'.join(content_lines).strip()
                
                tags_input = input("Tags (comma-separated, optional): ").strip()
                tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
                tags = [tag for tag in tags if tag]
                
                success, message = self.note_manager.add_note(title, content, tags)
                print(f"{'✅' if success else '❌'} {message}")
            
            elif choice == '2':
                limit_input = input("Show how many recent notes? (Enter for all): ").strip()
                limit = int(limit_input) if limit_input.isdigit() else None
                
                print(self.note_manager.list_notes(limit))
            
            elif choice == '3':
                search_term = input("Search for: ").strip()
                if search_term:
                    matches = self.note_manager.search_notes(search_term)
                    if matches:
                        print(f"\n🔍 Found {len(matches)} matching notes:")
                        for note in matches:
                            print(f"[{note['id']}] {note['title']}")
                    else:
                        print("No matching notes found")
            
            elif choice == '4':
                break
            
            else:
                print("❌ Invalid choice! Please select 1-4.")
    
    def contact_menu(self):
        """Contact management submenu"""
        while True:
            print(f"\n👥 CONTACTS")
            print("=" * 15)
            print("1. Add contact")
            print("2. List contacts")
            print("3. Search contacts")
            print("4. Back to main menu")
            
            choice = input("\nChoose option (1-4): ").strip()
            
            if choice == '1':
                name = input("Contact name: ").strip()
                email = input("Email (optional): ").strip()
                phone = input("Phone (optional): ").strip()
                notes = input("Notes (optional): ").strip()
                
                success, message = self.contact_manager.add_contact(name, email, phone, notes)
                print(f"{'✅' if success else '❌'} {message}")
            
            elif choice == '2':
                print(self.contact_manager.list_contacts())
            
            elif choice == '3':
                search_term = input("Search for: ").strip()
                if search_term:
                    matches = self.contact_manager.search_contacts(search_term)
                    if matches:
                        print(f"\n🔍 Found {len(matches)} matching contacts:")
                        for contact in matches:
                            print(f"[{contact['id']}] {contact['name']}")
                            if contact.get('email'):
                                print(f"    📧 {contact['email']}")
                            if contact.get('phone'):
                                print(f"    📱 {contact['phone']}")
                    else:
                        print("No matching contacts found")
            
            elif choice == '4':
                break
            
            else:
                print("❌ Invalid choice! Please select 1-4.")
    
    def show_dashboard(self):
        """Show overall statistics dashboard"""
        print(f"\n📊 PRODUCTIVITY DASHBOARD")
        print("=" * 30)
        
        # Task statistics
        task_stats = self.task_manager.get_statistics()
        print(task_stats)
        
        # Note statistics
        note_count = len(self.note_manager.notes)
        total_words = sum(note.get('word_count', 0) for note in self.note_manager.notes)
        print(f"\n📝 NOTE STATISTICS")
        print("==================")
        print(f"Total notes: {note_count}")
        print(f"Total words: {total_words:,}")
        if note_count > 0:
            print(f"Average words per note: {total_words/note_count:.1f}")
        
        # Contact statistics
        contact_count = len(self.contact_manager.contacts)
        contacts_with_email = len([c for c in self.contact_manager.contacts if c.get('email')])
        print(f"\n👥 CONTACT STATISTICS")
        print("====================")
        print(f"Total contacts: {contact_count}")
        print(f"With email: {contacts_with_email}")
        print(f"With notes: {len([c for c in self.contact_manager.contacts if c.get('notes')])}")
    
    def run(self):
        """Main application loop"""
        print("🎉 Welcome to your Personal Productivity Suite!")
        
        while True:
            self.display_main_menu()
            choice = input("\nChoose option (1-6): ").strip()
            
            if choice == '1':
                self.task_menu()
            elif choice == '2':
                self.note_menu()
            elif choice == '3':
                self.contact_menu()
            elif choice == '4':
                self.show_dashboard()
            elif choice == '5':
                print("⚙️  Settings coming in a future update!")
            elif choice == '6':
                print("\n🎉 Thank you for using Personal Productivity Suite!")
                print("Your data is safely saved. See you next time! 👋")
                break
            else:
                print("❌ Invalid choice! Please select 1-6.")
            
            input("\nPress Enter to continue...")

# PART 6: Demo and Testing
print("\n" + "="*50)
print("PART 6: DEMO AND TESTING")
print("="*50)

def demo_productivity_suite():
    """Demonstrate the productivity suite with sample data"""
    print("🎬 PRODUCTIVITY SUITE DEMO")
    print("=" * 30)
    
    # Create the application
    app = ProductivitySuite()
    
    # Add sample tasks
    print("\n📝 Adding sample tasks...")
    app.task_manager.add_task("Learn Python functions", "Complete Session 8 exercises", "high", "2024-10-15")
    app.task_manager.add_task("Build final project", "Create productivity suite", "medium")
    app.task_manager.add_task("Practice coding", "Code for 30 minutes daily", "low")
    
    # Add sample notes
    print("📄 Adding sample notes...")
    app.note_manager.add_note(
        "Python Functions Summary",
        "Functions are reusable blocks of code that help organize programs. Key concepts: def, parameters, return values, scope.",
        ["python", "programming", "study"]
    )
    app.note_manager.add_note(
        "Project Ideas",
        "Ideas for future projects: weather app, expense tracker, recipe manager, fitness tracker.",
        ["ideas", "projects"]
    )
    
    # Add sample contacts
    print("👥 Adding sample contacts...")
    app.contact_manager.add_contact("Python Mentor", "mentor@python.org", "555-0123", "Great teacher!")
    app.contact_manager.add_contact("Study Group", "group@study.com", notes="Weekly Python meetup")
    
    # Show dashboard
    print("\n📊 Demo Dashboard:")
    app.show_dashboard()
    
    print("\n💡 Sample data loaded! You can now explore the full application.")
    print("Uncomment the app.run() line below to start the interactive version!")

# Run the demo
demo_productivity_suite()

print("\n" + "="*60)
print("🎯 FINAL PROJECT COMPLETE!")
print("Congratulations! You've built a complete application using:")
print("• Variables and data types")
print("• Lists and dictionaries")
print("• Conditional logic (if/else)")
print("• Loops (for/while)")
print("• File handling and persistence")
print("• Functions and code organization")
print("• Error handling and user input")
print("• Menu-driven interfaces")
print("")
print("🚀 You're now a Python programmer!")
print("Keep practicing and building amazing things!")
print("="*60)

# Uncomment to run the full interactive application:
# if __name__ == "__main__":
#     app = ProductivitySuite()
#     app.run()