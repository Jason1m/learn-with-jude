# Session 6: Enhanced Shopping List Manager - Complete Build

print("=" * 60)
print("BUILDING ENHANCED SHOPPING LIST MANAGER")
print("=" * 60)

print("Let's build a powerful, menu-driven shopping list manager!")
print("This will demonstrate the full power of while loops.")

# STEP 1: Basic Menu Structure
print("\n" + "="*50)
print("STEP 1: BASIC MENU STRUCTURE")
print("="*50)

def basic_menu_demo():
    """Demonstrate basic menu structure with while loop"""
    
    print("\n📋 BASIC MENU DEMO")
    print("=" * 25)
    
    shopping_list = []
    
    while True:
        print(f"\nShopping List ({len(shopping_list)} items)")
        print("1. Add item")
        print("2. View list")
        print("3. Quit")
        
        choice = input("Choose option (1-3): ")
        
        if choice == '1':
            item = input("Enter item: ")
            shopping_list.append(item)
            print(f"Added: {item}")
        
        elif choice == '2':
            if shopping_list:
                print("Your list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"  {i}. {item}")
            else:
                print("List is empty!")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

print("Testing basic menu:")
# basic_menu_demo()  # Uncomment to test

# STEP 2: Enhanced Menu with Input Validation
print("\n" + "="*50)
print("STEP 2: ENHANCED MENU WITH VALIDATION")
print("="*50)

class ShoppingListManager:
    """Enhanced shopping list with validation and features"""
    
    def __init__(self):
        self.shopping_list = []
        self.completed_items = []
    
    def display_list(self):
        """Display current shopping list"""
        print(f"\n📋 SHOPPING LIST ({len(self.shopping_list)} items)")
        print("-" * 30)
        
        if self.shopping_list:
            for i, item in enumerate(self.shopping_list, 1):
                print(f"  {i}. {item}")
        else:
            print("  (List is empty)")
        
        if self.completed_items:
            print(f"\n✅ COMPLETED ({len(self.completed_items)} items)")
            print("-" * 30)
            for item in self.completed_items:
                print(f"  ✓ {item}")
    
    def add_item(self):
        """Add item with validation"""
        while True:
            item = input("\nEnter item to add (or 'back' to return): ").strip()
            
            if item.lower() == 'back':
                return
            
            if not item:
                print("❌ Item cannot be empty!")
                continue
            
            if item.lower() in [existing.lower() for existing in self.shopping_list]:
                print(f"❌ '{item}' is already in your list!")
                continue
            
            # Optional: Add quantity
            while True:
                try:
                    qty_input = input(f"Quantity for '{item}' (press Enter for 1): ").strip()
                    if not qty_input:
                        quantity = 1
                        break
                    quantity = int(qty_input)
                    if quantity <= 0:
                        print("❌ Quantity must be positive!")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid number!")
            
            # Format item with quantity if > 1
            if quantity > 1:
                formatted_item = f"{item} (x{quantity})"
            else:
                formatted_item = item
            
            self.shopping_list.append(formatted_item)
            print(f"✅ Added '{formatted_item}' to list")
            
            # Ask if they want to add another
            add_more = input("Add another item? (y/n): ").lower()
            if add_more not in ['y', 'yes']:
                break
    
    def remove_item(self):
        """Remove item from list"""
        if not self.shopping_list:
            print("❌ List is empty!")
            return
        
        self.display_list()
        
        while True:
            try:
                choice = input("\nEnter item number to remove (or 'back'): ").strip()
                
                if choice.lower() == 'back':
                    return
                
                index = int(choice) - 1
                
                if 0 <= index < len(self.shopping_list):
                    removed_item = self.shopping_list.pop(index)
                    print(f"✅ Removed '{removed_item}' from list")
                    break
                else:
                    print(f"❌ Please enter number between 1 and {len(self.shopping_list)}")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def mark_completed(self):
        """Mark item as completed"""
        if not self.shopping_list:
            print("❌ List is empty!")
            return
        
        self.display_list()
        
        while True:
            try:
                choice = input("\nEnter item number to mark complete (or 'back'): ").strip()
                
                if choice.lower() == 'back':
                    return
                
                index = int(choice) - 1
                
                if 0 <= index < len(self.shopping_list):
                    completed_item = self.shopping_list.pop(index)
                    self.completed_items.append(completed_item)
                    print(f"✅ Marked '{completed_item}' as completed!")
                    break
                else:
                    print(f"❌ Please enter number between 1 and {len(self.shopping_list)}")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def edit_item(self):
        """Edit an existing item"""
        if not self.shopping_list:
            print("❌ List is empty!")
            return
        
        self.display_list()
        
        while True:
            try:
                choice = input("\nEnter item number to edit (or 'back'): ").strip()
                
                if choice.lower() == 'back':
                    return
                
                index = int(choice) - 1
                
                if 0 <= index < len(self.shopping_list):
                    old_item = self.shopping_list[index]
                    print(f"Current item: {old_item}")
                    
                    new_item = input("Enter new item name: ").strip()
                    
                    if not new_item:
                        print("❌ Item cannot be empty!")
                        continue
                    
                    self.shopping_list[index] = new_item
                    print(f"✅ Changed '{old_item}' to '{new_item}'")
                    break
                else:
                    print(f"❌ Please enter number between 1 and {len(self.shopping_list)}")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def search_items(self):
        """Search for items in the list"""
        if not self.shopping_list:
            print("❌ List is empty!")
            return
        
        search_term = input("Enter search term: ").strip().lower()
        
        if not search_term:
            print("❌ Search term cannot be empty!")
            return
        
        matches = []
        for i, item in enumerate(self.shopping_list):
            if search_term in item.lower():
                matches.append((i + 1, item))
        
        if matches:
            print(f"\n🔍 Found {len(matches)} matching items:")
            for index, item in matches:
                print(f"  {index}. {item}")
        else:
            print(f"❌ No items found matching '{search_term}'")
    
    def clear_list(self):
        """Clear the entire list with confirmation"""
        if not self.shopping_list:
            print("❌ List is already empty!")
            return
        
        print(f"You have {len(self.shopping_list)} items in your list.")
        
        while True:
            confirm = input("Are you sure you want to clear all items? (yes/no): ").lower()
            
            if confirm in ['yes', 'y']:
                self.shopping_list.clear()
                print("✅ All items cleared!")
                break
            elif confirm in ['no', 'n']:
                print("❌ Clear cancelled.")
                break
            else:
                print("❌ Please enter 'yes' or 'no'")
    
    def show_statistics(self):
        """Show list statistics"""
        total_items = len(self.shopping_list)
        completed_items = len(self.completed_items)
        total_all_time = total_items + completed_items
        
        print(f"\n📊 SHOPPING LIST STATISTICS")
        print("-" * 30)
        print(f"Current items: {total_items}")
        print(f"Completed items: {completed_items}")
        print(f"Total items (all time): {total_all_time}")
        
        if total_all_time > 0:
            completion_rate = (completed_items / total_all_time) * 100
            print(f"Completion rate: {completion_rate:.1f}%")
        
        if self.shopping_list:
            # Find longest item name
            longest_item = max(self.shopping_list, key=len)
            print(f"Longest item name: '{longest_item}' ({len(longest_item)} chars)")
            
            # Check for items with quantities
            qty_items = [item for item in self.shopping_list if '(x' in item]
            if qty_items:
                print(f"Items with quantities: {len(qty_items)}")
    
    def export_list(self):
        """Export list to text format"""
        if not self.shopping_list and not self.completed_items:
            print("❌ No items to export!")
            return
        
        print("\n📤 EXPORTED SHOPPING LIST")
        print("=" * 30)
        print("SHOPPING LIST")
        print("-" * 15)
        
        if self.shopping_list:
            for i, item in enumerate(self.shopping_list, 1):
                print(f"{i}. [ ] {item}")
        else:
            print("(No pending items)")
        
        if self.completed_items:
            print("\nCOMPLETED ITEMS")
            print("-" * 15)
            for item in self.completed_items:
                print(f"[✓] {item}")
        
        print("\n💡 Tip: You can copy this text to save your list!")
    
    def run(self):
        """Main application loop"""
        print("\n🛒 ENHANCED SHOPPING LIST MANAGER")
        print("=" * 40)
        print("Welcome! Manage your shopping list with style!")
        
        while True:
            self.display_list()
            
            print(f"\n📋 MENU OPTIONS")
            print("1. Add item")
            print("2. Remove item")
            print("3. Mark item complete")
            print("4. Edit item")
            print("5. Search items")
            print("6. Clear all items")
            print("7. Show statistics")
            print("8. Export list")
            print("9. Quit")
            
            choice = input("\nChoose option (1-9): ").strip()
            
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.mark_completed()
            elif choice == '4':
                self.edit_item()
            elif choice == '5':
                self.search_items()
            elif choice == '6':
                self.clear_list()
            elif choice == '7':
                self.show_statistics()
            elif choice == '8':
                self.export_list()
            elif choice == '9':
                print("\n👋 Thank you for using Shopping List Manager!")
                if self.shopping_list:
                    print(f"Don't forget your {len(self.shopping_list)} items!")
                print("Happy shopping! 🛍️")
                break
            else:
                print("❌ Invalid choice! Please select 1-9.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")

# STEP 3: Running the Complete Application
print("\n" + "="*50)
print("STEP 3: COMPLETE APPLICATION")
print("="*50)

def demo_shopping_list():
    """Demo the complete shopping list manager"""
    manager = ShoppingListManager()
    
    # Add some demo items
    print("Adding demo items...")
    manager.shopping_list = ["Milk", "Bread (x2)", "Apples", "Chicken", "Rice"]
    manager.completed_items = ["Eggs", "Butter"]
    
    print("Demo data loaded! Here's what the app looks like:")
    manager.display_list()
    manager.show_statistics()
    
    print("\n💡 This is what the full interactive version would look like!")
    print("Uncomment the line below to try the full application:")
    print("# manager.run()")

demo_shopping_list()

# STEP 4: Additional Features Demo
print("\n" + "="*50)
print("STEP 4: ADDITIONAL FEATURES")
print("="*50)

def demonstrate_features():
    """Demonstrate additional features"""
    
    # Smart input validation
    def get_valid_menu_choice(min_val, max_val):
        """Get a valid menu choice with retry logic"""
        while True:
            try:
                choice = int(input(f"Enter choice ({min_val}-{max_val}): "))
                if min_val <= choice <= max_val:
                    return choice
                else:
                    print(f"❌ Please enter a number between {min_val} and {max_val}")
            except ValueError:
                print("❌ Please enter a valid number!")
    
    # Auto-save functionality simulation
    def auto_save_simulation(shopping_list):
        """Simulate auto-saving the list"""
        import json
        
        # In a real app, this would save to a file
        data = {
            "shopping_list": shopping_list,
            "last_updated": "2024-10-09 14:30:00"
        }
        
        print("💾 Auto-saving list...")
        print(f"Saved {len(shopping_list)} items")
        return True
    
    # Smart suggestions
    def suggest_items(current_list):
        """Suggest items based on current list"""
        common_items = {
            "milk": ["bread", "eggs", "butter", "cereal"],
            "bread": ["milk", "butter", "jam", "ham"],
            "apples": ["bananas", "oranges", "grapes"],
            "chicken": ["rice", "vegetables", "seasoning"],
            "pasta": ["tomato sauce", "cheese", "garlic"]
        }
        
        suggestions = set()
        
        for item in current_list:
            item_lower = item.lower()
            for key, values in common_items.items():
                if key in item_lower:
                    suggestions.update(values)
        
        # Remove items already in list
        current_lower = [item.lower() for item in current_list]
        suggestions = [s for s in suggestions if s not in current_lower]
        
        if suggestions:
            print(f"\n💡 SMART SUGGESTIONS based on your list:")
            for suggestion in sorted(suggestions)[:5]:  # Show top 5
                print(f"  • {suggestion.title()}")
        
        return list(suggestions)
    
    # Demo the features
    sample_list = ["Milk", "Bread", "Apples", "Chicken"]
    print("Sample shopping list:", sample_list)
    
    print("\nTesting smart suggestions:")
    suggest_items(sample_list)
    
    print("\nTesting auto-save:")
    auto_save_simulation(sample_list)
    
    print("\nTesting input validation:")
    print("(This would normally prompt for user input)")
    # choice = get_valid_menu_choice(1, 5)

demonstrate_features()

print("\n" + "="*60)
print("🎯 ENHANCED SHOPPING LIST MANAGER COMPLETE!")
print("You've learned how to build:")
print("• Menu-driven applications with while loops")
print("• Robust input validation and error handling")
print("• Interactive user interfaces")
print("• Data management and persistence")
print("• Professional-quality user experience")
print("This pattern can be applied to many different applications!")
print("="*60)

# Uncomment to run the full interactive application:
# if __name__ == "__main__":
#     app = ShoppingListManager()
#     app.run()