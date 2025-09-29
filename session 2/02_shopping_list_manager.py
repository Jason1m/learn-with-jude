# Session 2 Project: Simple Shopping List Manager
# This is what students will build step by step

print("🛒 WELCOME TO YOUR SHOPPING LIST MANAGER! 🛒")
print("=" * 50)

# Initialize an empty shopping list
shopping_list = []

def display_menu():
    """Display the main menu options"""
    print("\n📋 SHOPPING LIST MENU:")
    print("1. View shopping list")
    print("2. Add item to list")
    print("3. Remove item from list")
    print("4. Check if item is in list")
    print("5. Clear entire list")
    print("6. Get list statistics")
    print("7. Exit")
    print("-" * 30)

def view_list():
    """Display the current shopping list"""
    print("\n🛍️  YOUR SHOPPING LIST:")
    if not shopping_list:  # If list is empty
        print("   Your list is empty! Time to add some items."),
    else:
        for i, item in enumerate(shopping_list, 1):  # Start counting from 1
            print(f"   {i}. {item}")
    print(f"\n   Total items: {len(shopping_list)}")

def add_item():
    """Add an item to the shopping list"""
    item = input("\n🆕 Enter item to add: ").strip()
    if item:  # Check if item is not empty
        shopping_list.append(item)
        print(f"✅ Added '{item}' to your list!")
    else:
        print("❌ Cannot add empty item!")

def remove_item():
    """Remove an item from the shopping list"""
    if not shopping_list:
        print("\n❌ Your list is empty! Nothing to remove.")
        return
    
    view_list()  # Show current list
    
    print("\nHow would you like to remove an item?")
    print("1. Remove by item name")
    print("2. Remove by position number")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Remove by name
        item = input("Enter item name to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"✅ Removed '{item}' from your list!")
        else:
            print(f"❌ '{item}' not found in your list!")
    
    elif choice == "2":
        # Remove by position
        try:
            position = int(input("Enter position number to remove: "))
            if 1 <= position <= len(shopping_list):
                removed_item = shopping_list.pop(position - 1)  # Convert to 0-based index
                print(f"✅ Removed '{removed_item}' from position {position}!")
            else:
                print(f"❌ Invalid position! Please enter a number between 1 and {len(shopping_list)}")
        except ValueError:
            print("❌ Please enter a valid number!")
    else:
        print("❌ Invalid choice!")

def check_item():
    """Check if an item is in the shopping list"""
    item = input("\n🔍 Enter item to search for: ").strip()
    if item in shopping_list:
        position = shopping_list.index(item) + 1  # Convert to 1-based index
        print(f"✅ '{item}' is in your list at position {position}!")
    else:
        print(f"❌ '{item}' is not in your list.")

def clear_list():
    """Clear the entire shopping list"""
    if not shopping_list:
        print("\n📝 Your list is already empty!")
        return
    
    confirm = input(f"\n⚠️  Are you sure you want to clear all {len(shopping_list)} items? (yes/no): ").strip().lower()
    if confirm in ['yes', 'y']:
        shopping_list.clear()
        print("✅ List cleared successfully!")
    else:
        print("❌ Clear operation cancelled.")

def show_statistics():
    """Show statistics about the shopping list"""
    print(f"\n📊 LIST STATISTICS:")
    print(f"   Total items: {len(shopping_list)}")
    
    if shopping_list:
        print(f"   First item: {shopping_list[0]}")
        print(f"   Last item: {shopping_list[-1]}")
        
        # Find longest and shortest item names
        longest = max(shopping_list, key=len)
        shortest = min(shopping_list, key=len)
        print(f"   Longest item name: '{longest}' ({len(longest)} characters)")
        print(f"   Shortest item name: '{shortest}' ({len(shortest)} characters)")
        
        # Check for duplicates
        unique_items = list(set(shopping_list))
        if len(unique_items) < len(shopping_list):
            print(f"   Unique items: {len(unique_items)} (you have some duplicates!)")
        else:
            print(f"   All items are unique!")

def main():
    """Main program loop"""
    print("Let's create your personalized shopping list!\n")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            view_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            check_item()
        elif choice == "5":
            clear_list()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("\n👋 Thanks for using the Shopping List Manager!")
            print("Happy shopping! 🛒")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number from 1-7.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

# Demo mode for teaching purposes
def demo_mode():
    """Demonstrate the shopping list functionality"""
    print("\n🎯 DEMO MODE - Let's see the shopping list in action!")
    print("=" * 50)
    
    # Add some demo items
    demo_items = ["Milk", "Bread", "Eggs", "Apples", "Chicken"]
    print(f"Adding demo items: {demo_items}")
    
    for item in demo_items:
        shopping_list.append(item)
        print(f"Added: {item}")
    
    print(f"\nFinal shopping list: {shopping_list}")
    print(f"List length: {len(shopping_list)}")
    
    # Demo accessing items
    print(f"\nFirst item: {shopping_list[0]}")
    print(f"Last item: {shopping_list[-1]}")
    print(f"Middle item: {shopping_list[2]}")
    
    # Demo removing items
    print(f"\nRemoving 'Bread'...")
    shopping_list.remove("Bread")
    print(f"List after removal: {shopping_list}")
    
    # Demo inserting
    print(f"\nInserting 'Butter' at position 1...")
    shopping_list.insert(1, "Butter")
    print(f"List after insertion: {shopping_list}")

# Run the program
if __name__ == "__main__":
    # Ask if user wants demo mode or interactive mode
    print("Choose mode:")
    print("1. Interactive mode (you control the list)")
    print("2. Demo mode (see automatic demonstration)")
    
    mode = input("Enter your choice (1 or 2): ").strip()
    
    if mode == "1":
        main()
    elif mode == "2":
        demo_mode()
        print("\nDemo complete! Would you like to try interactive mode?")
        if input("Enter 'yes' to continue: ").strip().lower() in ['yes', 'y']:
            shopping_list.clear()  # Clear demo data
            main()
    else:
        print("Invalid choice. Starting interactive mode by default.")
        main()