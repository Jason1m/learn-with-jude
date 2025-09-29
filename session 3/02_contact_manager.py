# Contact Manager - Session 3 Project

print("📞 CONTACT MANAGER")
print("=" * 20)

contacts = {}

def show_menu():
    print("\n1. Add contact")
    print("2. View contact") 
    print("3. View all contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

def add_contact():
    name = input("Name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Added {name} to contacts!")

def view_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        contact = contacts[name]
        print(f"\n{name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found!")

def view_all():
    if not contacts:
        print("No contacts saved!")
        return
    
    print(f"\nAll Contacts ({len(contacts)}):")
    for name, info in contacts.items():
        print(f"{name}: {info['phone']}")

def update_contact():
    name = input("Enter name: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    
    print("Leave blank to keep current value")
    phone = input(f"Phone ({contacts[name]['phone']}): ").strip()
    email = input(f"Email ({contacts[name]['email']}): ").strip()
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    
    print("Contact updated!")

def delete_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}")
    else:
        print("Contact not found!")

# Main program
def main():
    while True:
        show_menu()
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            view_all()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Demo data
def load_demo():
    contacts["John"] = {"phone": "123-456-7890", "email": "john@email.com"}
    contacts["Alice"] = {"phone": "987-654-3210", "email": "alice@email.com"}
    print("Demo contacts loaded!")

if __name__ == "__main__":
    print("Load demo data? (y/n): ", end="")
    if input().lower() == 'y':
        load_demo()
    main()