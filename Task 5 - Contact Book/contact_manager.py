import json
import os

def load_contacts(filename="contacts.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, 'w') as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} - {c['phone']}")

def search_contacts(contacts):
    query = input("Search by name or phone: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if not found:
        print("No matching contacts found.")
        return
    for c in found:
        print(f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip().lower()
    for c in contacts:
        if c['name'].lower() == name:
            print("Leave blank to keep current value.")
            new_name = input(f"New name [{c['name']}]: ").strip() or c['name']
            new_phone = input(f"New phone [{c['phone']}]: ").strip() or c['phone']
            new_email = input(f"New email [{c['email']}]: ").strip() or c['email']
            new_address = input(f"New address [{c['address']}]: ").strip() or c['address']
            c.update({'name': new_name, 'phone': new_phone, 'email': new_email, 'address': new_address})
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name:
            del contacts[i]
            print(f"Contact '{c['name']}' deleted.")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main() 