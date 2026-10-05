contacts = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]

def remove_contact(contacts, name):
    for contact in contacts:
        if contact == name:
            contacts.remove(contact)
            print(f"{name} has been removed from your contacts.")
            return
    print(f"{name} is not in your contacts.")
        
remove_contact(contacts, "Bob Brown")
