contacts = []
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
   
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"\nContact for {name} added successfully!\n")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
    else:
        print("\nNo contacts found.\n")

def search_contact():
    search_term = input("\nEnter name or phone number to search: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("\nNo contact found with the given details.\n")


def update_contact():
    view_contacts()
    contact_number = int(input("\nEnter the number of the contact to update: "))
    
    if 0 < contact_number <= len(contacts):
        contact = contacts[contact_number - 1]
        print(f"\nUpdating contact: {contact['name']}")
        contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
        contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact['phone']
        contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
        contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
        print("\nContact updated successfully!\n")
    else:
        print("\nInvalid contact number.\n")


def delete_contact():
    view_contacts()
    contact_number = int(input("\nEnter the number of the contact to delete: "))
    
    if 0 < contact_number <= len(contacts):
        contact = contacts.pop(contact_number - 1)
        print(f"\nContact for {contact['name']} deleted successfully!\n")
    else:
        print("\nInvalid contact number.\n")


def main_menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


main_menu()
