import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

def add_contact(contacts):
    """Add a new contact"""
    name = input("👤 Enter contact name: ")
    phone = input("📞 Enter phone number: ")
    if name in contacts:
        print("⚠️ Contact already exists! Use a different name.")
    else:
        contacts[name] = phone
        save_contacts(contacts)
        print(f"✅ Contact added: {name} ({phone})")

def save_contacts(contacts):
    """Save contacts to the file"""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)  # Save contacts in JSON format

def load_contacts():
    """Load contacts from the file if it exists"""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)  # Load contacts from JSON file
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return empty dictionary if file doesn't exist or is corrupted

def show_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("\n📂 No contacts found! Add a new one.")
    else:
        print("\n📞 Your Contacts:")
        for name, phone in contacts.items():
             print(f"📌 {name}: {phone}")

def search_contact(contacts):
    """Search for a contact"""
    name = input("🔍 Enter the contact name to search: ")
    if name in contacts:
        print(f"📌 {name}: {contacts[name]}")
    else:
        print("❌ Contact not found!")

def delete_contact(contacts):
    """Delete a contact"""
    name = input("❌ Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"✅ Contact deleted: {name}")
    else:
        print("❌ Contact not found!")


def main():
    """Main menu for the Contact Book"""
    contacts = load_contacts()

    while True:
        print("\n🔹 Contact Book Menu 🔹")
        print("1️⃣ View Contacts")
        print("2️⃣ Add Contact")
        print("3️⃣ Search Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Exit")

        choice = input("👉 Enter your choice: ")
        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, 4, or 5.")

        
    

if __name__ == "__main__":
    main()