
contacts = []
contact = {
            "name": "dan",
            "phone": "22222",
            "email": "dan@email",
            "address": "222 road"
        }
contacts.append(contact)
contact = {
            "name": "nathan",
            "phone": "9999",
            "email": "nath@email",
            "address": "33 road"
        }
contacts.append(contact)

def unique_name(base_name, existing_name):
    names = [contact['name'] for contact in existing_name]
    if base_name not in names:
        return base_name
    name_number = 2
    while True:
        new_name = f"{base_name}{name_number}"
        if new_name not in names:
            return new_name
        name_number += 1


while True:
    contact = {}
    contacts_count = len(contacts)

    user_input = input("\nWould you like to view, add, remove, edit or exit your contact book?: ").lower()

    if user_input == "view":
        if contacts_count == 0:
            print("You currently have no contacts.")
        else:
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}: {contact['name']}")
            view_input = input("\nWhich contact would you like to view? (Leave blank to return): ").lower()
            if view_input == "":
                continue

            # New Code
            elif view_input.isdigit():
                view_input = int(view_input) - 1
                if 0 <= view_input < len(contacts):
                    print(f"\nName: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print(f"Address: {contact['address']}")
                else:
                    print("\nContact does not exist")

            else:
                found = False
                for contact in contacts:
                    if contact['name'] == view_input:
                        print(f"\nName: {contact['name']}")
                        print(f"Phone: {contact['phone']}")
                        print(f"Email: {contact['email']}")
                        print(f"Address: {contact['address']}")
                        found = True
                        break
                if not found:
                    print(f"No contact by the name '{view_input}' found.")


    elif user_input == "add":
        name = input("\nEnter name: ").lower()
        original_name = name
        name = unique_name(name, contacts)
        if name != original_name:
            print(f"'{original_name}' already exists. Adding as '{name}'")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ").lower()
        address = input("Enter address: ").lower()
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        print(f"\nContact {name} added")

    elif user_input == "remove":
        if contacts_count == 0:
            print("You currently have no contacts.")
            continue
        else:
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}: {contact['name']}")
        remove_input = input("\nWhich contact would you like to remove? (Leave blank to return): ").lower()
        if remove_input == "":
            continue

        # New Code
        elif remove_input.isdigit():
                remove_input = int(remove_input) - 1
                if 0 <= remove_input < len(contacts):
                    contacts.pop(remove_input)
                    print("\nContact succesfully removed.")
                else:
                    print("\nContact does not exist")

        else:
            found = False
            for contact in contacts:
                if contact['name'] == remove_input:
                    contacts.remove(contact)
                    print("\nContact succesfully removed.")
                    found = True
            if not found:
                print(f"\nNo contact by the name '{remove_input}' found.")

    elif user_input == "edit":
        if contacts_count == 0:
            print("You currently have no contacts.")
            pass
        for i, contact in enumerate(contacts, start=1):
                print(f"{i}: {contact['name']}")
        edit_input = input("\nWhich contact would you like to edit? (Leave blank to return): ").lower()
        if edit_input == "":
            continue
        
        # New Code
        elif edit_input.isdigit():
            edit_input = int(edit_input) - 1
            if 0 <= edit_input < len(contacts):
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                to_edit = input("\nWhat would you like to edit? Name, Phone, Email, Address or all?: ").lower()
                if to_edit == "name":
                    updated = input("New name: ")
                    contact["name"] = updated
                elif to_edit == "phone":
                    updated = input("New phone number: ")
                    contact["phone"] = updated
                elif to_edit == "email":
                    updated = input("New email: ")
                    contact["email"] = updated
                elif to_edit == "address":
                    updated = input("New address: ")
                    contact["address"] = updated
                elif to_edit == "all":
                    name = input("Enter name: ").lower()
                    phone = input("Enter phone number: ")
                    email = input("Eneter email address: ").lower()
                    address = input("Enter address: ").lower()
                    contact["name"] = name
                    contact["phone"] = phone
                    contact["email"] = email
                    contact["address"] = address
                else:
                    print("\nInvalid selection.")
                
            else:
                print("\nContact does not exist")

        else:
            found = False
            for contact in contacts:
                if contact['name'] == edit_input:
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print(f"Address: {contact['address']}")
                    to_edit = input("\nWhat would you like to edit? Name, Phone, Email, Address or all?: ").lower()
                    if to_edit == "name":
                        updated = input("New name: ")
                        contact["name"] = updated
                    elif to_edit == "phone":
                        updated = input("New phone number: ")
                        contact["phone"] = updated
                    elif to_edit == "email":
                        updated = input("New email: ")
                        contact["email"] = updated
                    elif to_edit == "address":
                        updated = input("New address: ")
                        contact["address"] = updated
                    elif to_edit == "all":
                        name = input("Enter name: ").lower()
                        phone = input("Enter phone number: ")
                        email = input("Eneter email address: ").lower()
                        address = input("Enter address: ").lower()
                        contact["name"] = name
                        contact["phone"] = phone
                        contact["email"] = email
                        contact["address"] = address
                    else:
                        print("\nInvalid selection.")
                    found = True
                    
            if not found:
                print(f"\nNo contact by the name '{edit_input}' found.")
    
    elif user_input == "exit":
        print("\nGoodbye")
        break

    else:
        print("\nPlease enter a valid action (view, add, remove, edit or exit.")