# Session 7: Personal Journal Application - Complete Build

print("=" * 60)
print("BUILDING A PERSONAL JOURNAL APPLICATION")
print("=" * 60)

print("Let's build a comprehensive personal journal that saves your thoughts!")
print("This will demonstrate the full power of file handling in Python.")

import datetime
import os
import json

# STEP 1: Basic Journal with Simple Text Files
print("\n" + "="*50)
print("STEP 1: BASIC JOURNAL WITH TEXT FILES")
print("="*50)

class BasicJournal:
    """Simple journal using plain text files"""
    
    def __init__(self, filename='basic_journal.txt'):
        self.filename = filename
        print(f"📓 Basic Journal initialized: {filename}")
    
    def add_entry(self, content):
        """Add a new journal entry"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"\n{'='*50}\n")
            file.write(f"DATE: {timestamp}\n")
            file.write(f"{'='*50}\n")
            file.write(content + "\n")
        
        print(f"✅ Entry added to {self.filename}")
    
    def read_journal(self):
        """Read and display all entries"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                if content.strip():
                    print("\n📖 YOUR JOURNAL:")
                    print(content)
                else:
                    print("📖 Journal is empty. Add your first entry!")
        except FileNotFoundError:
            print("📖 No journal file found. Start writing to create one!")
    
    def get_entry_count(self):
        """Count the number of entries"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content.count("DATE:")
        except FileNotFoundError:
            return 0

# Demo basic journal
print("Testing basic journal:")
basic_journal = BasicJournal('demo_basic.txt')
basic_journal.add_entry("Today I started learning about file handling in Python. It's incredible how I can save my thoughts permanently!")
basic_journal.add_entry("I'm building my own journal application. Each entry is timestamped and saved forever.")

print(f"Journal has {basic_journal.get_entry_count()} entries")
basic_journal.read_journal()

# STEP 2: Enhanced Journal with Better Structure
print("\n" + "="*50)
print("STEP 2: ENHANCED JOURNAL WITH STRUCTURE")
print("="*50)

class EnhancedJournal:
    """Enhanced journal with better data structure"""
    
    def __init__(self, filename='enhanced_journal.json'):
        self.filename = filename
        self.entries = []
        self.load_entries()
        print(f"📓 Enhanced Journal initialized: {filename}")
    
    def load_entries(self):
        """Load existing entries from JSON file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.entries = data.get('entries', [])
            print(f"📖 Loaded {len(self.entries)} existing entries")
        except FileNotFoundError:
            print("📖 Starting fresh journal")
            self.entries = []
        except json.JSONDecodeError:
            print("⚠️  Journal file corrupted, starting fresh")
            self.entries = []
    
    def save_entries(self):
        """Save all entries to JSON file"""
        data = {
            'created': datetime.datetime.now().isoformat(),
            'total_entries': len(self.entries),
            'entries': self.entries
        }
        
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    
    def add_entry(self, content, mood=None, tags=None):
        """Add a new journal entry with metadata"""
        entry = {
            'id': len(self.entries) + 1,
            'timestamp': datetime.datetime.now().isoformat(),
            'date': datetime.date.today().isoformat(),
            'content': content,
            'mood': mood,
            'tags': tags or [],
            'word_count': len(content.split())
        }
        
        self.entries.append(entry)
        self.save_entries()
        
        print(f"✅ Entry #{entry['id']} added with {entry['word_count']} words")
        if mood:
            print(f"   Mood: {mood}")
        if tags:
            print(f"   Tags: {', '.join(tags)}")
    
    def display_entries(self, limit=None, show_metadata=True):
        """Display journal entries"""
        if not self.entries:
            print("📖 No entries yet. Add your first entry!")
            return
        
        entries_to_show = self.entries[-limit:] if limit else self.entries
        
        print(f"\n📖 JOURNAL ENTRIES (showing {len(entries_to_show)} of {len(self.entries)}):")
        print("=" * 60)
        
        for entry in entries_to_show:
            # Parse date for readable format
            date_obj = datetime.datetime.fromisoformat(entry['timestamp'])
            readable_date = date_obj.strftime("%B %d, %Y at %I:%M %p")
            
            print(f"\nEntry #{entry['id']} - {readable_date}")
            
            if show_metadata:
                if entry.get('mood'):
                    print(f"Mood: {entry['mood']}")
                if entry.get('tags'):
                    print(f"Tags: {', '.join(entry['tags'])}")
                print(f"Word count: {entry['word_count']}")
            
            print("-" * 40)
            print(entry['content'])
            print("-" * 40)
    
    def search_entries(self, search_term, search_type='content'):
        """Search entries by content, mood, or tags"""
        search_term = search_term.lower()
        matches = []
        
        for entry in self.entries:
            if search_type == 'content':
                if search_term in entry['content'].lower():
                    matches.append(entry)
            elif search_type == 'mood':
                if entry.get('mood') and search_term in entry['mood'].lower():
                    matches.append(entry)
            elif search_type == 'tags':
                if entry.get('tags'):
                    for tag in entry['tags']:
                        if search_term in tag.lower():
                            matches.append(entry)
                            break
        
        if matches:
            print(f"\n🔍 Found {len(matches)} entries matching '{search_term}' in {search_type}:")
            for entry in matches:
                date_obj = datetime.datetime.fromisoformat(entry['timestamp'])
                readable_date = date_obj.strftime("%B %d, %Y")
                print(f"\nEntry #{entry['id']} - {readable_date}")
                print(entry['content'][:100] + "..." if len(entry['content']) > 100 else entry['content'])
        else:
            print(f"🔍 No entries found matching '{search_term}' in {search_type}")
        
        return matches
    
    def get_statistics(self):
        """Get detailed journal statistics"""
        if not self.entries:
            return "No entries to analyze"
        
        total_entries = len(self.entries)
        total_words = sum(entry['word_count'] for entry in self.entries)
        average_words = total_words / total_entries
        
        # Date range
        first_entry = datetime.datetime.fromisoformat(self.entries[0]['timestamp'])
        last_entry = datetime.datetime.fromisoformat(self.entries[-1]['timestamp'])
        days_journaling = (last_entry.date() - first_entry.date()).days + 1
        
        # Mood analysis
        moods = [entry.get('mood') for entry in self.entries if entry.get('mood')]
        mood_counts = {}
        for mood in moods:
            mood_counts[mood] = mood_counts.get(mood, 0) + 1
        
        # Tag analysis
        all_tags = []
        for entry in self.entries:
            if entry.get('tags'):
                all_tags.extend(entry['tags'])
        
        tag_counts = {}
        for tag in all_tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        # Most productive day
        entries_by_date = {}
        for entry in self.entries:
            date = entry['date']
            entries_by_date[date] = entries_by_date.get(date, 0) + 1
        
        most_productive_date = max(entries_by_date, key=entries_by_date.get) if entries_by_date else None
        
        stats = f"""📊 JOURNAL STATISTICS:
Total entries: {total_entries}
Total words: {total_words:,}
Average words per entry: {average_words:.1f}
Days journaling: {days_journaling}
Entries per day average: {total_entries/days_journaling:.1f}

📅 Date range: {first_entry.strftime('%B %d, %Y')} to {last_entry.strftime('%B %d, %Y')}"""
        
        if most_productive_date:
            productive_count = entries_by_date[most_productive_date]
            stats += f"\n🏆 Most productive day: {most_productive_date} ({productive_count} entries)"
        
        if mood_counts:
            stats += f"\n\n😊 MOOD DISTRIBUTION:"
            for mood, count in sorted(mood_counts.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / len(moods)) * 100
                stats += f"\n  {mood}: {count} times ({percentage:.1f}%)"
        
        if tag_counts:
            stats += f"\n\n🏷️  TOP TAGS:"
            top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            for tag, count in top_tags:
                stats += f"\n  #{tag}: {count} times"
        
        return stats
    
    def export_entries(self, format='txt', date_range=None):
        """Export entries to different formats"""
        if not self.entries:
            print("No entries to export!")
            return
        
        entries_to_export = self.entries
        
        # Filter by date range if specified
        if date_range:
            start_date, end_date = date_range
            entries_to_export = [
                entry for entry in self.entries
                if start_date <= entry['date'] <= end_date
            ]
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == 'txt':
            filename = f"journal_export_{timestamp}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("PERSONAL JOURNAL EXPORT\n")
                file.write("=" * 50 + "\n")
                file.write(f"Exported on: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
                file.write(f"Total entries: {len(entries_to_export)}\n")
                file.write("=" * 50 + "\n\n")
                
                for entry in entries_to_export:
                    date_obj = datetime.datetime.fromisoformat(entry['timestamp'])
                    readable_date = date_obj.strftime("%B %d, %Y at %I:%M %p")
                    
                    file.write(f"Entry #{entry['id']} - {readable_date}\n")
                    if entry.get('mood'):
                        file.write(f"Mood: {entry['mood']}\n")
                    if entry.get('tags'):
                        file.write(f"Tags: {', '.join(entry['tags'])}\n")
                    file.write("-" * 40 + "\n")
                    file.write(entry['content'] + "\n")
                    file.write("=" * 50 + "\n\n")
            
            print(f"✅ Exported {len(entries_to_export)} entries to {filename}")
        
        elif format == 'json':
            filename = f"journal_export_{timestamp}.json"
            export_data = {
                'export_date': datetime.datetime.now().isoformat(),
                'total_entries': len(entries_to_export),
                'entries': entries_to_export
            }
            
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(export_data, file, indent=2, ensure_ascii=False)
            
            print(f"✅ Exported {len(entries_to_export)} entries to {filename}")

# Demo enhanced journal
print("Testing enhanced journal:")
enhanced_journal = EnhancedJournal('demo_enhanced.json')

enhanced_journal.add_entry(
    "Today I learned about JSON files and how they make data storage so much more flexible than plain text. I can now add metadata to my journal entries!",
    mood="excited",
    tags=["learning", "python", "files"]
)

enhanced_journal.add_entry(
    "I'm amazed at how Python handles file operations. The combination of dictionaries and JSON makes it easy to create sophisticated data structures.",
    mood="amazed",
    tags=["python", "data-structures", "programming"]
)

enhanced_journal.add_entry(
    "Building this journal application is teaching me so much about software design. I'm thinking about user experience and data persistence.",
    mood="thoughtful",
    tags=["learning", "software-design", "reflection"]
)

print(f"\nJournal Statistics:")
print(enhanced_journal.get_statistics())

print(f"\nSearching for entries about 'python':")
enhanced_journal.search_entries("python")

# STEP 3: Complete Journal Application with Menu
print("\n" + "="*50)
print("STEP 3: COMPLETE INTERACTIVE JOURNAL")
print("="*50)

class PersonalJournal(EnhancedJournal):
    """Complete interactive journal application"""
    
    def __init__(self, filename='personal_journal.json'):
        super().__init__(filename)
        self.current_session_entries = 0
    
    def interactive_add_entry(self):
        """Interactive entry addition with prompts"""
        print("\n✍️  NEW JOURNAL ENTRY")
        print("-" * 25)
        
        content = input("Write your journal entry:\n> ")
        
        if not content.strip():
            print("❌ Entry cannot be empty!")
            return
        
        # Optional mood
        mood = input("\nHow are you feeling? (optional): ").strip()
        if not mood:
            mood = None
        
        # Optional tags
        tags_input = input("Add tags (comma-separated, optional): ").strip()
        tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
        tags = [tag for tag in tags if tag]  # Remove empty tags
        
        self.add_entry(content, mood, tags)
        self.current_session_entries += 1
    
    def quick_mood_check(self):
        """Quick mood tracking entry"""
        moods = ["happy", "sad", "excited", "anxious", "calm", "frustrated", "grateful", "tired"]
        
        print("\n😊 QUICK MOOD CHECK")
        print("-" * 20)
        print("Select your current mood:")
        
        for i, mood in enumerate(moods, 1):
            print(f"{i}. {mood.title()}")
        
        while True:
            try:
                choice = int(input(f"\nChoose (1-{len(moods)}): "))
                if 1 <= choice <= len(moods):
                    selected_mood = moods[choice - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(moods)}")
            except ValueError:
                print("Please enter a valid number!")
        
        # Optional note about the mood
        note = input(f"\nAny thoughts about feeling {selected_mood}? (optional): ").strip()
        
        if note:
            content = f"Mood check: {note}"
        else:
            content = f"Feeling {selected_mood} right now."
        
        self.add_entry(content, mood=selected_mood, tags=["mood-check"])
        print(f"✅ Mood logged: {selected_mood}")
    
    def browse_by_date(self):
        """Browse entries by date"""
        if not self.entries:
            print("No entries to browse!")
            return
        
        # Get unique dates
        dates = list(set(entry['date'] for entry in self.entries))
        dates.sort(reverse=True)  # Most recent first
        
        print(f"\n📅 BROWSE BY DATE ({len(dates)} days with entries)")
        print("-" * 30)
        
        for i, date in enumerate(dates[:10], 1):  # Show last 10 days
            entries_on_date = [e for e in self.entries if e['date'] == date]
            date_obj = datetime.datetime.fromisoformat(date + "T00:00:00")
            readable_date = date_obj.strftime("%B %d, %Y")
            print(f"{i:2d}. {readable_date} ({len(entries_on_date)} entries)")
        
        if len(dates) > 10:
            print(f"    ... and {len(dates) - 10} more days")
        
        while True:
            try:
                choice = input(f"\nChoose date (1-{min(10, len(dates))}) or 'back': ")
                if choice.lower() == 'back':
                    return
                
                choice_num = int(choice)
                if 1 <= choice_num <= min(10, len(dates)):
                    selected_date = dates[choice_num - 1]
                    entries_on_date = [e for e in self.entries if e['date'] == selected_date]
                    
                    date_obj = datetime.datetime.fromisoformat(selected_date + "T00:00:00")
                    readable_date = date_obj.strftime("%B %d, %Y")
                    
                    print(f"\n📖 ENTRIES FOR {readable_date}")
                    print("=" * 40)
                    
                    for entry in entries_on_date:
                        time_obj = datetime.datetime.fromisoformat(entry['timestamp'])
                        time_str = time_obj.strftime("%I:%M %p")
                        
                        print(f"\nEntry #{entry['id']} at {time_str}")
                        if entry.get('mood'):
                            print(f"Mood: {entry['mood']}")
                        print("-" * 20)
                        print(entry['content'])
                        print("-" * 20)
                    
                    input("\nPress Enter to continue...")
                    break
                else:
                    print(f"Please enter a number between 1 and {min(10, len(dates))}")
            except ValueError:
                print("Please enter a valid number or 'back'!")
    
    def run(self):
        """Main interactive loop"""
        print(f"\n📓 PERSONAL JOURNAL APPLICATION")
        print("=" * 40)
        print(f"Welcome! You have {len(self.entries)} existing entries.")
        
        while True:
            print(f"\n📋 MAIN MENU")
            print("1. Write new entry")
            print("2. Quick mood check")
            print("3. View recent entries")
            print("4. Browse by date")
            print("5. Search entries")
            print("6. View statistics")
            print("7. Export journal")
            print("8. Quit")
            
            choice = input("\nChoose option (1-8): ").strip()
            
            if choice == '1':
                self.interactive_add_entry()
            
            elif choice == '2':
                self.quick_mood_check()
            
            elif choice == '3':
                limit = 5
                print(f"\n📖 RECENT ENTRIES (last {limit}):")
                self.display_entries(limit=limit)
            
            elif choice == '4':
                self.browse_by_date()
            
            elif choice == '5':
                search_term = input("Enter search term: ").strip()
                if search_term:
                    print("\nSearch options:")
                    print("1. Content")
                    print("2. Mood")
                    print("3. Tags")
                    
                    search_choice = input("Search in (1-3): ").strip()
                    search_types = {'1': 'content', '2': 'mood', '3': 'tags'}
                    search_type = search_types.get(search_choice, 'content')
                    
                    self.search_entries(search_term, search_type)
            
            elif choice == '6':
                print(self.get_statistics())
            
            elif choice == '7':
                print("\nExport format:")
                print("1. Text file (.txt)")
                print("2. JSON file (.json)")
                
                format_choice = input("Choose format (1-2): ").strip()
                export_format = 'txt' if format_choice == '1' else 'json'
                
                self.export_entries(format=export_format)
            
            elif choice == '8':
                if self.current_session_entries > 0:
                    print(f"\n🎉 Great session! You added {self.current_session_entries} entries today.")
                print("📖 Your thoughts are safely saved. See you next time!")
                break
            
            else:
                print("❌ Invalid choice! Please select 1-8.")

# Demo the complete application
def demo_complete_journal():
    """Demonstrate the complete journal application"""
    print("📓 COMPLETE JOURNAL APPLICATION DEMO")
    print("=" * 40)
    
    journal = PersonalJournal('demo_complete.json')
    
    # Add some sample data if journal is empty
    if len(journal.entries) == 0:
        print("Adding sample entries for demonstration...")
        
        journal.add_entry(
            "Started building my personal journal app today. It's incredible how Python makes file handling so straightforward!",
            mood="excited",
            tags=["programming", "python", "journal"]
        )
        
        journal.add_entry(
            "Learned about JSON files and structured data. My journal can now store much more than just text!",
            mood="accomplished",
            tags=["learning", "json", "data"]
        )
        
        journal.add_entry(
            "Reflecting on my progress. Building real applications is so much more engaging than just doing exercises.",
            mood="thoughtful",
            tags=["reflection", "progress", "learning"]
        )
    
    print("\nJournal demo data loaded!")
    print(journal.get_statistics())
    
    print("\n💡 To run the full interactive journal, uncomment the line below:")
    print("# journal.run()")

demo_complete_journal()

print("\n" + "="*60)
print("🎯 PERSONAL JOURNAL APPLICATION COMPLETE!")
print("You've learned how to build:")
print("• File-based data persistence")
print("• JSON for structured data storage")
print("• Interactive menu-driven applications")
print("• Search and filtering functionality")
print("• Data export and statistics")
print("• User-friendly interfaces")
print("Your journal will preserve your thoughts forever! 📚")
print("="*60)

# Uncomment to run the full interactive application:
# if __name__ == "__main__":
#     app = PersonalJournal()
#     app.run()