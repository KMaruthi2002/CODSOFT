class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone_number]
        if not found_contacts:
            print("No contacts found.")
        else:
            print("Search Results:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def update_contact(self):
        name = input("Enter contact name to update: ")
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contact_list()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
