"""14. **Contact Book**: Develop a simple contact book program where users can add, search, and edit contacts.
"""
import os
book = {}

menu = """
**Contact Book**
1.-Add contact.
2.-Search contact.
3.-Edit contact.
4.-Exit."""

def add_contact(name,phone):
    """Add a new contact to the contact book."""
    book[name] = phone
    print(f"Contact {name} added with phone number {phone}.")
    
def search_contact(name):
    """Search for a contact by name."""
    if name in book:
        print(f"Contact: {name}, Phone: {book[name]}")
    else:
        print(f"Contact {name} not found.")

def edit_contact(name,new_phone):
    """Edit the phone number of an existing contact."""
    if name in book:
        book[name] = new_phone
        print(f"Contact: {name} updated with new phone number: {new_phone}")
    else:
        print(f"Contact {name} not found.")
    
while True:
    os.system("clear")
    print(menu)
    choice = input("Choose an option: ")

    match choice:
        case "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name,phone)
            input("Press enter to continue.")
            
        case "2":
            name = input("Enter contact name: ")
            search_contact(name)
            input("Press enter to continue.")
            
        case "3":
            name = input("Enter contact name: ")
            new_phone = input("Enter phone number: ")
            edit_contact(name,new_phone)
            input("Press enter to continue.")
            
        case "4":
            print("Goodbye.")
            break
        
        case _:
            print("Error!, invalid input.")
            input("Press enter to continue.")
        